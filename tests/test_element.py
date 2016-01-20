#!/usr/bin/env python3

from solidfire.element import api

mvip = '192.168.133.64'
username = 'admin'
password = 'admin'
apiver = '8.0'

server = api.SolidFireElement.create(mvip, username, password, apiver, False)

print(server.list_services())
