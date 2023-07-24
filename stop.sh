#/bin/bash
RUN_PORT2=`netstat -tunlp|grep 9000|awk '{print $7}'|awk -F'/' '{print $1}'`
kill -9 $RUN_PORT2
