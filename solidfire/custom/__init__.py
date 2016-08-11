from __future__ import unicode_literals
from __future__ import absolute_import
from solidfire.common import model as data_model

auto_generate_secret = "AUTO-GENERATE-CHAP-SECRET"


class CHAPSecret(data_model.DataObject):
    """
    A representation of the CHAP Secret

    :param secret: [required] A 12 - 16 character string.
    :type start: str

    """

    secret = data_model.property(
        "secret", str,
        array=False, optional=False,
        documentation="A 12 - 16 character string."
    )

    def auto_generate(self):
        """
        Used in 'AddAccount' and 'ModifyAccount' to cause a CHAP Secret to be
        auto generated by the cluster.
        """
        self.secret = auto_generate_secret
        return self

    def __init__(self, **kwargs):
        data_model.DataObject.__init__(self, **kwargs)

    @classmethod
    def custom_extract(cls, data):
        """
        Deserialize the property from json.

        :param data: the data to be converted.

        :return: the extracted data.
        """
        chap = CHAPSecret()
        chap.secret = data
        return chap

    def custom_to_json(self):
        """
        Custom json serialize logic
        :return:
        """
        if self.secret == auto_generate_secret:
            return None
        else:
            return self.secret