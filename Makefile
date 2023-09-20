install:
	#install files
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py

test:
	# tests
deploy:
	# deploy
	
all: install lint test deploy    