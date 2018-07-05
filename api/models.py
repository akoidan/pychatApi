import random
import string

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.db.models import FileField


def id_generator(size=16, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def get_random_path(instance, filename):
	"""
	:param filename base string for generated name
	:return: a unique string filename
	"""
	return "{}_{}".format(id_generator(8), filename)

class UploadedFile(models.Model):
	file = FileField(upload_to=get_random_path, null=True)

# Create your models here.
