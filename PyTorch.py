import numpy as np
import pandas as pd
import torch

# Приклад роботи з numpy
array = np.array([1, 2, 3, 4, 5])
print("Numpy array:", array)

# Приклад роботи з pandas
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 23, 45]}
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)

# Приклад роботи з PyTorch
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
result = torch.matmul(x, y)
print("PyTorch matrix multiplication result:")
print(result)
