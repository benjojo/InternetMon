Internet Monitor
=============

So because of a certain ISP having certain issues providing my broadband and not believing that the problem is exists.

This python script was made to run in the background on a [Raspberry Pi](http://en.wikipedia.org/wiki/Raspberry_Pi "rPi") to keep an eye on when the router hung up from the internet.

It works by tailing the output of "ping". The router usefully responds with "Destination Unreachable" when it has hung up so I use that to determine if the internet is down or not.

Sample output is as follows
```
root@raspberrypi:~# python IsTheFuckingInternetDown.py
1379164295 Internet is down
1379164358 Internet is back
1379164358 Down for 63 secs
```

It is recommended to run this in [Screen](http://en.wikipedia.org/wiki/GNU_Screen) to make sure its running all the time.

You can do that like so:

```
root@raspberrypi:~# screen -dS InternetMon ./Run.sh
root@raspberrypi:~#
```

It will then run on its own until the system dies.

##URL Logging
There is functionality to allow when internet comes back up on the host. For a POST request to be sent to a URL of your choice, This URL can then do whatever you want.

Even tweet a complaint to the ISP for you!

To have this functionality to work you will need to check in `config.cfg` and set a URL as follows
```
contacturl=http://server.somewhere.dev/internettracker.php
```

The variable that is sent is the time that the internet was unavailable for and is called `timedown` and can be grabbed in php like so:
```php
<?php
$TimeDown = (int)$_POST['timedown']
```
