#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.
"""API Utilities"""


def ascii_art(version):
    """
    Used to build SolidFire ASCII art.
    :return: a string with the SolidFire ASCII art.
    """
    art = "\n"
    art += "                                             \n"
    art += "                ______________            ___\n"
    art += "               /__/__\__\__\__\       ___/__/\n"
    art += "              /_ /__/_\__\__\__\  ___/__/__/ \n"
    art += "             /__/__/__/\__\__\__\/__/__/__/  \n"
    art += "            /__/__/__/  \__\__\__\_/__/__/   \n"
    art += "           /__/__/       \__\__\__\__/__/    \n"
    art += "          /__/            \__\__\__\/__/     \n"
    art += "                                             \n"
    art += "             NetApp SolidFire Version {0}    \n".format(version)
    art += "                                             \n"
    return art
