# Filters largely copied from Ansible:
# https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/filter/core.py

from datetime import datetime


def to_resume_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").strftime("%b. %Y")
