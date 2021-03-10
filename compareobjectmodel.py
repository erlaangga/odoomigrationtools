# coding: utf8
import csv
import os
import sys
from odoo_object import OdooObject

os.environ["PYTHONIOENCODING"] = "utf-8"
if not os.path.exists('csv'):
    os.mkdir('csv')

url1 = sys.argv[1]
db1 = sys.argv[2]
username1 = sys.argv[3]
password1 = sys.argv[4]

url2 = sys.argv[5]
db2 = sys.argv[6]
username2 = sys.argv[7]
password2 = sys.argv[8]

current_path = os.getcwd()

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
with open(current_path+'\\csv\\'+'custom.models.csv', mode='w') as custom_model_file:
    model_writer = csv.writer(custom_model_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for model_name in models_difference:
        print('Writing %s structure' %model_name)
        print('====================================================================')
        no=1
        model_writer.writerow(['model', model_name, 'transient', model2_names[model_name]])
        try:
            fields = object2.fields_get(model_name)
        except:
            failed_msg = 'failed to get fields list of %s' %model_name
            model_writer.writerow([failed_msg])
            model_writer.writerow(['', '', '', '', ''])
            print(failed_msg)
            continue
        model_writer.writerow(['no', 'field', 'type', 'relation', 'string'])
        for field in fields:
            field_attr = fields[field]
            model_writer.writerow([no, field, field_attr['type'],field_attr.get('relation', ''), field_attr['string'].encode('utf-8')])
            no+=1
        model_writer.writerow(['', '', '', '', ''])
        model_writer.writerow(['', '', '', '', ''])

# save every default model to <model>.<name>.csv
# list of default fields (intersection) in a table
# give a break after default fields
# list of custom fields
# give two breaks after fields

models_intersection = model2_names_set.intersection(model1_names_set)
for model_name in models_intersection:
    with open(current_path+'\\csv\\'+model_name+'.csv', mode='w') as model_file:
        model_writer = csv.writer(model_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        print('Writing %s structure' %model_name)
        print('====================================================================')
        no=1
        model_writer.writerow(['model', model_name, 'transient', model2_names[model_name]])
        try:
            fields1 = object1.fields_get(model_name)
            fields2 = object2.fields_get(model_name)
        except:
            failed_msg = 'failed to get fields list of %s' %model_name
            model_writer.writerow([failed_msg])
            model_writer.writerow(['', '', '', '', ''])
            print(failed_msg)
            continue
        fields_intersection = set(fields2.keys()).intersection(fields1.keys())
        fields_difference = set(fields2.keys()).difference(fields1.keys())
        model_writer.writerow(['no', 'field', 'type', 'relation', 'string'])
        for field in fields_intersection:
            field_attr = fields[field]
            model_writer.writerow([no, field, field_attr['type'],field_attr.get('relation', ''), field_attr['string'].encode('utf-8')])
            no+=1
        model_writer.writerow(['', '', '', '', ''])
        for field in fields_difference:
            field_attr = fields[field]
            model_writer.writerow([no, field, field_attr['type'],field_attr.get('relation', ''), field_attr['string'].encode('utf-8')])
            no+=1
        model_writer.writerow(['', '', '', '', ''])
        model_writer.writerow(['', '', '', '', ''])

# csv column format
# no, field name, type, relation, string
# if field is not many2one, leave it blank
import pdb;pdb.set_trace()