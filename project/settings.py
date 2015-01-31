from platform import node

from project.settings_local import *

if node() == DEVELOPMENT_HOST:
    from project.settings_development import *
elif node() == PRODUCTION_HOST:
    from project.settings_production import *
else:
    raise Exception("Cannot determine execution mode for host '%s'.  Please check DEVELOPMENT_HOST and PRODUCTION_HOST in settings_local.py." % node())