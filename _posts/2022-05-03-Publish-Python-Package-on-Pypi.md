# Publish Python Package on Pypi

Table of content
  - [Create conda environment and install Cookiecutter](#create-conda-environment-and-install-cookiecutter)
  - [Use Cookiecutter to generate template for a python package](#use-cookiecutter-to-generate-template-for-a-python-package)
  - [Push to Github repo](#push-to-github-repo)
    - [Create a repo on Github](#create-a-repo-on-github)
    - [Initialize local repository with Git](#initialize-local-repository-with-git)
  - [Upload to Pypi](#upload-to-pypi)

This post will show the process of creating a python package and publish it on Pypi. The steps mostly follows this [Youtube](https://www.youtube.com/watch?v=7FcX9uWDuIQ) by [Qiusheng Wu](https://github.com/giswqs).

Before you start, make sure you have created an account with Github and Pypi, and have installed Anaconda on your PC.

## Create conda environment and install Cookiecutter

In this example, we use `pypackage` as the environment name.
```
conda create --name pypackage python
conda activate pypackage
pip install cookiecutter
```

## Use Cookiecutter to generate template for a python package
I will use the template provided by [giswqs/pypackage](https://github.com/giswqs/pypackage) which is originally created by [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage). The main differences is that the modified version used markdown instead of restructured text as documentation.

```
cookiecutter gh:giswqs/pypackage
```
This is prompt up a few questions asking about Full name, email address, Github username, project name (i.e., package name), project description, Pypi username, version, and etc. Then a folder with the same project name will be created under current working directory.

## Push to Github repo

### Create a repo on Github
Create an empty repo on Github with the same project name. Do no create README file! Here we use `demo` as the repo/project name.

### Initialize local repository with Git
```
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/pinshuai/demo.git
git push -u origin main
```

Add your python scripts under `./demo/demo/` and commit. Those scripts will be published on Pypi.

## Upload to Pypi

First install some packages (e.g., `twine`) that will be used to push to Pypi.
```
pip install -r ./demo/requirements_dev.txt
```

Create `dist` folder and create a tarball inside it.
```
python setup.py sdist
```

Use `twine` to upload the tarball to Pypi. This will ask for the username and passward for Pypi.
```
twine upload demo-0.0.1.tar.gz
```

Now the package has been successfully upload to Pypi! Now users can install the package using `pip install demo`.

## Deploy documentation website on Github Pages

The python package template already contains the necessary files (e.g, `mkdocs.yaml`) to deploy your documentation website using `MkDocs` on Github Pages. You will also find `/docs` folders with markdown files which will be used for documentation.

### Setup MkDocs
First, we need to install `MkDocs` and some plugins as specified in the `mkdocs.yaml`.
```bash
pip install mkdocs
pip install mkdocs-material
# plugins are optional 
pip install mkdocstrings
pip install mkdocs-git-revision-date-plugin
pip install mkdocs-jupyter
```

### Deploy the website
Simply run the following command under the repo. It should autimatically create the website on `pinshuai.github.io/demo`. Make sure the source of the GitHub Pages under Settings is pointed to `gh-pages` branch and `/(root)` folder.

```bash
 mkdocs gh-deploy
```

## Reference

- My `modvis` python package: https://github.com/pinshuai/modvis
- `Pypackage` by Qiusheng Wu: https://github.com/giswqs/pypackage





