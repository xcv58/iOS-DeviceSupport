# iOS-DeviceSupport
This repository holds the device support files for the iOS, and I will update it regularly.

### Usage:
See docs: [https://ighibli.github.io/2017/03/28/Could-not-locate-device-support-files/](https://ighibli.github.io/2017/03/28/Could-not-locate-device-support-files/)

Below command will try to unzip all new device support files to `/Applications/Xcode.app`.

```sh
sudo ./deploy.py
```

You can use `-t` if your Xcode is not in `/Applications/` or has different name.

```sh
sudo ./deploy.py -t /Applications/Xcode\ 9.app
```

### Supported versions:
1. iOS8
	* 8.0	`2017/04/07`
	* 8.1	`2017/04/07`
	* 8.2	`2017/04/07`
	* 8.3	`2017/04/07`
	* 8.4  `2017/04/07`
2. iOS9
	* 9.0	`2017/04/07`
	* 9.1	`2017/04/07`
	* 9.2	`2017/04/07`
	* 9.3	`2017/04/07`
3. iOS10
	* 10.0 (14A345)	`2017/04/07`
	* 10.0 `2017/12/05`
	* 10.1 (14B72)	`2017/04/07`
	* 10.1 `2017/12/05`
	* 10.2 (14C92)	`2017/04/07`
	* 10.2 `2017/12/05`
	* 10.3 (14E269)	`2017/04/07`
	* 10.3 `2017/12/05`
4. iOS11
	* 11.0 `2017/12/05`
	* 11.1 (15B87)	`2017/12/05`
	* 11.1 `2017/12/11`
	* 11.2 (15C107)	`2017/12/11`
	* 11.2 `2018/03/06`
	* 11.3 (15E5167d)	`2018/01/30`
	* 11.3 (15E5201e)	`2018/03/06`
	* 11.3 `2018/04/09`
	* 11.4 (15F5037c)	`2018/04/09`
	* 11.4 `2018/06/07`
5. iOS12
	* 12.0 (16A5288q)	`2018/06/07`
	* 12.0 (16A5308d)	`2018/06/19`
