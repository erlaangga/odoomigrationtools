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

model_name = sys.argv[9]

object1 = OdooObject(url1, db1, username1, password1)
object2 = OdooObject(url2, db2, username2, password2)

partner1_fields = object1.fields_get(model_name)
partner2_fields = object2.fields_get(model_name)

partner1_fields_set = set(partner1_fields.keys())
partner2_fields_set = set(partner2_fields.keys())

partner_fields_difference_set = partner2_fields_set.difference(partner1_fields_set)

import pdb;pdb.set_trace()