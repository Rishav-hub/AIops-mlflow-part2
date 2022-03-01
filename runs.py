import os
import mlflow
import numpy as np

alphas = np.linspace(0.1,1.0, 5)
l1_ratios = np.linspace(0.1,1.0, 5)


for p1 in alphas:
    for p2 in l1_ratios:
        print(f"Logging experiment for p1 = {p1} and p2 = {p2}")
        os.system(f"python demo.py -a {p1} -l1 {p2}")