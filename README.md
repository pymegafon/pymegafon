# PyMegaFon - Manage your MegaFon account

This toolset allows you to automate manipulations with your MegaFon account.

Currently implemented funcions:
1. Sign in
2. Retrieve account balance
3. Retrieve subscriptions status

## Quick start

There are two ways to use this "product": as a CLI tool and as a python module.

### Install `pymegafon` python package:

```bash
$ python3 -m pip install --user pymegafon
```

### Run in CLI

```bash
$ python3 -m pymegafon --help
```

#### Check balance

```bash
$ python3 -m pymegafon -l 79210001111 -p rND0mPw --check-balance
INFO:root:Signing in...
INFO:root:Balance: 302.44
```

#### Check internet subscription remainings

```bash
$ python3 -m pymegafon -l 79210001111 -p rND0mPw --check-remainings
INFO:root:Signing in...
INFO:root:Internet: {'total': 30, 'available': 7.54}
```

#### Ccredentials via environment

You can pass your credentials via environment variables. This way just ommit auth related CLI parameters.

```bash
$ export MEGAFON_LOGIN="79210001111"
$ export MEGAFON_PASSWORD="rND0mPw"
$ python3 -m pymegafon --check-remainings
```

## Reporting bugs

Please, use GitHub issues.

## Requesting new functionality

Please, use GitHub issues.
