from django import template

register = template.Library()

@register.filter(name='custom_cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('cut', cut)