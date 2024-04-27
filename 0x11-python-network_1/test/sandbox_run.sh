#!/bin/bash

cd /etc/init.d/ ;

update-rc.d web defaults;

service web start;

rm -rf /root/.bash_history;

while true
do
  /usr/sbin/sshd -D
done
