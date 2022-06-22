# Conda environment in Jupyter

This will show how to create customized conda environment on Mac/Linux.

## Install conda

Refer to the [user guide](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

## Create new conda env

### Python

This example shows how to create new environment called `my_env` while specify the python version you want. The packages are optional.

```bash
$ conda create --name my_env -c conda-forge python jupyterlab=3 ipykernel ipywidgets ipyleaflet numpy pandas scipy scikit-learn matplotlib seaborn tqdm shapely rasterio PyShp geopandas h5py xarray rioxarray plotly jupyterlab-git cartopy
```



### R

Install R version in conda env.



## Create kernel spec file for Jupyter (must do this inside the activated env!)

In order for Jupyter to find your kernel, run following command and optionally choose the display kernel name

```bash
(my_env) $ python -m ipykernel install --user --name my_env --display-name My-Jupyter-Env
```

## Install packages

Before you install any package, activate the new conda env just created.

```bash
$ conda activate my_env
```

Then install  `ipykernel` and other packages using `conda`

```bash
(my_env) $ conda install ipykernel numpy
```

Or using `pip`

```bash
(my_env) $ pip install matplotlib
```



## launch Jupyter

Lauch Jupyter lab and you should see you new kernel `my_env-jupyter` from the kernel dropdown.

```bash
(my_env) $ jupyter lab
# or launch the classic notebook
(my_env) $ jupyter notebook 
```

## remove a jupyter kernel

```bash
#check available kernels
jupyter kernelspec list
# remove selected kernel
jupyter kernelspec uninstall unwanted-kernel
```



###  Install Jupyterlab extentions

```bash
#check installed server extension
jupyter serverextension list
# install selected extention
conda install -c conda-forge jupyterlab-git
```



# Export Conda env

```bash
# only the main packages are exported
conda env export --from-history > environment.yml 

conda env create -f environment.yml # the env name is included in the .yml file
conda activate widget
python -m ipykernel install --user --name widget --display-name widget

jupyter labextension install @jupyter-widgets/jupyterlab-manager # enable widget
```





