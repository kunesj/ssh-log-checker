SSH log checker
===============
Periodically check SSH logs and warns user with popup if there are any new logins. Linux only.

install: (Debian based)

    make install install_dep


Usage
-----

run from commandline with:

    sshlogchecker


To autostart script with conky, add to .conkyrc:

    ${execpi 300 sshlogchecker --once > /dev/null }


Show commandline options with:

    sshlogchecker --help
