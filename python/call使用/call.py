class X(object):
	def __init__(self, a, b, range):
		self.a = a
		self.b = b
		self.range = range
	def __call__(self, a, b):
		self.a = a
		self.b = b
		print('__call__ with （{}, {}）'.format(self.a, self.b))
	def __del__(self, a, b, range):
		del self.a
		del self.b
		del self.range
one_instance=X(1,2,3)
one_instance(1,2)