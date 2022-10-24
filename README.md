# A Sample Python Project

[![Documentation Status](https://readthedocs.org/projects/python-project-exsample/badge/?version=latest)](https://python-project-exsample.readthedocs.io/en/latest/?badge=latest)

This repository serves as a template for developing python packages. Thereby this repo should mainly serve two purposes:

1. It should serve as an example for people who are new to python
2. There is no need to configure things like testing, documentation, and `setup.py` over and over again. This repo should serve as an initial python project seed which can be used to start off new python packages 🚀. 

## How to Use

1. clone it to your local filesystem: `git clone git@github.com:tobirohrer/python-project-template.git` (depending on your needs, you can also [fork](https://github.com/tobirohrer/python-project-template/fork) the repo or [create your own repo based on this one](https://github.com/tobirohrer/python-project-template/generate))		
2. cd into the cloned repository: `cd python-project-template`
3. optional:

	4. create new python environment: `conda create -n <env_name> python=3.9`
	5. activate new python environment: `conda activate <env_name>`
6. install the package by: `pip install -e .[docs,tests]` (If you don´t want to run tests or build the sphinx documentation locally, you can omit the `[docs,tests]` parameter)
7. run `python use_package.py` to use the sample package :)

## Whats Included

### Documentation

[Sphinx](https://www.sphinx-doc.org/) is used to create the documentation and [Read the Docs](https://readthedocs.org/) to publish it. The documentation was created mainly by running `sphinx-quickstart` as explained in the [tutorial](https://www.sphinx-doc.org/en/master/tutorial/getting-started.html). 

To see the documentation, you can either:

- Build and open the documentation locally: By running `make doc` in the project root (or run `make html` in the `/docs` subfolder). After building, the documentation is available as html in the folder `./docs/build/html`. Open the `index.html` file (i.e. in your browser) to see the documentation.
- Or open the documentation live on [https://python-project-exsample.readthedocs.io/en/latest/](https://python-project-exsample.readthedocs.io/en/latest/).

### Testing

[pytest](https://docs.pytest.org/) is used for testing. You can run the tests locally, by running `make test` in the project root (or you run `pytest ./tests`).

### Continuous Integration

GitHub Actions are used to automatically test the package whenever code is pushed to the master branch. The configuration can be found in `/.github/workflows/test.yml`.

