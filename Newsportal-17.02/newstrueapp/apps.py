from django.apps import AppConfig


class NewstrueappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newstrueapp'
    def ready(self):
        import newstrueapp.signals