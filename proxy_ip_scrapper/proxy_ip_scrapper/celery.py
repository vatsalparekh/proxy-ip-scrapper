from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


class Config:
    # Configuration for celery tasks::

    BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672//'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'


# Set default configuration module name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proxy_ip_scrapper.settings')


# Create instance of Celery
app = Celery('proxy_ip_scrapper')


# This method load configuration from a configuration object.
# Any configuration that was previously set will be reset when this method is called
# So additional configuration should be written after this method
app.config_from_object(Config)
# Here Config is a class which include all configurations for celery


# To find tasks.py file from apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
