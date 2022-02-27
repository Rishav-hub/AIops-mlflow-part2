Export environment to conda.yaml

```bash
conda env export > conda.yaml
```

Run mlflow in current directory
You need the conda.yaml file and MLproject file
```bash
mlflow run .
```

