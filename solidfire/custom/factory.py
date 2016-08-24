import re
from solidfire import Element
from solidfire.common import SdkOperationError, ApiVersionUnsupportedError
import logging

minimum_version = 7.0
maximum_version = 8.4


class Factory:
    """
    The Factory for creating a SolidFire Element object.
    """

    @staticmethod
    def create(target, username, password, version=None,
               verify_ssl=False, port=443):

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
            doesn't match the cluster or is outside the versions supported by this
            SDK, you will get an exception.
        :type version: float or str
        :param verify_ssl: enable this to check ssl connection for errors
            especially when using a hostname. It is invalid to set this to
            true when using an IP address in the target.
        :type verify_ssl: bool
        :param port: a port to connect to if other than 443, which is the
            default for a SolidFire cluster. Specify 442 if connecting to
            a SoldiFire node.
        :type port: int
        :return: a configured and tested instance of Element
        :raises:
            SdkOperationError: verify_ssl is true but target is an IP address
            SdkOperationError: version is unable to be determined as float
            ApiVersionUnsupportedError: version is not supported by
                instance of Element OS.
        """

        target_is_ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", target)

        if target_is_ip is not None and verify_ssl == True:
            raise SdkOperationError("Cannot verify SSL when target is an IP "
                                    "address. Set verify_ssl to false or use a "
                                    "fully qualified domain name.")

        if port != 443:
            target = target + ":" + str(port)

        element = Element(target, username, password, minimum_version,
                          verify_ssl)

        api = element.get_api()

        min_supported_version = float(min(api.supported_versions))
        max_supported_version = float(max(api.supported_versions))

        if version is None:
            # cluster's version is greater than max supported version
            if float(api.current_version) > maximum_version:
                element = Element(target, username, password, maximum_version,
                                  verify_ssl)
            else:
                element = Element(target, username, password,
                                  api.current_version, verify_ssl)
        else:
            try:
                versionActual = float(version)
            except:
                raise SdkOperationError("Unable to determine version to "
                                        "connect from value: " + version)

            if versionActual < min_supported_version or \
                            versionActual > max_supported_version:
                raise SdkOperationError(
                    "Invalid version to connect to on cluster. Valid version are between {0} and {1}"
                        .format(min_supported_version, max_supported_version))
            else:
                element = Element(target, username, password, versionActual,
                                  verify_ssl)

        logging.info(Factory.asciiArt())
        return element

    @staticmethod
    def asciiArt():
        """
        Used to build SolidFire ASCII art.
        :return: a string with the SolidFire ASCII art.
        """
        art = "\n"
        art += "                ______________            ___\n"
        art += "               /__/__\__\__\__\       ___/__/\n"
        art += "              /_ /__/_\__\__\__\  ___/__/__/ \n"
        art += "             /__/__/__/\__\__\__\/__/__/__/  \n"
        art += "            /__/__/__/  \__\__\__\_/__/__/   \n"
        art += "           /__/__/       \__\__\__\__/__/    \n"
        art += "          /__/            \__\__\__\/__/     \n"
        art += "\n"
        art += "                  NetApp SolidFire\n"
        return art
