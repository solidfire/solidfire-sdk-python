#!/usr/bin/env python

from solidfire.element.api.SolidFireElement import SolidFireElement

mvip = '172.26.64.39'
username = 'admin'
password = 'admin'
apiver = '8.0'

server = SolidFireElement(mvip, username, password, apiver, False)
