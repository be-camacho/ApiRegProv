from django.apps import AppConfig



class RegprovsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'regprovs'

    def ready(self):
        from . import signals