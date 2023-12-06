from django.apps import AppConfig

class AplicacoesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicacoes'

    def ready(self):
        import aplicacoes.signals