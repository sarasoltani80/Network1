
import pyshark
import os

f=open("fi.pcap","w")
capture = pyshark.LiveCapture(interface = 'lo',bpf_filter='port 4040',output_file="fi.pcap")
capture.sniff(timeout = 15)
tcpbazersal=0
f.close()
capture.close()

secondcapture = pyshark.FileCapture(r'fi.pcap', display_filter='tcp.analysis.retransmission')
for i in range(len(secondcapture)):
    tcpbazersal += 1

secondcapture.close()
print("number of retransmission:", tcpbazersal)

os._exit(1)
    
    