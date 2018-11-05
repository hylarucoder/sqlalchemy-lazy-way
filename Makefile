.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

py := poetry run python
pytest := PYTHONPATH=./sqlalchemy_lazy_way poetry run pytest

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

sep--sep-a: ## ========== 开发时命令 ==============

sep--sep-b: ## ========== 测试与代码质量 ==============
	echo "## ========== 本行只是优雅的分割线  ==============="

lint: ## check style with flake8
	echo "TODO"

test: ## run tests quickly with the default Python
	$(pytest) --html=test_report.html --self-contained-html

coverage: ## check code coverage quickly with the default Python
	$(pytest) tests/ --cov=sqlalchemy_lazy_way

sep--sep-c: ## ========== 文档生成相关 ==============
	echo "## ========== 本行只是优雅的分割线  ==============="

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/source/sqlalchemy_lazy_way.rst
	rm -f docs/source/sqlalchemy_lazy_way/*
	rm -f docs/source/modules.rst
	find ./sqlalchemy_lazy_way/  -maxdepth 1 -not -name "*template" -not -name "*static" -not -name "*__pycache__*" -not -name 'lemonade' -exec sphinx-apidoc -o docs/source/sqlalchemy_lazy_way"{}" \;
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

sep--sep-d: ## ========== 程序发布相关 ==============
	echo "## ========== 本行只是优雅的分割线  ==============="

release: clean ## package and upload a release
	$(py) setup.py sdist upload
	$(py) setup.py bdist_wheel upload

dist: clean ## builds source and wheel package
	$(py) setup.py sdist
	$(py) setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	$(py) setup.py install

sep--sep-e: ## ========== 文件清理相关 ==============
	echo "## ========== 本行只是优雅的分割线  ==============="

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

