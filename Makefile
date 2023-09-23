install:
	#install files
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py

test:
	python -m pytest -vv --cov=mylib test_*.py --cov=main test_*.py
build:
	# build container
deploy:
	# deploy
	
all: install lint test deploy    