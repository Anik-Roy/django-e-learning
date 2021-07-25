from django import template
from math import ceil

register = template.Library()


@register.filter(name='category_range_filter')
def category_range_filter(value):
    if len(value) > 16:
        return value[0:15]+'...'
    return value


@register.filter(name='title_range_filter')
def title_range_filter(value):
    if len(value) > 20:
        return value[0:20]+'...'
    return value


@register.filter(name='content_range_filter')
def content_range_filter(value):
    if len(value) > 600:
        return value[0:600]+'...'
    return value


@register.filter(name='remove_html_img_tags')
def remove_html_img_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<img.*?>')
    return re.sub(clean, '', text)


@register.filter(name='content_range_filter_for_profile_page')
def content_range_filter(value):
    if len(value) > 50:
        return value[0:50]+'...'
    return value


@register.filter(name='encode_plus')
def encode_plus(value):
    return value.replace('+', '%2B')


@register.filter(name='as_chunks')
def as_chunk(lst, chunk_size):
    limit = ceil(len(lst) / chunk_size)
    for idx in range(limit):
        yield lst[chunk_size*idx:chunk_size*(idx+1)]
