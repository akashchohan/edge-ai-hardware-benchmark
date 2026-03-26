import time
import torch
import numpy as np
from models.mobilenet_test import load_model

model = load_model()

dummy_input = torch.randn(1, 3, 224, 224)

runs = 50
times = []

for _ in range(runs):
    start = time.time()
    with torch.no_grad():
        output = model(dummy_input)
    end = time.time()
    times.append(end - start)

print("Average inference time:", np.mean(times))