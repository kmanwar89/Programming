import meraki
import os

'''
General flow:
1) List the organizations/parse the OrgID
2) With the OrgID in hand, grab a list of networks/parse the NetworkID in question
3) Perform whatever other operations are needed
'''

# Define the API key in a secure(ish) way
api=os.getenv("meraki")

# Instantiate a Meraki dashboard API session
def main():
    dashboard = meraki.DashboardAPI(
    api_key=api,
    base_url='https://api-mp.meraki.com/api/v1/',
    #base_url='https://dashboard.meraki.com',
    # output_log=True,
    # log_file_prefix=os.path.basename(__file__)[:-3],
    # log_path='',
    print_console=False
    )
    
    organizations = dashboard.organizations.getOrganizations()
    #print(organizations)

    # Iterate through list of orgs
    for org in organizations:
        #print(f'\nAnalyzing organization {org["name"]}:')
        org_id = org['id']

        # # Get list of networks in organization
        networks = dashboard.organizations.getOrganizationNetworks(org_id)
        
        # Grab the network ID from previous output
        for net in networks:
            net_id = net['id']
        # print(networks)
        #print("The organization ID for the", org['name'], "organization is", org['id'], "and the URL for this dashboard is:", org['url'])




main()