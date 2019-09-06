from django.apps import AppConfig


class GraphConfig(AppConfig):
    name = 'graph'

    def ready(self):
        print('hello')
        # pass  # startup code here
