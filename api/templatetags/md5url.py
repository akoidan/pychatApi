import hashlib
import threading
from os import path

from django import template

from pychatApi.settings import STATIC_URL, STATIC_ROOT

register = template.Library()



class UrlCache(object):
	_md5_sum = {}
	_lock = threading.Lock()

	@classmethod
	def get_md5(cls, file_name):
		try:
			return cls._md5_sum[file_name]
		except KeyError:
			with cls._lock:
				try:
					md5 = cls.calc_md5(path.join(STATIC_ROOT, file_name))[:8]
					value = '%s%s?v=%s' % (STATIC_URL, file_name, md5)
				except:
					value = STATIC_URL + file_name
				cls._md5_sum[file_name] = value
				return value

	@classmethod
	def calc_md5(cls, file_path):
		with open(file_path, 'rb') as fh:
			m = hashlib.md5()
			while True:
				data = fh.read(8192)
				if not data:
					break
				m.update(data)
			return m.hexdigest()


@register.simple_tag
def md5url(file_name):
	return UrlCache.get_md5(file_name)
