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
        cherrypy.tree.mount(application(), '/')

        # in practice, you will want to specify a value for
        # log.error_file below or in your config file.  If you
        # use a config file, be sure to use an absolute path to
        # it, as you can't be assured what path your service
        # will run in.
        cherrypy.config.update({
            'global':{
                'engine.autoreload.on': False,
                'log.screen': False,
                'engine.SIGHUP': None,
                'engine.SIGTERM': None
                }
            })
        # set blocking=False so that start() does not block
        cherrypy.server.quickstart()
        cherrypy.engine.start(blocking=False)
        # now, block until our event is set...
        win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        cherrypy.server.stop()
        win32event.SetEvent(self.stop_event)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ViLoggedAPIServer)