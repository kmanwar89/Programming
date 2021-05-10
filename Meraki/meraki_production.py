import os
import meraki

# API Key is set as an environmental variable in Windows
key = os.getenv("meraki")

# Instantiate Dashboard object
dashboard = meraki.DashboardAPI(
    api_key=key,
    base_url='https://api-mp.meraki.com/api/v1/',
)

# Get the organization ID
def get_org_id(): 
    organization = dashboard.organizations.getOrganizations()
    # Parse out just the network ID
    for org in organization:
        org_id = org['id']
        org_name = org['name']
        #print("Name: " + org_name + " - ID: " + org_id)
    return org_id, org_name

# # Assign it to a variable
# org_id=get_org_id()

# print(org_id)
# # Get the network ID
# def get_net_id():
#    for net in dashboard.organizations.getOrganizationNetworks(org_id):
#        net_id = net['id']
#    return net_id

# # Assign it to a variable
# net_id=get_net_id()

# # Update device address
# initial_device-update = dashboard.devices.updateDevice(
#     serial ='Q2MN-4YZZ-67PM',
#     name='Home MX64W',
#     address='1908 Nellora Lane Durham, NC 27703',
#     floorPlanID="",
#     notes='Home MX64W Security Appliance',
#     moveMapMarker=True,
#     mac='2C:3F:0B:AC:BB:10'
# )

# print(initial_device_update)

#print(dashboard.devices.getDevice('Q2MN-4YZZ-67PM'))

#create_org = dashboard.organizations.createOrganization('Test')
#print(create_org)
#print(org_id)

# Delete an organization
delete_org = dashboard.organizations.deleteOrganization('622059698530550289')
print(dashboard.organizations.getOrganizations())







# response = dashboard.organizations.claimIntoOrganization(
#     id,
#     orders=['4C3515414'],
#     serials=['Q2MN-4YZZ-67PM'],
#     licenses=[{'key': 'Z2WH-QA7Q-3PHY', 'mode': 'addDevices'}]
# )

# print(response)



'''
TODO:
1) Create a network
2) Add a device to network using SN or Order #
    2a) Read in devices from CSV file?
3) Create an SSID
    3a) Tune wireless settings
'''