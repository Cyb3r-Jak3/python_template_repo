.PHONY: clean clean-build clean-pyc test docs

clean: clean-build clean-pyc

full-test: lint test

ifeq ($(OS),Windows_NT)
    RM = del //Q //F
    RRM = rmdir //Q //S
else
    RM = rm -f
    RRM = rm -f -r
endif

clean-build:
	$(RM) -r build/
	$(RM) -r dist/
	$(RM) -r *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec $(RM) {} +
	find . -name '*.pyo' -exec $(RM) {} +
	find . -name '*~' -exec $(RM) {} +

build:
	python setup.py sdist bdist_wheel

check-dist:
	pip install twine --quiet
	python setup.py egg_info
	python setup.py sdist bdist_wheel
	twine check --strict dist/*

lint:
	black --check python_gh_template
	pylint python_gh_template
	flake8 --statistics --show-source --count python_gh_template
	bandit -r python_gh_template

test:
	py.test --cov python_gh_template tests/ -vv