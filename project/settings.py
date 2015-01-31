from platform import node

DEVELOPMENT_HOST = 'vesperalwall860-HP-ENVY-m6-Notebook-PC'
PRODUCTION_HOST = 'apache2-python.2.2.31300.but-service'

if node() == DEVELOPMENT_HOST:
    from project.settings_development import *
elif node() == PRODUCTION_HOST:
    from project.settings_production import *
else:
    raise Exception("Cannot determine execution mode for host '%s'.  Please check DEVELOPMENT_HOST and PRODUCTION_HOST in settings_local.py." % node())