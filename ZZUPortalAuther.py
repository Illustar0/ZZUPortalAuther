import time
import httpx
from fake_useragent import UserAgent
import base64
import socket
import toml
import psutil
import random

config = toml.load('config.toml')
account = config['Account']['account']
password = config['Account']['password']
interfaces = config['Settings']['interfaces']

try:
    baseURL = config['Settings']['baseURL']
except:
    baseURL = 'http://10.2.7.8:801'


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


def login(client, baseURL, ua):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://10.2.7.8/',
        'User-Agent': ua,
    }
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
        ('v', str(random.randint(500, 10499))),
        ('lang', 'zh'),
    ]
    response = client.get(f"{baseURL}/eportal/portal/login", params=params, headers=headers)
    return interface, response.text


def chkstatus(client, baseURL, ua):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://10.2.7.8/a79.htm',
        'User-Agent': ua,
    }

    params = {
        'callback': 'dr1002',
        'jsVersion': '4.X',
        'v': str(random.randint(500, 10499)),
        'lang': 'zh',
    }
    client.get(f"{baseURL}/drcom/chkstatus", params=params, headers=headers)


def loadConfig(client, baseURL, ua):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'http://10.2.7.8/',
        'User-Agent': ua,
    }

    params = {
        'callback': 'dr1001',
        'program_index': '',
        'wlan_vlan_id': '1',
        'wlan_user_ip': base64.b64encode(getIPByInterface(interface).encode()).decode(),
        'wlan_user_ipv6': '',
        'wlan_user_ssid': '',
        'wlan_user_areaid': '',
        'wlan_ac_ip': '',
        'wlan_ap_mac': '000000000000',
        'gw_id': '000000000000',
        'jsVersion': '4.X',
        'v': str(random.randint(500, 10499)),
        'lang': 'zh',
    }
    client.get(f"{baseURL}/eportal/portal/page/loadConfig", params=params, headers=headers)


for interface in interfaces:
    client = createClient(interface)
    User_Agent = UserAgent().random
    chkstatus(client, baseURL, User_Agent)
    loadConfig(client, baseURL, User_Agent)
    i, r = login(client, baseURL, User_Agent)
    print(f"{i}: {r}")
    time.sleep(1)
