import csv
import sys
from odoo_object import OdooObject

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

object1_models = object1.search_read('ir.model', [], ['model'])
object2_models = object2.search_read('ir.model', [], ['model'])

model1_names = {model['model']:model['id'] for model in object1_models}
model2_names = {model['model']:model['id'] for model in object2_models}

model1_names_set = set(model1_names.keys())
model2_names_set = set(model2_names.keys())

model2_names_set.difference(model1_names_set)

# Todo
# save difference model to custom.models.csv

# save every default model to <model>.<name>.csv
# list of default fields (intersection) in a table
# give a break after default fields
# list of custom fields

# csv column format
# field name, type, relation
# if field is not many2one, leave it blank

import pdb;pdb.set_trace()