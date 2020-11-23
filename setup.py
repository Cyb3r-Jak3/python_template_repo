from setuptools import setup

VERSION = "<Version>"
install_reqs = open("requirements.txt").readlines()

test_requirements = open("requirements-dev.txt").readlines()

readme = open("README.md").read()

setup(
        name="Python Template",
        version=VERSION,
        description="Insert short description here",
        long_description=readme,
        author="Your Pypi user name",
        author_email="Your Email",
        url="Link to the repo",
        project_urls={
            "Changelog": "https://github.com/Cyb3r-Jak3/python_template_repo/blob/master/CHANGELOG.md",
        },
        download_url="https://github.com/Cyb3r-Jak3/python_template_repo/releases/latest",
        packages=[
            "src"
        ],
        package_dir={"src": "src"},
        tests_require=test_requirements,
        install_requires=install_reqs,
        license="MPL",
        zip_safe=False,
        keywords="template",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
)
