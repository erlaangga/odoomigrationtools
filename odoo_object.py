import xmlrpclib

class OdooObject:

	def __init__(self, url, db, username, password):
		self.url = url
		self.db = db
		self.username = username
		self.password = password
		self.common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
		print(self.common.version())
		print('Logging In.....')
		self.uid = self.common.authenticate(self.db, self.username, self.password, {})
		self.models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
		# import pdb;pdb.set_trace()
	
	def check_access_rights(self, model_name='res.partner'):
		print('Checking access right of %s:' %model_name),
		res = self.models.execute_kw(self.db, self.uid, self.password,
		    model_name, 'check_access_rights',
		    ['read'], {'raise_exception': False})
		return res

	def fields_get(self, model_name='res.partner'):
		print('Fields of model %s:' %model_name)
		print('=========================================================================')
		res = self.models.execute_kw(self.db, self.uid, self.password,
		    model_name, 'fields_get', [])
		return res

	def search_read(self, model_name, domain=[], fields_name=None):
		print('Fields of model %s:' %model_name)
		print('=========================================================================')
		res = self.models.execute_kw(self.db, self.uid, self.password,
		    model_name, 'search_read', [domain, fields_name])
		return res

	def call(self, model_name='res.partner', function_name='search', args=[]):
		res = self.models.execute_kw(self.db, self.uid, self.password,
		    model_name, function_name, args)
		return res


