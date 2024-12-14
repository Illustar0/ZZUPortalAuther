# ZZUPortalAuther
<font color=gray size=3>调用 ZZU.Py 实现的郑州大学校园网多拨认证工具</font>

## Getting Started

```shell
pip install httpx fake_useragent toml psutil
# 如果你正在使用 Openwrt，记得使用 opkg 来安装 psutil
# opkg install python3-psutil
python ZZUPortalAuther.py
# 如果你正在使用 mwan3，请在认证前停用它
```

## Config

```toml
[accounts.one]
usercode="YourAccount"
password="YourPassword"
interfaces=[ "macvlan1","macvlan2","macvlan3","macvlan4" ]
[accounts.two]
usercode="YourAccount"
password="YourPassword"
interfaces=[ "macvlan1","macvlan2","macvlan3","macvlan4" ]
```
## Done & To Do

- [x] 多账号支持

## License

License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)