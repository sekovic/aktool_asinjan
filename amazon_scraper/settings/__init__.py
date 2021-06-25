import os

k = 'DJANGO_ENV'
if k in os.environ and os.environ[k] == 'prod':
   from .prod import *
else:
   from .dev import *
