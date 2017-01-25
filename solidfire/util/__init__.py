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
    art += "\n"
    art += "                                               77               \n"
    art += "                                              7777              \n"
    art += "                                               77               \n"
    art += "                                               ==               \n"
    art += "                             77IIIIIIIIIIIIIIIIII777            \n"
    art += "                           =7                       7=          \n"
    art += "                           7                         7          \n"
    art += "                          =7                         7=         \n"
    art += "                          =7                         7=         \n"
    art += "                         =77   7777777777777777777   77=        \n"
    art += "                        7777  777777777777777777777  7777       \n"
    art += "                        7777   7777777777777777777   7777       \n"
    art += "                         =77                         77=        \n"
    art += "                          =7                         7=         \n"
    art += "                           7                         7          \n"
    art += "                           7=                       =7          \n"
    art += "                            77=                   =77           \n"
    art += "                              =7777777777777777777=             \n"
    art += "                                                                \n"
    art += "                               ====IIIIIIIIII=====              \n"
    art += "                         =77777=                 =77777=        \n"
    art += "                     =777=                             =777=    \n"
    art += "                 =777=                                     =777=\n"
    art += "                                                                \n"
    art += "                           NetApp SolidFire Version {0}    " \
           "\n".format(version)
    art += "                                             \n"
    return art
