install:
	#install files
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	# format code
	black *.py mylib/*.py
lint:
	# flake or pylint
test:
	# tests
deploy:
	# deploy
	
all: install lint test deploy    