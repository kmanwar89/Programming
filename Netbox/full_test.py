from netbox import NetBox
import os

'''
Add some code here later on to dynamically grab API keys, add them to ~/.env and source that file into .bashrc
    search for .env in ~
        if the file exists
            set "counter" variable to 1 and exit
        otherwise
            var = input("please enter your environment variable in the form KEY=VALUE)
'''

auth = os.getenv('NETBOX_API_KEY')
netbox = NetBox(host='192.168.1.154', port='', use_ssl=True,
                auth_token=auth, ssl_verify=False)

# Purpose: Demonstrating end-to-end flow of interacting with NetBox in a programmatic way
# Programmer: Kadar Anwar
# Language: Python 3.8.5
# Filename: full_test.py
# Versioning: 22 MAR 2021 - v0.1

'''
The general flow is:
1) Create a region
2) Create a site & assign it to a region; can add additional attributes such as description, location, rack info, ASN, etc.
3) Create device roles (routers, switch, servers, printer, etc)
4) Create devices and assign them to device roles (required parameter)
'''

#netbox.dcim.create_region("AMER","amer")
#netbox.dcim.delete_region("AMER")
#netbox.dcim.create_site("Home","home")
#print(netbox.dcim.get_sites())

# Colors for device roles
# amber	=	'ffc107'
# aqua	=	'00ffff'
# black	=	'111111'
# blue	=	'2196f3'
# brown	=	'795548'
# cyan	=	'00bcd4'
# dark_green	=	'2f6a31'
# dark_grey	=	'607d8b'
# dark_orange	=	'ff5722'
# dark_purple	=	'673ab7'
# dark_red	=	'aa1409'
# fuschia	=	'ff66ff'
# green	=	'4caf50'
# grey	=	'9e9e9e'
# indigo	=	'3f51b5'
# light_blue	=	'03a9f4'
# light_green	=	'8bc34a'
# light_grey	=	'c0c0c0'
# lime	=	'cddc39'
# orange	=	'ff9800'
# pink	=	'e91e63'
# purple	=	'9c27b0'
# red	=	'f44336'
# rose	=	'ffe4e1'
# teal	=	'009968'
# white	=	'ffffff'
# yellow	=	'ffeb3b'
netbox.dcim.create_device_role(name='Layer 3 Switch', color='8bc34a', slug='switch')

print(netbox.dcim.get_device_roles())
