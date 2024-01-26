import numpy as np
v = np.random.uniform(1,20, 20)
print(v)

v = v.reshape(4, 5)
print(v)

vec = np.where(v == np.max(v, axis=1,keepdims=True), 0, v)
print(v)