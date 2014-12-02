import sys
sys.path.append(sys.path[0])
from viLogged.wsgi import application
import cherrypy
import json
import win32serviceutil
import win32service


class ViLoggedAPIServer(win32serviceutil.ServiceFramework):
    """NT Service."""

    _svc_name_ = "viLoggedAPI"
    _svc_display_name_ = "viLogged API"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        # create an event that SvcDoRun can wait on and SvcStop
        # can set.
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        cherrypy.tree.graft(application, "/")
        # Unsubscribe the default server
        cherrypy.server.unsubscribe()
        # Instantiate a new server object
        server = cherrypy._cpserver.Server()

        # Configure the server object
        server.socket_host = "0.0.0.0"
        server.socket_port = 8000
        server.thread_pool = 30
        # Subscribe this server
        server.subscribe()
        # Start the server engine (Option 1 *and* 2)
        cherrypy.engine.start()
        cherrypy.engine.block()

        # now, block until our event is set...
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        cherrypy.server.stop()
        win32event.SetEvent(self.stop_event)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ViLoggedAPIServer)