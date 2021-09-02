# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/27 19:47
# @Author    :   Chasion
# Description:

a = [x for x in range(4, 82)]
b = [x for x in range(84, 162)]
for i in range(len(a)):
    print('set tcp [new Agent/TCP]' + '\n' + '$tcp set class_2' + '\n' + '$ns attach-agent $n{} $tcp'.format(a[i]) + '\n' + 'set sink [new Agent/TCPSink]' + '\n' + '$ns attach-agent $n{} $sink'.format(b[i]) + '\n' + '$ns connect $tcp $sink' + '\n' + '$tcp set fid_ 1' + '\n')

