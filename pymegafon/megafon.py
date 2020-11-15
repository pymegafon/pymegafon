#!/usr/bin/env python3
"""
    Interacts with MegaFon
"""

import logging

from . import balance
from . import credentials

def main(login=None, password=None, do_check_balance=False, debug=False):
    logging.basicConfig(level=logging.INFO)
    logging.debug("Validating credentials..")

    if not login or not password:
        env_credentials = credentials.get_from_env()
        login = env_credentials['login']
        password = env_credentials['password']

    login = credentials.uniform_login(login)

    if do_check_balance:
        connection = balance.APIConnection(login=login, password=password)
        connection.sign_in()
        connection.get_balance()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main("stub", "stub")
