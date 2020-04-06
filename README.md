# Repo for using in a Kaggle notebook
This is an example of how to import a Python module that is saved in a GitHub repo into a Kaggle notebook (aka "kernel").

The accompanying notebook, including further instructions, is here: <https://www.kaggle.com/btw78jt/try-out-kaggle>.

## Further notes
### Downloading Kaggle datasets
This can be done using the Kaggle CLI (which sends commands to the Kaggle API). Specific notes:
- To download using the Kaggle Python package (*not* the Kaggle CLI): <https://stackoverflow.com/a/54869077>. But this does not load into memory, so not that good.
- Using the Kaggle API, you can download a subsample of the files <https://github.com/Kaggle/kaggle-api#download-dataset-files>. First `kaggle datasets files -v [dataset]` to get a list of the files in CSV format.
