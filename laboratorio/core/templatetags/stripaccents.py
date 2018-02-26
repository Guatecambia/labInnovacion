#taken and modified from: https://gist.github.com/juanique/3427063 , also using: https://gist.github.com/victorono/7633010

from django import template
import unicodedata

register = template.Library()

def stripaccents(value, arg=""):
    return ''.join((c for c in unicodedata.normalize('NFD',str(value)) if unicodedata.category(c) != 'Mn'))

register.filter("stripaccents", stripaccents)