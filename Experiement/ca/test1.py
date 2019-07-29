#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from subprocess import *

pid = Popen(["/Users/thiquynhnhunguyen/Desktop/STAR 2019/ca/ca.macos", "basic.cfg"],
            stdin=PIPE,
            stdout=PIPE)

for i in xrange(10):
    for j in xrange(10):
        x = pid.stdout.readline()
        pid.stdin.write('1/1\n')
        x = pid.stdout.readline()
        pid.stdin.write("4/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("2/1\n")
        x = pid.stdout.readline()
        pid.stdin.write("0/1\n")
        x = pid.stdout.readline()
pid.stdin.close()