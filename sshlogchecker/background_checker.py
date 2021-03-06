#!/usr/bin/env python3
# encoding: utf-8

import time, sys, argparse

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QApplication, QVBoxLayout, QTextEdit, \
                        QPushButton, QWidget

import sshlogchecker.check_ssh_log as check_ssh_log

class InfoDialog(QMainWindow):
    def __init__(self, parent=None, info_data=''):
        QMainWindow.__init__(self)

        self.info_data = info_data
        self.confirmed = False

        self.resize(700, 400)
        self.initUI()

    def initUI(self):
        cw = QWidget()
        self.setCentralWidget(cw)
        layout_main = QVBoxLayout()
        layout_main.setSpacing(5)

        self.setWindowTitle('New SSH logins to Localhost')

        ## Info
        self.info = QTextEdit()
        self.info.setReadOnly(True)
        self.info.setLineWrapMode(QTextEdit.NoWrap)
        self.info.append(self.info_data)

        layout_main.addWidget(self.info, 1)

        # confirm button
        self.btn_confirm = QPushButton('Confirm')
        self.btn_confirm.pressed.connect(self.confirm)
        layout_main.addWidget(self.btn_confirm)

        ## add stretch
        layout_main.addStretch()

        ## Setup layout
        cw.setLayout(layout_main)
        self.show()

    def confirm(self):
        self.confirmed = True
        self.close()

    def getConfirmed(self):
        return self.confirmed

def main():
    parser = argparse.ArgumentParser(
        description='SSH log checker'
    )
    parser.add_argument(
        '-s', '--sleep',
        type=int,
        default=300,
        help='Sleep time between checks, default is 300 seconds')
    parser.add_argument(
        '--once',
        action='store_true',
        help="Run only once (doesn't start loop)")
    args = parser.parse_args()

    app = QApplication(sys.argv)
    while True:
        # check if last info check was confirmed
        if check_ssh_log.last_new_confirmed():
            check_ssh_log.check_ssh_log()
        else:
            print("INFO: Last new SSH logins not read")

        # shows list of new SSH logins
        if not check_ssh_log.last_new_confirmed():
            infoD = InfoDialog(info_data = check_ssh_log.get_new())
            app.exec_()
            confirmed = infoD.getConfirmed()

            if confirmed:
                check_ssh_log.confirm_new()

        if args.once:
            break
        else:
            time.sleep(args.sleep)

if __name__ == "__main__":
    main()
