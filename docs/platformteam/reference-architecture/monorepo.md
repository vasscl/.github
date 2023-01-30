# Monorepo by product

> **What to read previously?** - [Reference Architecture](index.md)

## What is a monorepo?

It is a single git repository described as:

- Contains more than one artifact or microservice.
- Each microservice can be deployed by its own, without any dependency.

## Why a monorepo?

It creates a single source of truth. It makes it easier to document it, share code, on boarding process, architecture discovery and inter team complex visibility.

A monorepo structure improve:

### Visibility

Using a single repository gives you visibility into your code and assets for every project. This helps you manage dependencies.

### Collaboration

A single repository makes it easier to collaborate. That’s because everyone can access the code, files, and assets. So, developers can share and reuse assets.

### Speed

Using a single repository can help you accelerate development. For instance, you can make atomic changes (one action to make a change across multiple projects).

## Why per product?

A monorepo provides a single source of truth and other advantages. Create a repository, bound to a business product, create a focal point for product teams, add visibility to the product source code, the CI/CD process, security considerations, shared code, and maintainability avoiding orphans repositories and repo anarchy.

## Monorepo folder structure

Base folder structure

```code
- root
  |- .github/
  |- deployr/
  |- infra/
  |- docs/
  |- catalog-info.yaml
  |- mkdocs.yaml
```

**.github** folder, common CI actions take in place here per artifact.

**deployr** folder, here you should have kubernetes deployment per namespace divided per artifact subfolder.

**infra** folder, common infrastructure requirements take in place here using terraform files.

**docs** folder, common documentation in markdown per artifact.

**catalog-info.yaml** file, developer portal system documentation for auto discovery.

**mkdocs.yaml** file, developer portal documentation configuration for auto discovery.

## Extending the monorepo

How a new artifact is added to the repo?

As described before we have common folder for common actions, when we add a new artifact it should follow the following:

Base folder structure, adding a new artifact call `principal-api`

```code
- root
  |- .github/
    |- workflows/
      |- principal-api/
        |- build-staging.yaml
  |- deployr/
    |- principal-api/
      |- *yaml
  |- infra/
    |- principal-api/
      |- *.tf
  |- docs/
  |- principal-api/
    |- docs
    |- catalog-info.yaml
    |- mkdocs.yaml
  |- catalog-info.yaml
  |- mkdocs.yaml
```
