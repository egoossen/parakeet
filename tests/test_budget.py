# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (C) 2024 Elijah Goossen, ekgoossen@gmail.com

import pytest

from parakeet.budget import (
    Budget,
    ImbalanceException
)

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

def test_add_budgeted_expense(budget):
    budget.add_account('Expense', budgeted=100)
    assert budget.get_accounts()[0] == ('Expense', False, 100)

def test_add_budgeted_income(budget):
    budget.add_account('Income',is_income=True, budgeted=1000)
    assert budget.get_accounts()[0] == ('Income', True, 1000)

def test_get_mismatch_expense(budget):
    budget.add_account('Expense', budgeted=100)
    assert budget.get_mismatch() == -100

def test_get_mismatch_income(budget):
    budget.add_account('Income', is_income=True, budgeted=100)
    assert budget.get_mismatch() == 100

def test_get_mismatch(budget):
    budget.add_account('Income', is_income=True, budgeted=100)
    budget.add_account('Expense', budgeted=10)
    assert budget.get_mismatch() == 90

def test_under_budget(budget):
    budget.add_account('Income', is_income=True, budgeted=100)
    budget.add_account('Expense', budgeted=10)
    with pytest.raises(ImbalanceException, match='Under-budget by 90'):
        budget.verify()

def test_over_budget(budget):
    budget.add_account('Income', is_income=True, budgeted=100)
    budget.add_account('Expense', budgeted=110)
    with pytest.raises(ImbalanceException, match='Over-budget by 10'):
        budget.verify()

def test_balanced_budget(budget):
    budget.add_account('Income', is_income=True, budgeted=100)
    budget.add_account('Expense', budgeted=100)
    budget.verify() # Does not raise an error

def test_balanced_budget_positive_tolerance(budget):
    budget.add_account('Income', is_income=True, budgeted=100)
    budget.add_account('Expense', budgeted=100 + 1e-5)
    budget.verify() # Does not raise an error

def test_balanced_budget_positive_tolerance(budget):
    budget.add_account('Income', is_income=True, budgeted=100)
    budget.add_account('Expense', budgeted=100 - 1e-5)
    budget.verify() # Does not raise an error
