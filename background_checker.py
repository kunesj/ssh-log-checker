#!python2
#coding: utf-8

import check_ssh_log

if check_ssh_log.last_new_confirmed():
    check_ssh_log.check_ssh_log()
else:
    print "INFO: Last new SSH logins not read"

if not check_ssh_log.last_new_confirmed():
    # TODO - show dialog with list of new SSH logins and
    # check_ssh_log.confirm_new()
