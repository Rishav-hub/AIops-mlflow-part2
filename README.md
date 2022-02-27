Export environment to conda.yaml

```bash
conda env export > conda.yaml
```

Run mlflow in current directory
You need the conda.yaml file and MLproject file
```bash
mlflow run .
```
To run from git the repo should have the MLproject file amd conda.yaml file
```bash
mlflow run "git repo path" --no-conda
```

