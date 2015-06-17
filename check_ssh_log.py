#!python2
#coding: utf-8

import os, sys

from datetime import datetime
from dateutil.parser import parse

# list paths to logfiles. from older to newest
logfiles_default = ['/var/log/auth.log.1', '/var/log/auth.log']

# file/path where to save info about when was last log check
last_check_file = '.ssh_log_last_check'

# file/path where to save new info parsed from logfiles
new_info_file = '.ssh_log_new_info'

def format_info(info):
    time = info[0].isoformat()
    info = [time, info[1], info[2], info[3]]
    return " ".join(info)

def check_ssh_log(logfiles=None):
    if logfiles is None:
        logfiles = logfiles_default
    
    # load lines releated to SSH from logfiles
    ssh_log = []
    for logfile in logfiles:
        try:
            with open(logfile, 'r') as f:
                for line in f:
                    if 'sshd' in line and 'pam_unix' not in line:
                        ssh_log.append(line.strip())
        except Exception, e:
            print "Error: Failure when pasing logfile ("+logfile+"), error_msg: "+str(e)


    # parse SSH log lines
    parsed_log = []
    for line in ssh_log:
        l = line.split()
        
        time_date = parse(l[0]+" "+l[1]+" "+l[2])
        hostname = l[3]
        process = l[4][:-1]
        msg = " ".join(l[5:])
        
        #['2015-02-08T15:42:10', 'MS-7758', 'sshd[31838]', 'Accepted password for jirka642 from 192.168.1.12 port 46363 ssh2']
        parsed_log.append([time_date, hostname, process, msg])


    # get time of last log check
    if os.path.isfile(last_check_file):
        with open(last_check_file, 'r') as f:
            last_check = f.read().strip()
            
        last_check = parse(last_check)
        print "INFO: Last check on: "+last_check.isoformat()
    else:
        last_check = datetime.fromtimestamp(0)
        print "INFO: Log was never chacked before"


    # filter new info
    new_shh_logins = []
    for info in parsed_log:
        if info[3].startswith("Server listening on"):
            continue # ignore SSH startup message
        if info[3].endswith('terminating.'):
            continue # ignore SSH shutdown message
        
        if last_check < info[0]:
            new_shh_logins.append(info)
        
            # print new log info
            print format_info(info)
        
    # save new info to file and update last_check info
    with open(last_check_file, 'w') as f:
        f.write(datetime.now().isoformat())
    with open(new_info_file, 'w') as f:
        for info in new_shh_logins:
            line = format_info(info)+"\n"
            f.write(line)
            
    return new_shh_logins

def get_new():
    """
    Returns False if new_info_file is not empty
    """
    data = ''
    if os.path.isfile(new_info_file):
        with open(new_info_file, 'r') as f:
            data = f.read().strip()
 
    return data

def last_new_confirmed():
    """
    Returns False if new_info_file is not empty
    """
    if '' == get_new():
        return True
    else: 
        return False

def confirm_new():
    """
    Empties new_info_file
    """
    with open(new_info_file, 'w') as f:
        f.write('')

if __name__ == "__main__":
    check_ssh_log()
