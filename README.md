# proofzero_sdk
> A parsing-hasher client to the Proof Zero matching system.


This file will become your README and also the index of your documentation.

## Install

Within your python environment:

```bash
tar -xvf proofzero_sdk.tar.bz2
pip install ./proofzero_sdk
```

## How to use

Import the code into your `.py` file or Jupyter notebook:

```python
import proofzero_sdk.core as p0
import proofzero_sdk.util as p1
```

### Load your data

```python
data = p0.load('./data.csv')
data[:1]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>acct_num</th>
      <th>name</th>
      <th>address</th>
      <th>phone</th>
      <th>SIN</th>
      <th>DOB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PXCG66212484637575</td>
      <td>Kristin Sanchez MD</td>
      <td>31417 Gina Lodge, Bradleytown, MB P7G 4N5</td>
      <td>1 (598) 742-6794</td>
      <td>203 268 552</td>
      <td>1943-04-15</td>
    </tr>
  </tbody>
</table>
</div>


