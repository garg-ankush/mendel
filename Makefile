install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py askmendel
format:
	black *.py askmendel/*.py askmendel/services/*.py
all: install lint format