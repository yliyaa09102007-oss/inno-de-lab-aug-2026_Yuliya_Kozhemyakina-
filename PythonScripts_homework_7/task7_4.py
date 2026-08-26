requested_roles = ["guest", "developer", "guest", "admin",
"developer", "guest"]
required_admin_roles = {"admin", "security_officer",
"audit_manager"}

#making a list into a set to deduplicate the list
requested_roles_set = set(requested_roles)
print(f"Уникальные запрошенные роли: {requested_roles_set}")

#using .intersection() to find the common roles
common_roles = requested_roles_set.intersection(required_admin_roles)
print(f"Общие административные роли: {common_roles}")

#using .difference() to find the difference between both sets
missing_roles = required_admin_roles.difference(requested_roles_set)
print(f"Недостающие административные роли: {missing_roles}")

#checking if security officer is present
if "security_officer" in requested_roles_set:
    has_security_officer = True
else:
    has_security_officer = False

print(f"Наличие роли security_officer в запросе: {has_security_officer}")