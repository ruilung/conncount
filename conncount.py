import psutil
import operator
conn=psutil.net_connections()
# get connection info from psutil

dictConn={}
dictStatus={}

for i in conn:
    if i.raddr:
        remoteAddress=i.raddr[0]
        connStatus=i.status
        if dictConn.has_key(remoteAddress):
            dictConn[remoteAddress]=dictConn[remoteAddress]+1
            # count  +1 if  dict already had this ip
        else:
            dictConn[remoteAddress]=1
            # add ip as new key, also count it from 1
        if dictStatus.has_key(connStatus):
            dictStatus[connStatus]=dictStatus[connStatus]+1
            # count  +1 if  dict already had this status
        else:
            dictStatus[connStatus]=1
            # add status as new key, also count it from 1


sorted_conn = sorted(dictConn.items(), key=operator.itemgetter(1), reverse=True)
sorted_status = sorted(dictStatus.items(), key=operator.itemgetter(1), reverse=True)

icount=1
for i in sorted_conn:
    print "%2d %-15s %s" %(icount,i[0],i[1])
    icount+=1
    if (icount>10):
        break
        # list top 10 remote address, sorted by connections.

print ""

icount=1
for i in sorted_status:
    print "%2d %-15s %s" %(icount,i[0],i[1])
    icount+=1
    if (icount>10):
        break
        # list top 10 status, sorted by status
