#!/usr/local/bin/python3

import string, random, os
rno = [4,5,6]
# p1-p4 create 4 digit random string with letters and number
rnum = (random.choice(rno))
p1 = ''.join([random.choice(string.ascii_letters + string.digits + string.digits) for n in range(rnum)])
rnum = (random.choice(rno))
p2 = ''.join([random.choice(string.ascii_letters + string.digits + string.digits) for n in range(rnum)])
rnum = (random.choice(rno))
p3 = ''.join([random.choice(string.ascii_letters + string.digits + string.digits) for n in range(rnum)])
# create passwd in format order
passwd = p1 + "-" + p2 + "-" + p3
# copy generated password to clipboard
os.system("echo '%s' | pbcopy" % passwd)