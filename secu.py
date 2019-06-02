#!/usr/bin/python2

import os, sys

print ("\033[1;33mTeam = 2e4h~GblkCrew~BogorBlackHat")
print ("\033[1;33mMasukan Pw + Username = done")
print ("\033[1;33mHubungi XerXez7 62886686741 \033[1;31;1m")
username = 'xerxez7'
password = 'gans2x'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mWOKE WELCOM TO MY TOOLS", 
			sys.exit()

		else:

			print "\n\033[1;36mKALO GA TAU GA USAH MAKSA ASU!!!\033[00m"
			print "LOIN KEMBALI \n"
			restart()

	else:
		print "\n\033[1;36mUSERNAME BUKAN ITU ASW !!!\033[00m"
		print "LOGIN BALIK AH\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
