import pyshark
import datetime
import time

capture = pyshark.LiveCapture(interface = 'lo',bpf_filter='port 4040')
capture.sniff(timeout = 10)
tcpbazersal=0
sumtool = 0
counter = 0
sumtime = 0

for i in range(len(capture)):
    sumtool += len(capture[i])
    counter += 1

firstdelaytime=capture[0].sniff_timestamp
seconddelaytime=capture[len(capture)-1].sniff_timestamp
firsttime = float(firstdelaytime)
secondtime = float(seconddelaytime)
sumtime = secondtime - firsttime
capture.close()
min_throughput=sumtool/sumtime
print("throughput is:", min_throughput)
print("tedad bastehaye daryafti:", counter)
