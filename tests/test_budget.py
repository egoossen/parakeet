# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (C) 2024 Elijah Goossen, ekgoossen@gmail.com

import pytest

from parakeet.budget import Budget

def test_create_budget():
    budget = Budget()

@pytest.mark.parametrize('account_list,num_accounts',[
    (['Income'], 1)
])
def test_add_account(account_list, num_accounts):
    budget = Budget()
    for account in account_list:
        budget.add_account(account)
    assert len(budget.get_accounts()) == num_accounts
