import time
import httpx
from fake_useragent import UserAgent
import base64
import socket
import toml
import psutil

config = toml.load('config.toml')
account = config['Account']['account']
password = config['Account']['password']
interfaces = config['Settings']['interfaces']

try:
    baseLoginURL = config['Settings']['baseLoginURL']
except:
    baseLoginURL = 'http://10.2.7.8:801/eportal/portal/login'



def getIPByInterface(interface):
    addresses = psutil.net_if_addrs()
    if interface in addresses:
        for addr in addresses[interface]:
            if addr.family == socket.AF_INET:
                return addr.address
    return None
def createClient(interface):
    transport = httpx.HTTPTransport(local_address=getIPByInterface(interface))
    client = httpx.Client(transport=transport)
    return client

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'http://10.2.7.8/',
    'User-Agent': UserAgent().random,
}

for interface in interfaces:
    params = [
        ('callback', 'dr1003'),
        ('login_method', '1'),
        ('user_account', f',0,{account}'),
        ('user_password', base64.b64encode(password.encode()).decode()),
        ('wlan_user_ip', getIPByInterface(interface)),
        ('wlan_user_ipv6', ''),
        ('wlan_user_mac', '000000000000'),
        ('wlan_ac_ip', ''),
        ('wlan_ac_name', ''),
        ('jsVersion', '4.2.1'),
        ('terminal_type', '1'),
        ('lang', 'zh-cn'),
        ('v', '1262'),
        ('lang', 'zh'),
    ]
    client=createClient(interface)
    response = client.get(baseLoginURL, params=params, headers=headers)
    print(f"{interface}: {response.text}")
    time.sleep(1)
