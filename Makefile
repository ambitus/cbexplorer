#

.PHONY: clean
clean: ## clean project
clean:
	-rm -rf ./tests/controlblocks
	-rm -rf ./tests/jzon
	-rm -rf ./tests/zml
	-rm -rf ./dist
	-rm -rf ./build
	-rm -rf *.egg-info
	-rm -rf ./pysvc/__py_cache__
	-rm -rf ./tests/__py_cache__

.PHONY: build
build: ## build project
build: clean install-dev
	pipenv run python setup.py sdist bdist_wheel

.PHONY: help
help: ## display helpful information
help:
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/' | sort`); \
	printf "$(COLOR1)Usage:$(COLOR0)\n"; \
	printf "  make [$(COLOR2)target$(COLOR0)]\n\n"; \
	printf "$(COLOR1)Targets:$(COLOR0)\n"; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf "  $(COLOR2)%-30s$(COLOR0) %s\n" $$help_command $$help_info ; \
	done

.PHONY: install
install: ## install dependencies for local development
install:
	pip install -U setuptools
	pip install -e ".[dev]"
	pip install -r requirements.txt

.PHONY: pipenv-install
pipenv-install: ## install dependencies for local development through Pipenv
	pipenv install --dev
	pipenv lock
	pipenv run pipenv-setup sync --dev

.PHONY: test
test: ## test and lint code
test:
	./tests/test.sh
	flake8 ./cbexplorer
