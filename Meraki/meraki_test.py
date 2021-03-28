import csv
from datetime import datetime
import os
import meraki

dashboard = meraki.DashboardAPI(
        api_key='',
        base_url='https://api-mp.meraki.com/api/v1/',
        output_log=True,
        log_file_prefix=os.path.basename(__file__)[:-3],
        log_path='',
        print_console=True
    )

print(dashboard.organizations.getOrganizations())
