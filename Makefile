.PHONY: init format

init:
	poetry install

format:
	black plog tests
	isort plog tests