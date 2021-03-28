from netbox import NetBox
import os

API = os.environ.get('NETBOX_API_KEY')

netbox = NetBox(host='192.168.1.154', use_ssl=True, auth_token='API')

red="FF0000"
red_rgb='255,0,0'

#netbox.dcim.create_device_role({"name":"switch", "slug":"switch", "color":'f44336', "vm_role":"false", "description":"first test!"})
netbox.dcim.create_device_role({"name":Test,"slug":test,"color":f44336})
#netbox.dcim.create_device('test','switch','Test','switch')
print(netbox.dcim.get_device_roles())
#print(netbox.dcim.get_devices())
