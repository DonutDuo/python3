#!/usr/local/bin/python3

import string, random, os
# p1-p4 create 4 digit random string with letters and number
p1 = ''.join([random.choice(string.ascii_letters + string.digits + string.digits) for n in range(4)])
p2 = ''.join([random.choice(string.ascii_letters + string.digits + string.digits) for n in range(4)])
p3 = ''.join([random.choice(string.ascii_letters + string.digits + string.digits) for n in range(4)])
p4 = ''.join([random.choice(string.ascii_letters + string.digits + string.digits) for n in range(4)])
# create passwd in format order
passwd = p1 + "-" + p2 + "-" + p3 + "-" + p4
# copy generated password to clipboard
os.system("echo '%s' | pbcopy" % passwd)