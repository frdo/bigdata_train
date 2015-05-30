# -*- coding: utf-8 -*-

# Tutorial from:
# [COVERED] http://blog.cloudera.com/blog/2013/03/how-to-use-the-apache-hbase-rest-interface-part-1/
# [       ] http://blog.cloudera.com/blog/2013/04/how-to-use-the-apache-hbase-rest-interface-part-2/
# [       ] http://blog.cloudera.com/blog/2013/07/how-to-use-the-apache-hbase-rest-interface-part-3/

############################################################
# Using the REST interface, you can create or delete tables#
#                                                          #
# requierements:                                           #
#     'requests' package                                   #
#      http://docs.python-requests.org/en/latest/          #
#           - easy_install requests                        #
#                   or                                     #
#           - pip install requests                         #
############################################################

import requests

baseurl = "http://localhost:8070"

# Method for encoding ints with base64 encoding
def encode(n):
     data = struct.pack("i", n)
     s = base64.b64encode(data)
     return s

# Method for decoding ints with base64 encoding
def decode(s):
     data = base64.b64decode(s)
     n = struct.unpack("i", data)
     return n[0]

# Checks the request object to see if the call was successful
def issuccessful(request):
    #if 200
    pass

def createTable(tablename, *cfname):
    # Let’s take a look at the code to create a table
    content =  '<?xml version="1.0" encoding="UTF-8"?>'
    content += '<TableSchema name="' + tablename + '">'
    
    for cf in cfname:
        content += '  <ColumnSchema name="' + cf + '" />'
    
    content += '</TableSchema>'

    request = requests.post(baseurl + "/" + tablename + "/schema", data=content, headers={"Content-Type" : "text/xml", "Accept" : "text/xml"})
    return request

def getTable(tablename):
    # We can easily check if a table exists using the following code
    content =  '<?xml version="1.0" encoding="UTF-8"?>'
    content += '<TableSchema name="' + tablename + '">'
    content += '</TableSchema>'

    request = requests.get(baseurl + "/" + tablename + "/schema")
    return request

def deleteTable(tablename):
    # We can delete a table using the following code
    content =  '<?xml version="1.0" encoding="UTF-8"?>'
    content += '<TableSchema name="' + tablename + '">'
    content += '</TableSchema>'

    request = requests.delete(baseurl + "/" + tablename + "/schema")
    return request

def main():
   tablename = 'emp'
   cfname = 'Sepal'

   #createTable(tablename, cfname)
   #getTable(tablename)
