install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py askmendel/*.py askmendel/services/*.py
lint:
	pylint --disable=R,C *.py
all: install format lint