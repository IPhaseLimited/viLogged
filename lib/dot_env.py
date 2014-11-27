import os
import sys
import warnings


class DotEnv():
#https://github.com/jacobian-archive/django-dotenv/blob/master/dotenv.py
    @staticmethod
    def read_dotenv(dotenv=None):
        """
        Read a .env file into os.environ.

        If not given a path to a dotenv path, does filthy magic stack backtracking
        to find manage.py and then find the dotenv.
        """
        if dotenv is None:
            frame = sys._getframe()
            dotenv = os.path.join(os.path.dirname(frame.f_back.f_code.co_filename), '.env')
            if not os.path.exists(dotenv):
                warnings.warn("not reading %s - it doesn't exist." % dotenv)
                return
        for k, v in DotEnv.parse_dotenv(dotenv):
            os.environ.setdefault(k, v)

    @staticmethod
    def parse_dotenv(dotenv):
        for line in open(dotenv):
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            v = v.strip("'").strip('"')
            yield k, v
