# Script to find accounting groups
groups = env['res.groups'].search([])
for g in groups:
    ext_id = g.get_external_id().get(g.id, '')
    if 'account' in ext_id or 'Account' in g.name or 'Advis' in g.name or 'Invoic' in g.name:
        print(f"ID: {ext_id} | Name: {g.name}")
