import psutil
import operator
import datetime

def printTop(dictData,recordToPrint,totalConnection):
    #dictData get connection info from dictConn,dictStatus and so on
    #recordToprint decide how many record will be print
    #totalConnection get remoteAddressSum to calc perentage
    listSorted=sorted(dictData.items(), key=operator.itemgetter(1), reverse=True)
    icount = 1
    rcount = 0.0
    for i in listSorted:
        print "%2d %-15s %s" % (icount, i[0], i[1])
        icount += 1
        rcount += i[1]
        if (icount > recordToPrint):
            break
            # list top 10 remote address, sorted by connections.

    print "top %d %3.2f%%, others %3.2f%%" % (recordToPrint, rcount / totalConnection * 100, (totalConnection - rcount) / totalConnection * 100)
    print ""

#  program start at here
print ""
print "conncount ver 0.1"
print "execute time:",datetime.datetime.now()

conn=psutil.net_connections()
# get connection info from psutil
print "total connections:", len(conn)
print ""


dictConnRaddr={}
dictStatus={}
dictLocalPort={}

remoteAddressSum=0
for i in conn:
    if i.raddr:
        remoteAddress=i.raddr[0]
        connStatus=i.status
        localPort=i.laddr[1]
        remoteAddressSum += 1
        if dictConnRaddr.has_key(remoteAddress):
            dictConnRaddr[remoteAddress]=dictConnRaddr[remoteAddress]+1
            # count  +1 if  dict already had this ip
        else:
            dictConnRaddr[remoteAddress]=1
            # add ip as new key, also count it from 1
        if dictStatus.has_key(connStatus):
            dictStatus[connStatus]=dictStatus[connStatus]+1
            # count  +1 if  dict already had this status
        else:
            dictStatus[connStatus]=1
            # add status as new key, also count it from 1
        if dictLocalPort.has_key(localPort):
            dictLocalPort[localPort]=dictLocalPort[localPort]+1
            # count  +1 if  dict already had this localPort
        else:
            dictLocalPort[localPort]=1
            # add localPort as new key, also count it from 1


print "top 10, remote address"
printTop(dictConnRaddr,10,remoteAddressSum)

print "top 10,connection status"
printTop(dictStatus,10,remoteAddressSum)

print "top 10,local port"
printTop(dictLocalPort,10,remoteAddressSum)
