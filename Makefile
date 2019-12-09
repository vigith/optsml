all: test

init:
	pip install pipenv --upgrade
	pipenv install --dev

test:
	pipenv run py.test --junitxml=report.xml
