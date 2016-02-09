SSH log checker
===============
[![Code Climate](https://codeclimate.com/github/kunesj/ssh-log-checker/badges/gpa.svg)](https://codeclimate.com/github/kunesj/ssh-log-checker)

Periodically check SSH logs and warns user with popup if there are any new logins or login attempts. Linux only.

Install 
-------

To install into system path run: (if it fails on first try, try second time)

    make install

To install dependencies run: (only on Debian based systems)

    make install_dep

Usage
-----

run from commandline with:

    sshlogchecker


To autostart script with conky, add to .conkyrc:

    ${execpi 300 sshlogchecker --once > /dev/null }


Show commandline options with:

    sshlogchecker --help
