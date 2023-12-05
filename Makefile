SHELL := /bin/bash

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	python3 manage.py runserver 0.0.0.0:8011

freeze:
	pip3 freeze > req.txt

drop-tables:
	python3 manage.py runscript drop_tables

create-super-user:
	python3 manage.py runscript create_super_user

init:
	python3 manage.py runscript drop_tables
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runscript create_super_user
	python3 manage.py runserver 0.0.0.0:8008

remove-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

install-requirements:
	pip3 install -r requirements.txt

uninstall-requirements:
	pip3 uninstall -r requirements.txt -y


RELEASE_VERSION := $(shell cat VERSION)
push-version:
	git add . && git commit -m 'update version = $(RELEASE_VERSION)' && git push

uat-tag:
	@git tag -a "uat-v$(RELEASE_VERSION)" -m "uat-v$(RELEASE_VERSION)"
	@git push origin "uat-v$(RELEASE_VERSION)"



