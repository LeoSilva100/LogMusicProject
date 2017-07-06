from django import template
from ..models import ImageData

register = template.Library()

@register.filter(name='profileimage')
def profileimage(value):
	try:
		profile = ImageData.objects.get(user=value)
		if profile:			
			if profile.profile:
				print(profile.profile.url)
				return profile.profile.url
			else:
				return False
	except ObjectDoesNotExist:
		return False

@register.filter(name='coverimage')
def coverimage(value):
	try:
		cover = ImageData.objects.get(user=value)
		if cover:			
			if cover.cover:
				return cover.cover.url
			else:
				return False
	except ObjectDoesNotExist:
		return False