from netbox import NetBox
netbox = NetBox(host='192.168.1.154', port='', use_ssl=True, auth_token='#########')

#print(netbox.dcim.get_device_roles())
#print(netbox.dcim.get_devices())


netbox.dcim.create_device()