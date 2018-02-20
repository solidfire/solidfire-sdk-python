from solidfire.factory import ElementFactory
from solidfire.custom.models import CHAPSecret
from tests.base_test import SolidFireBaseTest

import logging
from solidfire import common
common.setLogLevel(logging.DEBUG)

class TestChapCreation(SolidFireBaseTest):
    def test_should_all_have_same_init_secret(self):
        #This test script assumes no accounts named below exist
        e = ElementFactory.create("10.117.61.129", "admin", "admin") #hardcoded clusterIP, currently targetting a 10.3 cluster

        username1 = "username1"
        username2 = "username2"
        username3 = "username3"
        username4 = "username4"
        initiatorSecret = "abcde1245678"

        chap2 = CHAPSecret(initiatorSecret)
        chap3 = CHAPSecret(secret=initiatorSecret)
        kwarg = {"secret":initiatorSecret}
        chap4 = CHAPSecret(**kwarg)

        e.add_account(username1,initiator_secret=initiatorSecret)
        e.add_account(username2,initiator_secret=chap2)
        e.add_account(username3,initiator_secret=chap3)
        e.add_account(username4,initiator_secret=chap4)

        a1 = e.get_account_by_name("username1")
        a2 = e.get_account_by_name("username2")
        a3 = e.get_account_by_name("username3")
        a4 = e.get_account_by_name("username4")

        is1 = a1.account.initiator_secret.secret
        is2 = a2.account.initiator_secret.secret
        is3 = a3.account.initiator_secret.secret
        is4 = a4.account.initiator_secret.secret

        self.assertEquals(is1,is2)
        self.assertEquals(is2,is3)
        self.assertEquals(is3,is4)

        #cleanup
        e.remove_account(a1.account.account_id)
        e.remove_account(a2.account.account_id)
        e.remove_account(a3.account.account_id)
        e.remove_account(a4.account.account_id)

    def test_should_all_have_same_target_secret(self):
        # This test script assumes no accounts named below exist
        e = ElementFactory.create("10.117.61.129", "admin",
                                  "admin")  # hardcoded clusterIP, currently targetting a 10.3 cluster

        username1 = "username1"
        username2 = "username2"
        username3 = "username3"
        username4 = "username4"
        targetSecret = "abcde1245678"

        chap2 = CHAPSecret(targetSecret)
        chap3 = CHAPSecret(secret=targetSecret)
        kwarg = {"secret": targetSecret}
        chap4 = CHAPSecret(**kwarg)

        e.add_account(username1, target_secret= targetSecret)
        e.add_account(username2, target_secret= chap2)
        e.add_account(username3, target_secret= chap3)
        e.add_account(username4, target_secret= chap4)

        a1 = e.get_account_by_name("username1")
        a2 = e.get_account_by_name("username2")
        a3 = e.get_account_by_name("username3")
        a4 = e.get_account_by_name("username4")

        ts1 = a1.account.target_secret.secret
        ts2 = a2.account.target_secret.secret
        ts3 = a3.account.target_secret.secret
        ts4 = a4.account.target_secret.secret

        self.assertEquals(ts1, ts2)
        self.assertEquals(ts2, ts3)
        self.assertEquals(ts3, ts4)

        # cleanup
        e.remove_account(a1.account.account_id)
        e.remove_account(a2.account.account_id)
        e.remove_account(a3.account.account_id)
        e.remove_account(a4.account.account_id)

