# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (C) 2024 Elijah Goossen, ekgoossen@gmail.com

class Budget():
    def __init__(self):
        self.__accounts = list()

    def add_account(self,name):
        self.__accounts.append(name)

    def get_accounts(self):
        return self.__accounts
