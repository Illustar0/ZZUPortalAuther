# ZZUPortalAuther
<font color=gray size=3>Portal authentication for Zhengzhou University campus network.</font>

## Getting Started

```shell
pip install httpx fake_useragent toml psutil
# If you are using OpenWrt then you should install psutil via opkg instead of PIP!
# opkg install python3-psutil
python ZZUPortalAuther.py
# Using crontab might be a good idea
```

## Config

```toml
[Account]
account="YourAccount"
password="YourPassword"
[Settings]
# Your interfaces
interfaces=[ "macvlan1","macvlan2","macvlan3","macvlan4" ]
```
## To Do

- [ ] Multi-account support

## License

License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)