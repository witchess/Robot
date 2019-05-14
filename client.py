#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Time: 2019/05/14
#@Author: witchess
#@File: client.py
#@Contact: 1822980791@qq.com

import os
import sys
import re
import time
import tkinter as tk

from socket import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


def do_login():
	pass


def do_register():
	pass


def check_register():
	pass


def do_menu1():
	pass


def do_menu2():
	pass


def main():
    if len(sys.argv) == 3:	
	    HOST = sys.argv[1]
 	    PORT = int(sys.argv[2])
 	    ADDR = (HOST,PORT)
 	else:
 		print('argv erro')
 		sys.exit(1)

 	s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.connect(ADDR)


  if __name__ == '__main__':
  	main()