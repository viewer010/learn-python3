#!/usr/bin/env python3
#coding=utf8

import os

print("Process (%s) start..."% os.getpid())
#only work on Unix/Linux/Mac
pid = os.fork()
if pid == 0:
    print('I am a child process (%s) and my parent is %s.'%(os.getpid(),os.getppid()))
else:
    print("I (%s) just created a child process (%s)."%(os.getpid(),pid))