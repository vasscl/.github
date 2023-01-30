# Pre-commit

A framework for managing and maintaining multi-language pre-commit hooks. To know more visit [pre-commit website](https://pre-commit.com)

Here you can find sample pre-commit configuration for your repositories.

Asume that we have a file on the root of our repository called `pre-commit.yaml` we can configure it like:

> To know more about the actions and configuration for every step, visit the url described in the "repo" property

## Common configuration

- Secrets leak
- Files and merge checks

```yaml
common:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-added-large-files
    -   id: check-case-conflict
    -   id: check-merge-conflict
    -   id: mixed-line-ending
-   repo: https://github.com/zricethezav/gitleaks
    rev: v8.8.11
    hooks:
    -   id: gitleaks
```

## Golang configurations

You can extend your `pre-commit.yaml` file with:

```yaml
common:
...
-   repo: https://github.com/tekwizely/pre-commit-golang
    rev: v1.0.0-beta.5
    hooks:
    -   id: go-fmt
    -   id: go-mod-tidy
    -   id: go-test-mod
    -   id: go-revive-mod
    -   id: go-sec-mod
    -   id: go-staticcheck-mod
-   repo: https://github.com/hadolint/hadolint
    rev: master
    hooks:
      - id: hadolint-docker
```

## Node js configuration

You can extend your `pre-commit.yaml` file with:

```yaml
-   repo: https://github.com/pre-commit/mirrors-prettier
    rev: v2.7.1
    hooks:
    -   id: prettier
-   repo: https://github.com/pre-commit/mirrors-eslint
    rev: v0.18.0
    hooks:
    -   id: eslint
-   repo: https://github.com/hadolint/hadolint
    rev: master
    hooks:
      - id: hadolint
```

> you can browse more hooks [here](https://pre-commit.com/hooks.html)

## Monorepo strategy

For the monorepo strategy we have to modify our recipe as follows:

Node js example for monorepo

```yaml
-   repo: https://github.com/pre-commit/mirrors-prettier
    rev: v2.7.1
    hooks:
    -   id: prettier
        name: 'prettier_app1'
        files: '^app1/'
    -   id: prettier
        name: 'prettier_app2'
        files: '^app2/'
-   repo: https://github.com/pre-commit/mirrors-eslint
    rev: v0.18.0
    hooks:
    -   id: eslint
        name: 'eslint_app1'
        files: '^app1/'
    -   id: eslint
        name: 'eslint_app2'
        files: '^app2/'
-   repo: https://github.com/hadolint/hadolint
    rev: master
    hooks:
      - id: hadolint
        name: 'hadolint_app1'
        files: '^app1/'
      - id: hadolint
        name: 'hadolint_app2'
        files: '^app2/'
```
