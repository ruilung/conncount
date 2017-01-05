# conncount
collect network connections. count by remote address/ status/ localport. list top 10 of it. display percentage of top10.

# sample
conncount ver 0.1
execute time: 2017-01-05 10:29:38.200000
total connections: 438

top 10, remote address
 1 192.168.20.85    264
 2 127.0.0.1       8
 3 192.168.5.70      3
 4 192.168.5.186     3
 5 117.18.232.200  3
 6 192.168.3.34     2
 7 192.168.1.42      2
 8 104.196.229.58  2
 9 192.168.0.127    2
10 192.168.3.51     2
top 10 82.20%, others 17.80%

top 10,connection status
 1 TIME_WAIT       265
 2 ESTABLISHED     83
 3 CLOSE_WAIT      6
top 10 100.00%, others 0.00%

top 10,local port
 1 49161           1
 2 55329           1
 3 55330           1
 4 55331           1
 5 55332           1
 6 59517           1
 7 52597           1
 8 51403           1
 9 49364           1
10 49365           1
top 10 2.82%, others 97.18%
