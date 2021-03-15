from netbox import NetBox
netbox = NetBox(host='192.168.1.154', port='', use_ssl=True,
                auth_token='##############')
# The API only accepts certain colors. Need to create a device type for each and define those colors.
# Flow of creation:
# Regions --contain--> Sites --contain--> Devices --belong to--> Device Roles
# 1) Make a region
# 2) Add a site and assign it to a region
# 3) Create device roles for various device types
# 4) Add devices and assign them a device role

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





# netbox.dcim.create_site('Test Site','testsite')
netbox.dcim.create_device_role('test',red,'test')
# netbox.dcim.create_device('test','wlc','Test','wlc')

print(netbox.dcim.get_device_roles())
# print(netbox.dcim.get_devices())
# print(netbox.dcim.get_sites())