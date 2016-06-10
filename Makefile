
help:
	@echo "To install app: make install"
	@echo "To install dependencies: make install_dep"

install: clean
	sudo python3 setup.py build install

install_dep:
	sudo apt-get install python3 python3-pip python3-pyqt4
	sudo pip3 install appdirs python-dateutil

run:
	python3 -m sshlogchecker

remove_user_data:
	rm -rf ~/.local/share/sshlogchecker

clean:
	sudo rm -rf build dist sshlogchecker.egg-info
