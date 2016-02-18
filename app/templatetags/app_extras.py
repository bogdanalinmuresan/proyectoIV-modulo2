from django import template
from app.models import Bares

register = template.Library()

@register.inclusion_tag('cats.html')
def get_category_list():
	print "ha cargado get_category_list"
	return {'cats': Bares.objects.all()}