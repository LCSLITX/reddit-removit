SHELL := /bin/zsh

freeze:
	pip freeze | cat > requirements.txt

install_dependencies:
	pip install -r requirements.txt

execute_pylint: 
	python3 -m pylint --rcfile=.pylintrc --verbose --clear-cache-post-run=y src/*.py

execute_tests: execute_pylint
	source .env && python3 -m pytest -vv --cache-clear --cov=. tests/*test.py

execute_script:
	source .env && python3 -m src.main