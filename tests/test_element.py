#!/usr/bin/env python

from solidfire import Element

mvip = '172.26.64.39'
username = 'admin'
password = 'admin'
apiver = '8.0'

server = Element(mvip, username, password, apiver, False)
