.PHONY: local

local:
	docker-compose up -d
	export FLASK_APP=run.py
	export FLASK_ENV=development
	flask run

