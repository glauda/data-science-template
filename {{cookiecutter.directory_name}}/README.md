# {{cookiecutter.directory_name}}

[![python: version](https://img.shields.io/badge/Python-{{cookiecutter.python_version}}-blue)](https://docs.python.org/3/whatsnew/{{cookiecutter.python_version}}.html)

[![formatter: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


## Coding guidelines

* To keep data organized, the [data engineering convention](https://kedro.readthedocs.io/en/0.14.3/06_resources/01_faq.html) can be used. An example of this convention can be found in the `notebooks` folder.
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `src/conf/local/`
* Order your imports with `isorts`
* Add [typing](https://docs.python.org/3/library/typing.html) to your function signatures
* Use the git hook to only commit clean notebooks to the repo (see below)
* Follow pep8 convention
* Use [Google style docstring](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) to document functions
* To organize git branches, try to use a prefix. Examples: `feature/*` or `bug-fix/*`
* Use prefix to indicate the variable's type. There are some examples in the table below: 

    | prefix | type |
    |---|---|
    | ax | numpy array |
    | df | pandas dataframe |
    | d | dictionnary |
    | l | list |
    | dt | datetime |
    | ts | timestamp |
    | set | set |



## Set up the environment 

In this project, the makefile is used to create alias for command bash scripts. To setup the project:

1. Install [Poetry](https://python-poetry.org/docs/#installation)

2. Set up the environment:
``` bash
make activate
make setup
```

## Install new packages
To install new PyPI packages, run:
```bash
poetry add <package-name>
```