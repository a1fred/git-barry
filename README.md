[![PyPI version](https://badge.fury.io/py/gitbarry.svg)](https://badge.fury.io/py/gitbarry)
[![Build Status](https://travis-ci.org/a1fred/git-barry.svg?branch=master)](https://travis-ci.org/a1fred/git-barry)
[![Coverage Status](https://coveralls.io/repos/github/a1fred/git-barry/badge.svg?branch=master)](https://coveralls.io/github/a1fred/git-barry?branch=master)

Gitflow-inspired, but flexible and customizable project management tool.

Quick demo:
```shell
$ git barry start feature awesome  # Create and switch to feature branch
$ git barry finish  # Merge with master then delete branch, switch to master
$ git barry start release v0.9.8  # Create and switch to release branch
$ git barry finish  # Tag branch, merge with master
```

# Installation
## From source
```shell
$ python3 setup.py install
```
## From pypi
```shell
$ pip install gitbarry
```

# Usage

## Command line syntax
```shell
git barry <reason> <type> [name]
```
* reason - start or finish
* type - one types from ini
* name - name of task when start


#### Start new feature
```shell
$ git barry start feature <name>
```

#### Finish feature
```shell
$ git barry finish
```

#### Switch between tasks
```shell
$ git barry switch feature 22
$ git barry switch release v2.1
```

# Configuration
Store your configuration in *{PROJECT_ROOT}/gitbarry.ini*.

## Syntax
Example
```ini
[task-feature]
branch-from=master
finish-action=merge
finish-branch-to=master
```

We create task named *feature*
 - *branch-from* - branch from who we checking out when start feature
 - *finish-branch-to* - merge action-parameter. Target-branch for merge.

### Finish actions
#### Merge
name in configfile: *merge*

Merge current task-branch to *finish-branch-to* parameter.
Then check out to *finish-branch-to*.

#### Pull-request
name in configfile: *pull-request*

Send http-request, that created pull-request to *finish-branch-to*

Request-parameters:
* *finish-pull-request-url* - url template. http://gitlab.com/example/tree/{branch} for example
* *finish-pull-request-method* - request method. Default is GET

#### Tag
name in configfile: *tag*

Tag branch

Request-parameters:
- *branch-from* - branch from who we checking out when start feature
- *finish-branch-to* - merge action-parameter. Target-branch for merge.

#### Open-browser
name in configfile: *open-browser*

Open browser when finish

Parameters:
* *finish-open-browser-url* - url template. http://gitlab.com/example/tree/{branch} for example
