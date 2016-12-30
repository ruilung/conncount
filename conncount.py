import psutil
import operator
conn=psutil.net_connections()
# get connection info from psutil

dictconn={}

for i in conn:
    if i.raddr:
        remoteAddress=i.raddr[0]
        if dictconn.has_key(remoteAddress):
            dictconn[remoteAddress]=dictconn[remoteAddress]+1
            # count  +1 if  dict already had this ip
        else:
            dictconn[remoteAddress]=1
            # add ip as new key, also count it from 1

sorted_conn = sorted(dictconn.items(), key=operator.itemgetter(1), reverse=True)

icount=1
for i in sorted_conn:
    print "%2d %-15s %s" %(icount,i[0],i[1])
    icount+=1
    if (icount>10):
        break
        # list top 10 remote address, sorted by connections.


