from odoo_object import OdooObject
import sys

url1 = sys.argv[1]
db1 = sys.argv[2]
username1 = sys.argv[3]
password1 = sys.argv[4]

url2 = sys.argv[5]
db2 = sys.argv[6]
username2 = sys.argv[7]
password2 = sys.argv[8]

object1 = OdooObject(url1, db1, username1, password1)
object2 = OdooObject(url2, db2, username2, password2)

partner1_fields = object1.search_read('ir.model', [], ['model'])
partner2_fields = object2.search_read('ir.model', [], ['model'])

model1_names = {model['model']:model['id'] for model in partner1_fields}
model2_names = {model['model']:model['id'] for model in partner2_fields}

model1_names_set = set(model1_names.keys())
model2_names_set = set(model2_names.keys())

model2_names_set.difference(model1_names_set)

import pdb;pdb.set_trace()