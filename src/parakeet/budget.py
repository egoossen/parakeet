# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (C) 2024 Elijah Goossen, ekgoossen@gmail.com

import sqlite3

class ImbalanceException(Exception):
    pass

class Budget():
    def __init__(self, database:str=":memory:"):
        self.__con = sqlite3.connect(database)
        self.__cur = self.__con.cursor()
        self.__create_account_table()

    def add_account(self,
            name:str,
            is_income:bool=False,
            budgeted:float=0) -> None:
        self.__cur.execute(
            """
            INSERT INTO accounts(name, is_income, budgeted)
                VALUES(?, ?, ?);
            """,
            [name, is_income, budgeted]
        )

    def get_accounts(self) -> list:
        res = self.__cur.execute(
            "SELECT name, is_income, budgeted FROM accounts;"
        )
        return res.fetchall()

    def get_mismatch(self):
        res = self.__cur.execute("SELECT budgeted,is_income FROM accounts;")
        accounts = res.fetchall()
        income = [acct[0] for acct in accounts if acct[1]]
        expenses = [acct[0] for acct in accounts if not acct[1]]
        return sum(income) - sum(expenses)

    def verify(self):
        tolerance = 1e-4
        mismatch = self.get_mismatch()
        if mismatch > tolerance:
            raise ImbalanceException(f'Under-budget by {mismatch}')
        elif mismatch < -tolerance:
            raise ImbalanceException(f'Over-budget by {-mismatch}')

    def __create_account_table(self):
        self.__cur.execute("""
            CREATE TABLE accounts(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                is_income BOOL,
                budgeted REAL
            );
            """)
