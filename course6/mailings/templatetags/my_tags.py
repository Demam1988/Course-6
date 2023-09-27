from django import template

from users.models import User

register = template.Library()


# Создание тега
@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.simple_tag()
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.inclusion_tag('users/not_found_user.html')
def get_user(email=None):
    if not email:
        return 'Пользователь с указанным email не найден'
    else:
        user = User.objects.get(email='email')
        return {'user': user}
