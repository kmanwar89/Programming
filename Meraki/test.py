import os
import meraki

# API Key is set as an environmental variable in Windows
key = os.getenv("meraki")

# Instantiate Dashboard object
dashboard = meraki.DashboardAPI(
    api_key=key,
    base_url='https://api-mp.meraki.com/api/v1/',
    print_console=True,
)

orgs = dashboard.organizations.getOrganizations()
print(orgs)