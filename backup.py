from netmiko import ConnectHandler
from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)
db = client.config_backup
collection = db.configs



R1 = {
    'device_type': 'cisco_ios',
    'ip': 'xxxx',
    'username': 'xxxx',
    'password': 'xxxx',
    'global_delay_factor': 0,

}
R2 = {
    'device_type': 'xxxx',
    'ip': 'xxxx',
    'username': 'xxxx',
    'password': 'xxxx',
    'global_delay_factor': 0,
}

device_list = [R1, R2]
for router in device_list:
    net_connect = ConnectHandler(**router)
    net_connect.find_prompt()
    net_connect.send_command('terminal length 0')
    host = net_connect.send_command('show run | i hostname')[9:]
    config = net_connect.send_command('show run')
    x = {'host': host, 'data': [{'date': datetime.datetime.now().strftime('%y-%m-%d %H:%M')}, {'config': config}]}
    db.configs.insert_one(x)





