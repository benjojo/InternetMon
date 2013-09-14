import time
import subprocess
import httplib, urllib # Used for the Advanced contact parts.

def GetConfigPart(target):
    try:
        ins = open( "config.cfg", "r" )
        for line in ins:
            parts = line.split('=')
            if parts[0] == target:
                return parts[1]
        return 0
    except IOError:
        return 0

def ContactHost(url,info):
    params = urllib.urlencode({'timedown': info})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection(url.split('/')[0])
    conn.request("POST", url[url.index("/",7):], params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    conn.close()

proc = subprocess.Popen(['ping','8.8.8.8'],
                       #shell=True,
                       stdout=subprocess.PIPE,
                       )

TheInternetIsDown = 0
downtime = int(time.time())
while proc.poll() is None:
    output = proc.stdout.readline()
    if "Destination Host Unreachable" in output:
        if TheInternetIsDown == 0:
            TheInternetIsDown = 1
            downtime = int(time.time())
            print str(int(time.time())) + " Internet is down"
    if "from 8.8.8.8:" in output:
        if TheInternetIsDown == 1:
            print str(int(time.time())) + " Internet is back"
            if GetConfigPart("contacturl") != 0:
                ContactHost(GetConfigPart("contacturl"),str((int(time.time()) - downtime))) # Send off the info to the remote server since the url is in the config file.
            print str(int(time.time())) + " Down for " + str((int(time.time()) - downtime)) + " secs"
            TheInternetIsDown = 0