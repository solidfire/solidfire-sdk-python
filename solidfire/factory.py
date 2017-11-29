#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# CONFIDENTIALITY NOTICE: THIS SOFTWARE CONTAINS CONFIDENTIAL INFORMATION OF
# NETAPP, INC. USE, DISCLOSURE OR REPRODUCTION IS PROHIBITED WITHOUT THE PRIOR
# EXPRESS WRITTEN PERMISSION OF NETAPP, INC.
import re

from solidfire import Element
from solidfire.common import SdkOperationError
from solidfire.util import ascii_art
import logging

LOG = logging.getLogger('solidfire.Element')

min_sdk_version = 7.0

class ElementFactory:
    """
    The Factory for creating a SolidFire Element object.
    """

    @staticmethod
    def create(target, username, password, version=None,
               verify_ssl=False, port=443, print_ascii_art=True, timeout=30):
        """
        Factory method to create a Element object which is used to call
         the SolidFire API. This method runs multiple checks and logic
         to ensure the Element object creation is valid for the cluster
         you are attempting to connect to. It is preferred to use this
         factory method over the standard constructor.

        :param target: the target IP or hostname of the cluster or node.
        :type target: str
        :param username: username used to connect to the Element OS instance.
        :type username: str
        :param password: authentication for username
        :type password: str
        :param version: specific version of Element OS to connect to. If this
            doesn't match the cluster or is outside the versions supported by
            this SDK, you will get an exception.
        :type version: float or str
        :param verify_ssl: enable this to check ssl connection for errors
            especially when using a hostname. It is invalid to set this to
            true when using an IP address in the target.
        :type verify_ssl: bool
        :param port: a port to connect to if other than 443, which is the
            default for a SolidFire cluster. Specify 442 if connecting to
            a SoldiFire node.
        :type port: int
        :param print_ascii_art: When True, print the SolidFire Robot to the
            log.  Production deployments might consider disabling this feature.
        :type print_ascii_art: bool
        :param timeout: The number of seconds to wait before timing out a request.
        :type timeout: int
        :return: a configured and tested instance of Element
        :raises:
            SdkOperationError: verify_ssl is true but target is an IP address
            SdkOperationError: version is unable to be determined as float
            ApiVersionUnsupportedError: version is not supported by
                instance of Element OS.
        """

        target_is_ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
                                target)

        if target_is_ip is not None and verify_ssl:
            raise SdkOperationError("Cannot verify SSL when target is an IP "
                                    "address. Set verify_ssl to false or use "
                                    "a fully qualified domain name.")

        if port is None:
            port = 443

        if verify_ssl is None:
            verify_ssl = False

        if port != 443:
            target = target + ":" + str(port)

        element = Element(target, username, password, min_sdk_version,
                          verify_ssl)
        element.timeout(timeout)

        api = element.get_api()

        if version is None:
            element = Element(target, username, password,
                              api.current_version, verify_ssl)
            element.timeout(timeout)
        else:
            try:
                version_actual = float(version)
            except:
                raise SdkOperationError("Unable to determine version to "
                                        "connect from value: " + version)

            if version_actual < min_sdk_version:
                raise SdkOperationError("Cannot connect to a version lower "
                                        "than supported by the SDK. "
                                        "Connect at {0} or higher."
                                        .format(min_sdk_version))

            supported_versions = []
            version_is_unsupported = True
            for api_version in api.supported_versions:
                if float(api_version) >= min_sdk_version:
                    supported_versions.append(api_version)
                    if version_actual == float(api_version):
                        version_is_unsupported = False

            if version_is_unsupported:
                raise SdkOperationError(
                    "Invalid version to connect on this cluster. "
                    "Valid versions are: {0}"
                    .format(", ".join(supported_versions)))
            else:
                element = Element(target, username, password, version_actual,
                                  verify_ssl)
                element.timeout(timeout)

        LOG.info("Connected to {0} using API version {1}"
                 .format(target, element.api_version))

        if print_ascii_art:
            LOG.info(ascii_art(element.api_version))
        return element
