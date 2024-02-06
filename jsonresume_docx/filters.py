# Filters largely copied from Ansible:
# https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/filter/core.py

import datetime


def date_to_month_year(string):
    date = datetime.date.strptime(string, "%Y-%m-%d")
    return date.strftime("%b. %Y")
