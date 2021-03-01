# odoomigrationtools
Migration can be boring, so I decided to create this to help people migrating from Odoo version

- Running Odoo instance with custom environment.
- Default Odoo db.
- Custom Odoo db.

Run compareobjectmodel.py to get comparation of difference model, so we can directly create lists of custom object for future development.

```
python compareobjectmodel.py source_host source_db source_username source_password target_host target_db target_admin target_password
```

example:

```
python compareobjectmodel.py http://localhost:8069 db_default admin 1 http://localhost:8069 db_custom admin 1
```