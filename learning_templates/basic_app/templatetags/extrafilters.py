from atexit import register
from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value,args):
    
    """
    this cuts out all values of args from the string
    """
    return value.replace('args','')

# register.filter('cut', cut)
