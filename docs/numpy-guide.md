# NumPy guide

NumPy provides efficient n-dimensional arrays and vectorized numeric operations. Arrays are useful when many values share a type and the same operation should be applied across them.

```python
import numpy as np

temperatures = np.array([16.2, 17.8, 15.4])
print(temperatures.mean())
print(temperatures[temperatures >= 17])
```

Compared with a Python list, an array supports element-wise arithmetic and compact numeric storage. Learn array creation, shape, indexing, boolean masks, broadcasting, and missing or non-finite values.

Install it when needed with `py -m pip install numpy`. For labeled tables and mixed column types, see the [pandas guide](pandas-guide.md).
