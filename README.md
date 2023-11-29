# Setup

## Install Python

If you do not have Python, please install the latest 3.x version from python.org. You can check this by running: 

```
$ python --version
```

## Install Pipenv

### Install pip 

Make sure you have pip available, you should if you are using Python downloaded from python.org.

Check this by running:

```
$ pip --version
```

If you do not have Pipenv installed already, install with [Homebrew](https://brew.sh/). [Pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies) is the offical package management tool reccomended by Python (similar to `npm`): 

```
$ brew install pipenv
```

Alternatively, you can install Pipenv with pip: 

```
$ pip install --user pipenv
```

## Install dependencies

```
$ pipenv install
```

## Run tests

```
$ pipenv run test
```

## Run development server

```
$ pipenv run runserver
```

## Create db

```
$ pipenv run createdb
```

## Run migrations

```
$ pipenv run migrate
```