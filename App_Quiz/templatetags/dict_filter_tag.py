from django import template

register = template.Library()


@register.filter(name='dict_filter')
def dict_filter(lst, pk):
    if f'{pk}' in lst:
        print(f'{pk} in {lst}')
        return lst[f'{pk}']
    else:
        print(f'{pk} not in {lst}')
        return None
