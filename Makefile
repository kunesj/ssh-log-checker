
help:
	@echo "To install app: make install"
	@echo "To install dependencies: make install_dep"

install: clean
	sudo python setup.py build install
	
install_dep:
	sudo apt-get install python python-pip python-qt4 
	sudo pip install appdirs python-dateutil
	
run:
	python -m sshlogchecker

remove_user_data:
	rm -rf ~/.local/share/sshlogchecker

clean:
	sudo rm -rf build dist sshlogchecker.egg-info
