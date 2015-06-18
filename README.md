SSH log checker
===============
Periodically check SSH logs and warns user with popup if there are any new logins. Linux only.

Install 
-------

To install into system path run: (if it fails for first try, try again)

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
