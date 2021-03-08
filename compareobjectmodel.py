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

print('Odoo Source')
object1 = OdooObject(url1, db1, username1, password1)
print('====================================================================')
print('Odoo Target')
object2 = OdooObject(url2, db2, username2, password2)
print('====================================================================')

object1_models = object1.search_read('ir.model', [], ['model'])
object2_models = object2.search_read('ir.model', [], ['model', 'transient'])

model1_names = [model['model'] for model in object1_models]
model2_names = {model['model']:model['transient'] for model in object2_models}

model1_names_set = set(model1_names)
model2_names_set = set(model2_names.keys())

models_difference = model2_names_set.difference(model1_names_set)

# Todo
# save difference model to custom.models.csv
with open('custom.models.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for model_name in models_difference:
        print('Writing %s structure' %model_name)
        print('====================================================================')
        no=1
        employee_writer.writerow(['model', model_name, 'transient', model2_names[model_name]])
        try:
            fields = object2.fields_get(model_name)
        except:
            failed_msg = 'failed to get fields list of %s' %model_name
            employee_writer.writerow([failed_msg])
            employee_writer.writerow(['', '', '', '', ''])
            print(failed_msg)
            continue
        employee_writer.writerow(['no', 'field', 'type', 'relation', 'string'])
        for field in fields:
            field_attr = fields[field]
            employee_writer.writerow([no, field, field_attr['type'],field_attr.get('relation', ''), field_attr['string']])
            no+=1
        employee_writer.writerow(['', '', '', '', ''])

# save every default model to <model>.<name>.csv
# list of default fields (intersection) in a table
# give a break after default fields
# list of custom fields

# with open('custom.models.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

# csv column format
# no, field name, type, relation
# if field is not many2one, leave it blank

import pdb;pdb.set_trace()