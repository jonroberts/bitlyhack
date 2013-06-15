import sys, os

DEBUG   = True
ROOT    = os.path.dirname(os.path.abspath(__file__))
INTERP  = '/home/jr_hack/ezip.jrsandbox.com/venv/bin/python'

sys.path.insert(1,ROOT)
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

from theApp import app as application

#if DEBUG:
#   application.debug=True
#   from werkzeug_debugger_appengine import get_debugged_app
#   application = get_debugged_app(application)