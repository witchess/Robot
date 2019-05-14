#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Time: 2019/05/14
#@Author: witchess
#@File: server.py
#@Contact: 1822980791@qq.com

import os
import sys

from socket import *


#定义服务器类
class Server(object):
	def __init__(self):
		self.__sockfd = socket()
		self.__sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

	def bind(self,addr):
		self.__sockfd.bind(addr)

	def start(self):
		self.__sockfd.listen(10)
		while True:
			try:
				c, addr = self.__sockfd.accept()
			except KeyboardInterrupt:
				os.__exit(0)
			except Exception:
				continue
			pid = os.fork()
			if pid < 0:
				print("创建进程失败")
				c.close()
			elif pid == 0:
				self.__sockfd.close()
				print(addr,"已经连接")
				self.do_client(c)

	def do_client(self,c):
		while True:
			recv_data = b''
			while True:
				data = c.recv(1024)
				if len(data) < 1024:
					recv_data += data
					break
				elif not data:
					break
				else:
					recv_data += data
			recv_data = recv_data.decode()
			print(recv_data)
			
	def do_register(self):
		pass

	def do_login(self):
		pass

	def do_find(self):
		pass

	def do_history(self):
		pass


def main():
	if len(sys.argv) < 3:
		print("""
			argv is error
			input python3 server.py localhost xxxx
			""")
		HOST = sys.argv[1]
		PORT = int(sys.argv[2])
		ADDR = (HOST,PORT)
		rebot_server = Server()
		rebot_server.bond(ADDR)
		rebot_server.start()


if __name__ == "__main__":
	main()