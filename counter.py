Python 3.7.7 (v3.7.7:d7c567b08f, Mar 10 2020, 02:56:16) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import numpy as np
>>> np.array()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    np.array()
TypeError: array() missing required argument 'object' (pos 1)
>>> np.array([])
array([], dtype=float64)
>>> n = np.array([])
>>> n[1] = 1
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    n[1] = 1
IndexError: index 1 is out of bounds for axis 0 with size 0
>>> 
>>> np.zeros(3,3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    np.zeros(3,3)
TypeError: data type not understood
>>> np.zero(3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    np.zero(3)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/numpy/__init__.py", line 220, in __getattr__
    "{!r}".format(__name__, attr))
AttributeError: module 'numpy' has no attribute 'zero'
>>> np.zeros(3)
array([0., 0., 0.])
>>> np.zeros((3,3))
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
>>> import pandas as pd
>>> d = pd.DataFrame(np.zeros((3,3)))
>>> d
     0    1    2
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  0.0  0.0  0.0
>>> d = pd.DataFrame(np.zeros(3))
>>> d
     0
0  0.0
1  0.0
2  0.0
>>> d[1]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/range.py", line 350, in get_loc
    return self._range.index(new_key)
ValueError: 1 is not in range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[1]
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/range.py", line 352, in get_loc
    raise KeyError(key)
KeyError: 1
>>> d[[1]]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[[1]]
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2806, in __getitem__
    indexer = self.loc._get_listlike_indexer(key, axis=1, raise_missing=True)[1]
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexing.py", line 1553, in _get_listlike_indexer
    keyarr, indexer, o._get_axis_number(axis), raise_missing=raise_missing
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexing.py", line 1640, in _validate_read_indexer
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Int64Index([1], dtype='int64')] are in the [columns]"
>>> d[0]
0    0.0
1    0.0
2    0.0
Name: 0, dtype: float64
>>> d[0,1]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 135, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 109, in pandas._libs.index.Int64Engine._check_type
KeyError: (0, 1)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d[0,1]
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/range.py", line 353, in get_loc
    return super().get_loc(key, method=method, tolerance=tolerance)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 135, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 109, in pandas._libs.index.Int64Engine._check_type
KeyError: (0, 1)
>>> d[1,]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 135, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 109, in pandas._libs.index.Int64Engine._check_type
KeyError: (1,)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[1,]
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/range.py", line 353, in get_loc
    return super().get_loc(key, method=method, tolerance=tolerance)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 135, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 109, in pandas._libs.index.Int64Engine._check_type
KeyError: (1,)
>>> d[1,0]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 135, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 109, in pandas._libs.index.Int64Engine._check_type
KeyError: (1, 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d[1,0]
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/range.py", line 353, in get_loc
    return super().get_loc(key, method=method, tolerance=tolerance)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/_libs/index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 135, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index_class_helper.pxi", line 109, in pandas._libs.index.Int64Engine._check_type
KeyError: (1, 0)
>>> d.T
     0    1    2
0  0.0  0.0  0.0
>>> d.T[1]
0    0.0
Name: 1, dtype: float64
>>> 
>>> arr = np.array(range(1,6))
>>> arr
array([1, 2, 3, 4, 5])
>>> arr = np.array(11,2,2,3)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    arr = np.array(11,2,2,3)
ValueError: only 2 non-keyword arguments accepted
>>> arr = np.array([1,2,2,2,2,1,1,3])
>>> 
>>> f
>>> d=d.T[1]
>>> for i in range(3):
	result = arr[arr==i]
	d[i] = result

	
TypeError: only size-1 arrays can be converted to Python scalars

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/series.py", line 1014, in __setitem__
    self._set_with_engine(key, value)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/series.py", line 1054, in _set_with_engine
    self.index._engine.set_value(values, key, value)
  File "pandas/_libs/index.pyx", line 96, in pandas._libs.index.IndexEngine.set_value
  File "pandas/_libs/index_class_helper.pxi", line 109, in pandas._libs.index.Int64Engine._check_type
ValueError: setting an array element with a sequence.

During handling of the above exception, another exception occurred:

TypeError: only size-1 arrays can be converted to Python scalars

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#36>", line 3, in <module>
    d[i] = result
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/series.py", line 1024, in __setitem__
    self.loc[key] = value
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexing.py", line 671, in __setitem__
    self._setitem_with_indexer(indexer, value)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexing.py", line 1065, in _setitem_with_indexer
    self.obj._data = self.obj._data.setitem(indexer=indexer, value=value)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/internals/managers.py", line 561, in setitem
    return self.apply("setitem", **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/internals/managers.py", line 442, in apply
    applied = getattr(b, f)(**kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/internals/blocks.py", line 914, in setitem
    values[indexer] = value
ValueError: setting an array element with a sequence.
>>> 
>>> d.append(2)ù
SyntaxError: invalid syntax
>>> d.append(2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    d.append(2)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/series.py", line 2582, in append
    to_concat, ignore_index=ignore_index, verify_integrity=verify_integrity
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/reshape/concat.py", line 281, in concat
    sort=sort,
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/reshape/concat.py", line 357, in __init__
    raise TypeError(msg)
TypeError: cannot concatenate object of type '<class 'int'>'; only Series and DataFrame objs are valid
>>> d[1].append(1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d[1].append(1)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/series.py", line 871, in __getitem__
    result = self.index.get_value(self, key)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 4404, in get_value
    return self._engine.get_value(s, k, tz=getattr(series.dtype, "tz", None))
  File "pandas/_libs/index.pyx", line 80, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 90, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 998, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1005, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 1
>>> d[1]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    d[1]
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/series.py", line 871, in __getitem__
    result = self.index.get_value(self, key)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/indexes/base.py", line 4404, in get_value
    return self._engine.get_value(s, k, tz=getattr(series.dtype, "tz", None))
  File "pandas/_libs/index.pyx", line 80, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 90, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 998, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1005, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 1
>>> d
0    0.0
Name: 1, dtype: float64
>>> d = DataFrame()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d = DataFrame()
NameError: name 'DataFrame' is not defined
>>> d=pd.DataFrame()
>>> d
Empty DataFrame
Columns: []
Index: []
>>> d[1] = 1
>>> d
Empty DataFrame
Columns: [1]
Index: []
>>> d = np.zeros((1,3))
>>> d
array([[0., 0., 0.]])
>>> d = pd.DataFrame(d)
>>> d
     0    1    2
0  0.0  0.0  0.0
>>> def counter(vec):
	for i in range(d):
		result = arr[arr==i]
		d[i] = result
	return d

>>> counter(arr)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    counter(arr)
  File "<pyshell#56>", line 2, in counter
    for i in range(d):
TypeError: 'DataFrame' object cannot be interpreted as an integer
>>> d[1] = 1
>>> d
     0  1    2
0  0.0  1  0.0
>>> 
>>> d = np.zeros((1,3))
>>> d = pd.DataFrame(d)
>>> 
>>> def counter(vec):
	for i in range(len(d[0])):
		result = vec[vec==i]
		d[i] = result
	return d

>>> counter(arr)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    counter(arr)
  File "<pyshell#65>", line 4, in counter
    d[i] = result
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2938, in __setitem__
    self._set_item(key, value)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 3000, in _set_item
    value = self._sanitize_column(key, value)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 3636, in _sanitize_column
    value = sanitize_index(value, self.index, copy=False)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/internals/construction.py", line 611, in sanitize_index
    raise ValueError("Length of values does not match length of index")
ValueError: Length of values does not match length of index
>>> len(d[0])
1
>>> def counter(vec):
	for i in range(3):
		result = vec[vec==i]
		d[i] = result
	return d

>>> counter(arr)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    counter(arr)
  File "<pyshell#69>", line 4, in counter
    d[i] = result
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 2938, in __setitem__
    self._set_item(key, value)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 3000, in _set_item
    value = self._sanitize_column(key, value)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/frame.py", line 3636, in _sanitize_column
    value = sanitize_index(value, self.index, copy=False)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/internals/construction.py", line 611, in sanitize_index
    raise ValueError("Length of values does not match length of index")
ValueError: Length of values does not match length of index
>>> 
>>> 
>>> l =[]
>>> arr[arr==1]
array([1, 1, 1])
>>> len(arr[arr==1])
3
>>> def counter(vec):
	for i in range(3):
		result = len(vec[vec==i])
		d[i] = result
	return d

>>> counter(arr)
   0  1  2
0  0  3  4
>>> ncol(d)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    ncol(d)
NameError: name 'ncol' is not defined
>>> d.ncol
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    d.ncol
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/core/generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'ncol'
>>> arr
array([1, 2, 2, 2, 2, 1, 1, 3])
>>> 