ss -an > /tmp/conncount.log
echo ""
echo "conncount script ver 0.1"
echo "execute time: $(date)"

totalconn=$(cat /tmp/conncount.log | wc -l)

# header is not connection
totalconn=$((totalconn-1))


# echo top10 by remote address
echo "total connections: $totalconn"

cat /tmp/conncount.log  | awk '{print $5}' | grep -o -E '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}' | sort | uniq -c | sort -rn | head -n 10 | nl
cat /tmp/conncount.log  | awk '{print $5}' | grep -o -E '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}' | sort | uniq -c | sort -rn | head -n 10 | nl > /tmp/conncount.log.tmp

remoteAddrTop10=$(cat /tmp/conncount.log.tmp | awk ' {sum+=$2} END{print sum}')

percentage1=$(awk -v r=$remoteAddrTop10 -v t=$totalconn 'BEGIN { printf "%3.2f%%",r/t*100 }')
percentage2=$(awk -v r=$remoteAddrTop10 -v t=$totalconn 'BEGIN { printf "%3.2f%%",(t-r)/t*100 }')

printf "top 10 %s, others %s\n\n" $percentage1 $percentage2

# echo top 10 by status
echo "top 10,connection status"

cat /tmp/conncount.log | grep -v State | awk '{print $1}' | sort | uniq -c | sort -rn | head -n 10  | nl
cat /tmp/conncount.log | grep -v State | awk '{print $1}' | sort | uniq -c | sort -rn | head -n 10  | nl > /tmp/conncount.log.tmp

statusTop10=$(cat /tmp/conncount.log.tmp | awk ' {sum+=$2} END{print sum}')

percentage1=$(awk -v s=$statusTop10 -v t=$totalconn 'BEGIN { printf "%3.2f%%",s/t*100 }')
percentage2=$(awk -v s=$statusTop10 -v t=$totalconn 'BEGIN { printf "%3.2f%%",(t-s)/t*100 }')

printf "top 10 %s, others %s\n\n" $percentage1 $percentage2

#echo top10 by local port (listen port)
echo "top 10,local port"

cat /tmp/conncount.log | awk '{print $4}' | sed 's/::ffff://g' | awk -F : '{print $2}' | sort | uniq -c | sort -rn | head -n 10 | nl
cat /tmp/conncount.log | awk '{print $4}' | sed 's/::ffff://g' | awk -F : '{print $2}' | sort | uniq -c | sort -rn | head -n 10 | nl > /tmp/conncount.log.tmp

localPortTop10=$(cat /tmp/conncount.log.tmp | awk ' {sum+=$2} END{print sum}')

percentage1=$(awk -v l=$localPortTop10 -v t=$totalconn 'BEGIN { printf "%3.2f%%",l/t*100 }')
percentage2=$(awk -v l=$localPortTop10 -v t=$totalconn 'BEGIN { printf "%3.2f%%",(t-l)/t*100 }')

printf "top 10 %s, others %s\n\n" $percentage1 $percentage2
