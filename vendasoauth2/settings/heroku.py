import environ
from vendasoauth2.settings.base import *
import dj_database_url

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
   # "default": env.db(),
"default": dj_database_url.config(),
}