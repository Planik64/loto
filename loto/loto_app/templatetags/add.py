from django.template.defaultfilters import register


@register.filter(name='add')
def add(d, k):
    '''Returns the given key from a dictionary.'''
    return d + k - 1