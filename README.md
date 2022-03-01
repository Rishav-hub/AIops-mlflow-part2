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

To run command for presiction in WIndows
```bash
curl -X POST -H "Content-Type:application/json; format=pandas-split" --data "{\"columns\":[\"alcohol\", \"chlorides\", \"citric acid\", \"density\", \"fixed acidity\", \"free sulfur dioxide\", \"pH\", \"residual sugar\", \"sulphates\", \"total sulfur dioxide\", \"volatile acidity\"],\"data\":[[12.8, 0.029, 0.48, 0.98, 6.2, 29, 3.33, 1.2, 0.39, 75, 0.66]]}" http://127.0.0.1:1234/invocations
```
To run command for presiction On Linux and macOS
```bash
curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["alcohol", "chlorides", "citric acid", "density", "fixed acidity", "free sulfur dioxide", "pH", "residual sugar", "sulphates", "total sulfur dioxide", "volatile acidity"],"data":[[12.8, 0.029, 0.48, 0.98, 6.2, 29, 3.33, 1.2, 0.39, 75, 0.66]]}' http://127.0.0.1:1234/invocations
```

Postman -:
![image](https://user-images.githubusercontent.com/57321948/156178176-76a9aa48-0a7b-4159-8259-3265a943d346.png)
