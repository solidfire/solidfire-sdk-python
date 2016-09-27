---
title: Solidfire Python SDK
layout: index
---
These examples walk through all interactions with an Account on the SolidFire cluster.

Examples for:

-   [List all Accounts](#list-all-accounts)
-   [Get one Account](#get-one-account)
-   [Create an Account](#create-an-account)
-   [Modify an Account](#modify-an-account)

Documentation
=============

Further documentation for each method and type can be found in our PyPI documentation repository.

List all Accounts
=================

To list all accounts on a cluster:

``` sourceCode
from solidfire.factory import ElementFactory

# Create connection to SF Cluster
sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

# Send the request and gather the result
list_accounts_result = sfe.list_accounts()

# iterate the accounts array on the result object and display each Account
for account in list_accounts_result.accounts:
    print(account)
```

Get one Account
===============

To get a single account by ID:

``` sourceCode
from solidfire.factory import ElementFactory

# Create connection to SF Cluster
sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

# Send the request with a specific account id and gather the result
get_account_result = sfe.get_account_by_id(1)

# Display the account from the result object
print(get_account_result.account)
```

To get a single account by username:

``` sourceCode
from solidfire.factory import ElementFactory

# Create connection to SF Cluster
sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

# Send the request with a specific account username and gather the result
get_account_result = sfe.get_account_by_name('username-of-account')

# Display the account from the result object
print(get_account_result.account)
```

Create an Account
=================

To create an account you must specify the `username`. Optionally, you can also specify the `initiator_secret` and `target_secret` which are **CHAPSecret** objects. If those secrets are not specified, they will be auto-generated.

F.html, we create an account with only a username:

``` sourceCode
from solidfire.factory import ElementFactory

# Create connection to SF Cluster
sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

# Send the request and gather the result
add_account_result = sfe.add_account(username="my-new-account")

# Grab the account ID from the result object
new_account_id = add_account_result.account_id
```

Now we create an account and specify the `username` and `initiator_secret`. Notice we created a new **CHAPSecret** object and set the string value for the `intitiator_secret`. The `target_secret` will be auto-generated during the process on the cluster:

``` sourceCode
from solidfire.factory import ElementFactory

# Create connection to SF Cluster
sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

# Send the request and gather the result
add_account_result = sfe.add_account(username="my-new-account", 
                                     initiator_secret=CHAPSecret(
                                         "a12To16CharValue"))

# Grab the account ID from the result object
new_account_id = add_account_result.account_id
```

Modify an Account
=================

To modify an account, all you need is the `account_id` and the values you want to change. Any values you leave off will remain as they were before this call is made.

In this example, we will instruct the API to autogenerate a new `target_secret` value for an account. In order to do so we need to call the static `auto_generate()` method on the **CHAPSecret** class.

``` sourceCode
from solidfire.factory import ElementFactory

# Create connection to SF Cluster
sfe = ElementFactory.create("ip-address-of-cluster", "username", "password")

# Send the request with the account_id and gather the result
add_account_result = sfe.modify_account(account_id=1,
                                        target_secret=CHAPSecret.auto_generate())
```
