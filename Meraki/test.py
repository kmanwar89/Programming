import os
import meraki
# Instantiate a Meraki dashboard API session
dashboard = meraki.DashboardAPI(
#	api_key=API_KEY_ENVIRONMENT_VARIABLE,
	api_key = os.environ.get('MERAKI_DASHBOARD_API_KEY'),
    #api_key='',
        base_url='https://api-mp.meraki.com/api/v1/',
        output_log=True,
        log_file_prefix=os.path.basename(__file__)[:-3],
        log_path='',
        print_console=False
    )

organizations=dashboard.organizations.getOrganizations()
print(organizations)
