import sugarcrm

# This is the URL for the wsdl resource in your SugarCRM instance.
WSDL_URL = 'http://127.0.0.1/sugarcrm/service/v2/soap.php?wsdl'
USERNAME = 'admin'
PASSWORD = 'password'

# Leave these two parameters blank if you're not using LDAP authentication.
LDAP_PASSWD = ''
LDAP_IV = ''

# This way you log-in to your SugarCRM instance. You must specify the list of
# modules you are planning to access.
instance = sugarcrm.SugarInstance(WSDL_URL, USERNAME, PASSWORD,
                                    ['Contacts', 'Cases'], LDAP_PASSWD, LDAP_IV)

# This way you query all the Contacts in your database...
q1 = instance.modules['Contacts'].query()
# ... but we just show the first ten of them.
for contact in q1[:10]:
    print contact['first_name'] + ' ' + contact['last_name']

# OUTPUT:
# Darrin Adger
# Gilbert Adkins
# Maritza Bail
# Morris Balmer
# Polly Barahona
# Claude Barksdale
# Merrill Barragan
# Aimee Bassler
# Rosario Bassler
# Gil Batten

# We define a new query, but this time we specify a couple of query exclusions.
q2 = instance.modules['Contacts'].query()
q2.exclude(last_name__exact = 'Bassler')
q2.exclude(first_name__exact = 'Morris')
for contact in q2[:10]:
    print contact['first_name'] + ' ' + contact['last_name']

# OUTPUT:
# Darrin Adger
# Gilbert Adkins
# Maritza Bail
# Polly Barahona
# Claude Barksdale
# Merrill Barragan
# Gil Batten
# Rodrigo Baumeister
# Lakesha Bernhard
# Bryon Bilbo

# This new query has a filter. Please notice that the filter parameter is the
# field name in the SugarCRM module, followed by a double underscore, and then
# an operator (it can be 'exact', 'contains', 'gt', 'gte', 'lt', 'lte' or 'in').
q3 = instance.modules['Contacts'].query()
q3.filter(last_name__contains='ass')
for contact in q3[:10]:
    print contact['first_name'] + ' ' + contact['last_name']

# OUTPUT:
# Aimee Bassler
# Rosario Bassler
# Blake Cassity
# Ann Hassett

q4 = instance.modules['Contacts'].query()
q4.filter(last_name__in=['Bassler', 'Everitt'])
for contact in q4[:10]:
    print contact['first_name'] + ' ' + contact['last_name']

# OUTPUT:
# Aimee Bassler
# Rosario Bassler
# Stanford Everitt

q5 = instance.modules['Cases'].query()
q5.filter(case_number__lt='7')
for case in q5[:10]:
    print case['case_number'] + ' / ' + case['name'] + ' / ' + case['description']

# OUTPUT:
# 1 / Having trouble adding new items / 
# 2 / Warning message when using the wrong browser / 
# 3 / Having trouble adding new items / 
# 4 / Having trouble adding new items / 
# 5 / Need assistance with large customization / 
# 6 / Need to purchase additional licenses / 
