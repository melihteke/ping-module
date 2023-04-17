## PingDevice Class
The PingDevice class is a Python class that allows you to check if a device is online by pinging its IP address.

### Installation
The PingDevice class requires Python 3.6 or later. There are no additional dependencies required.

### Usage
First, import the PingDevice class:

```sh
In [7]: from ping_module import PingDevice
```

Create object and call ping() method.
```sh
In [8]: a = PingDevice(host="192.168.178.1")

In [9]: a.ping()
Out[9]: True

In [10]: a = PingDevice(host="www.ciscoscsdfsdfdsfsfds.com")

In [11]: a.ping()
Out[11]: False
```

