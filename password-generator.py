#!/usr/local/bin/python3

import string, random

p1 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])
p2 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])
p3 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])
p4 = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])

print(p1 + "-" + p2 + "-" + p3 + "-" + p4)