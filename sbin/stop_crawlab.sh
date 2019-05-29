#!/bin/sh
# __author__ = 'lish'

source ~/.bash_profile
source /etc/profile


pid0=`ps -ef|grep "/data/server/crawlab"|grep -v grep|awk '{print $2}'`
if [  -n "$pid0" ];then
    kill -9 `ps -ef|grep "/data/server/crawlab"|grep -v grep|awk '{print $2}'`
fi

pid1=`ps -ef|grep "/usr/local/bin/celery flower"|grep -v grep|awk '{print $2}'`
if [  -n "$pid1" ];then
    kill -9 `ps -ef|grep "/usr/local/bin/celery flower"|grep -v grep|awk '{print $2}'`
fi