import os

environment = os.environ.get("ENVIRONMENT" , 'dev')
if environment == 'dev':
    from .dev import *
elif environment == 'prod':
    from .prod import *