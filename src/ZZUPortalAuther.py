from zzupy import ZZUPy
import toml

config = toml.load("config.toml")
try:
    base_url = config["settings"]["baseurl"]
except:
    base_url = "http://10.2.7.8:801"
for name, data in config["accounts"].items():
    usercode = data["usercode"]
    password = data["password"]
    isp = data["isp"]
    client = ZZUPy(usercode, password)
    for interface in data["interfaces"]:
        print(client.Network.portal_auth(interface, base_url, isp=isp))
