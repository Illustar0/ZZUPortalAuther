# ZZUPortalAuther
<font color=gray size=3>调用 [ZZU.Py](https://github.com/Illustar0/ZZU.Py) 实现的郑州大学校园网多拨认证工具</font>

## Getting Started

```shell
# 如果你正在使用 Openwrt，记得先使用 opkg 来安装 psutil
# opkg install python3-psutil
pip install zzupy psutil
python ZZUPortalAuther.py
# 如果你正在使用 mwan3，请在认证前停用它
# 接下来，crontab 会很有用
```

## Config

```toml
[accounts.one]
usercode="YourAccount"
password="YourPassword"
isp="campus"
interfaces=[ "macvlan1","macvlan2","macvlan3","macvlan4" ]
[accounts.two]
usercode="YourAccount"
password="YourPassword"
isp="cm"
interfaces=[ "macvlan5","macvlan6","macvlan7","macvlan8" ]
```
## Done & To Do

- [x] 多账号支持
- [x] 多运营商支持

## 碎碎念
移动宽带为多终端共享带宽，多拨已无实际作用
后续（可能）接入的电信和联通宽带大抵也是这种模式

## License

License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)