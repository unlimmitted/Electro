from .models import *

header = [{'title': 'Electro',
           'exit': 'Выйти', 'login': 'Войти',
           'register': 'Регистрация'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['header'] = header
        return context