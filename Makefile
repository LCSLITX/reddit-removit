SHELL := /bin/zsh

freeze:
	pip freeze | cat > requirements.txt

execute_pylint: 
	python3 -m pylint --rcfile=.pylintrc --verbose --clear-cache-post-run=y src/*.py

execute_tests: execute_pylint
	source .env && python3 -m pytest -vv --cache-clear --cov=. tests/*test.py

execute_script:
	source .env && python3 -m src.main

docker_build_image: 
	source .env && docker build -t reddit-removit .

docker_remove_container:
	docker container remove $$(docker container stop REMOVIT)

execute_container: docker_build_image 
	source .env && docker run -d -ti -e REDDIT_CLIENT_ID -e REDDIT_CLIENT_SECRET -e REDDIT_USERNAME -e REDDIT_PASSWORD -e REDDIT_DEBUG_MODE --name REMOVIT reddit-removit