# Debug script to find correct field names
admin = env.ref('base.user_admin')
print(f"Admin: {admin}")
print(f"Admin Model: {admin._name}")
try:
    print(f"Group-related fields on User: {[f for f in admin._fields if 'group' in f]}")
except:
    print("Could not inspect User fields")

group = env.ref('base.group_user') # Internal User group
print(f"Group: {group}")
print(f"Group Model: {group._name}")
try:
    print(f"User-related fields on Group: {[f for f in group._fields if 'user' in f]}")
except:
    print("Could not inspect Group fields")
