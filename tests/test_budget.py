# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (C) 2024 Elijah Goossen, ekgoossen@gmail.com

import pytest

from parakeet.budget import Budget

@pytest.fixture
def budget():
    return Budget()

def test_create_budget(budget):
    assert type(budget) == Budget

def test_add_account(budget):
    budget.add_account('Expense')
    assert len(budget.get_accounts()) == 1

def test_add_multiple_accounts(budget):
    budget.add_account('Expense 1')
    budget.add_account('Expense 2')
    budget.add_account('Expense 3')
    assert len(budget.get_accounts()) == 3
