# Installation
## From source
```shell
$ python3 setup.py install
```
## From pypi
```shell
$ python install gitbarry
```

# Usage

## Command line syntax
```shell
git barry <reason> <type> [name]
```
reason - start or finish
type - one types from ini
name - name of task when start


## Start new feature
```shell
$ git barry start feature <name>
```

## Finish feature
```shell
$ git barry finish
```

# Configuration
Store your configuration in *gitbarry.ini*.

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
 - *finish-action* - action, called when finish
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

#### Open-browser
name in configfile: *open-browser*

Open browser when finish

Parameters:
* *finish-open-browser-url* - url template. http://gitlab.com/example/tree/{branch} for example
