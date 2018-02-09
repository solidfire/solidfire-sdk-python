from solidfire.factory import ElementFactory
from solidfire.custom.models import CHAPSecret

import logging
from solidfire import common
common.setLogLevel(logging.DEBUG)

print("This test script assumes no accounts named below exist.")
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

e.add_account(username1,initiatorSecret)
e.add_account(username2,chap2)
e.add_account(username3,chap3)
e.add_account(username4,chap4)

a1 = e.get_account_by_name("username1")
a2 = e.get_account_by_name("username2")
a3 = e.get_account_by_name("username3")
a4 = e.get_account_by_name("username4")

is1 = a1.account.initiator_secret.secret
is2 = a2.account.initiator_secret.secret
is3 = a3.account.initiator_secret.secret
is4 = a4.account.initiator_secret.secret

#print(is1)
#print(is2)
#print(is3)
#print(is4)

if (is1 == is2 and is2 == is3 and is3 == is4):
    print("All secrets are the same.")
    print("Tests succeeded")

e.remove_account(a1.account.account_id)
e.remove_account(a2.account.account_id)
e.remove_account(a3.account.account_id)
e.remove_account(a4.account.account_id)
