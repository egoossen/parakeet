# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Copyright (C) 2024 Elijah Goossen, ekgoossen@gmail.com

import sqlite3

class Budget():
    def __init__(self, database:str=":memory:"):
        self.__con = sqlite3.connect(database)
        self.__cur = self.__con.cursor()
        self.__create_account_table()

    def add_account(self,name:str, budgeted:float=0) -> None:
        self.__cur.execute(
            """
            INSERT INTO accounts(name, budgeted)
                VALUES(?, ?);
            """,
            [name, budgeted]
        )

    def get_accounts(self) -> list:
        res = self.__cur.execute("SELECT name, budgeted FROM accounts;")
        return res.fetchall()

    def __create_account_table(self):
        self.__cur.execute("""
            CREATE TABLE accounts(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                budgeted REAL
            );
            """)
