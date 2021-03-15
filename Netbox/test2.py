from netbox import NetBox
netbox = NetBox(host='192.168.35.4', port='', use_ssl=True, auth_token='#########')

red="FF0000"
red_rgb='255,0,0'

netbox.dcim.create_device_role('Switch','f44336','switch')
#netbox.dcim.create_device('test','switch','Test','switch')
print(netbox.dcim.get_device_roles())
#print(netbox.dcim.get_devices())
