
.PHONY: dump_requirements
dump_requirements:
	@pipenv run pip freeze > requirements.txt