import os
def print_dir(files):
    for file in files:
        objects = os.path.join(files,file)
        if os.path.isdir(objects):
            print_dir (objects)

        else:
            print objects


print_dir('/Users/mohanpraveenhazaru/Documents/audit_log')


A0 = {'a':1,'b':2,'c':3,'d':4,'e':5}
A1 = range(10)
A2 = sorted([i for i in range(10) if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]

print A2
print A3
print A4
print A5
print A6


def f(x,l=[]):z
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)

import requests
resp = requests.get('https://todolist.com/mayam/')
if resp.status_code!=200:
    raise ('GET/mayam/ {}'.format(resp.status_code))
for item in resp.json():
    print '{} {} '.format(item['id'],item['summary'])


class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# specify output from here onwards

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()