import sys
import requests
import json
import mysql.connector
from mysql.connector import (connection)
from sys import argv
import csv

script = sys.argv[0]
ucpe = sys.argv[1].upper()
print "UCPE: " + ucpe

flag = False
##eipam_keys = [ ]

db = mysql.connector.connect(user='sdnctlro', password='RUok2day?', host='iracavcsddb01-eth2.infra.aic.att.net',
                             database='sdnctl')
c = db.cursor()

u = ucpe[:16]

u = u + '%'

select = "select client_key,ip_address from sdnctl.EIPAM_IP_ASSIGNMENTS where client_key like \'%s\'" % u

##print select
c.execute(select)

for row in c:
    ##print row
    if row is not None:
        s = ','.join(row)
        print s
        flag = True

if not flag:
    print "No data found"

c.close()
db.close()





