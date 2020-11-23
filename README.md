# Python Template Repo
---

Template Python Repo for getting started with a Python Library with GitHub.

## Benefits

* GitHub Action Templates
* Auto deploy to PyPi
* Issue and Pull Request Templates
* Auto Configured install and test requires

## To Use

1. Clone the repo
2. Rename the [src](src) directory to the name of your project.
    * Make sure the names updates in [setup.py](setup.py), [lint workflow](.github/workflows/lint.yml).
3. Add your project requirements to [requirements.txt](requirements.txt).
    * If you have any development requirements add them to [requirements-dev.txt](requirements-dev.txt).
4. Change the [License](LICENSE) if desired.
5. Edit the assignees in [Issue Templates](.github/ISSUE_TEMPLATE), [Pull Request Template](.github/PULL_REQUEST_TEMPLATE) and [Dependabot Config](.github/dependabot.yml).
6. Edit [setup.py](setup.py) to have relevant links and information. 
7. Add `PYPI_USERNAME` and `PYPI_PASSWORD` into the secrets section.
