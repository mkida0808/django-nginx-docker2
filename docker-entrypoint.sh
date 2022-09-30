#!/bin/sh
#CPU / コア数を取得する
CPU=`grep physical.id /proc/cpuinfo | sort -u | wc -l`
CORE=`grep cpu.cores /proc/cpuinfo | sort -u | wc -l`

#uwsgiのプロセス数、スレッド数を設定(要パラメータチューニング)
export UWSGI_THREADS=`expr ${CPU}`
export UWSGI_PROCESSES=`expr ${CORE}`

/usr/local/bin/uwsgi --ini /home/docker/code/uwsgi.ini