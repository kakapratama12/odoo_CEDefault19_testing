# Script to enable accounting permissions (Robust Search v3, correct field name)
import logging
_logger = logging.getLogger(__name__)

admin = env.ref('base.user_admin')
if not admin:
    raise Exception("Admin user not found")

# Search for groups by name
groups = env['res.groups'].search([
    '|', '|', '|',
    ('name', 'ilike', 'Show Full Accounting Features'),
    ('name', 'ilike', 'Advisor'),
    ('name', 'ilike', 'Administrator'),
    ('name', 'ilike', 'Analytic Accounting')
])

print(f"Found {len(groups)} potential groups.")

for group in groups:
    ext_ids = group.get_external_id()
    xml_id = ext_ids.get(group.id, '')
    
    # Filter based on known accounting keywords in XML ID or Name
    if 'account' in xml_id or 'analytic' in xml_id or 'Account' in group.name or 'Advis' in group.name:
        print(f"Checking group: {group.name} (XML ID: {xml_id})")
        try:
            # Check if user already in group to avoid unnecessary writes
            # Use 'group_ids' (singular group, plural ids) which seems to be correct for Odoo 19
            if group.id not in admin.group_ids.ids:
                admin.write({'group_ids': [(4, group.id)]})
                print(f"Added Admin to {group.name}")
            else:
                print(f"Admin already in {group.name}")
        except Exception as e:
            print(f"Error adding to {group.name}: {e}")

env.cr.commit()
print("Permissions update complete.")
