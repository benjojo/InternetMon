import time
import subprocess
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
            print str(int(time.time())) + " Down for " + str((int(time.time()) - downtime)) + " secs"
            TheInternetIsDown = 0
        #print output
