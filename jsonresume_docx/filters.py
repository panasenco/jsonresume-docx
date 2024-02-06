# Filters largely copied from Ansible:
# https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/filter/core.py

import datetime


def to_datetime(string, format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.strptime(string, format)
