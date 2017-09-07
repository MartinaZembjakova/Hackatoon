.PHONY= venv venv_install

venv:
	virtualenv -p /usr/bin/python3 venv

venv_install: venv
	pip install --upgrade pip
	pip install -r requirements.txt

