install:
	#install files
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py

test:
	python -m pytest -vv --cov=mylib test_*.py --cov=main test_*.py
build:
	docker build -t wikify .
run:
	docker run -p 8000:8000 wikify
deploy:
	# deploy
	
all: install lint test deploy    