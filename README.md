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
data = p0.load('./data_1.csv')
data[:1]
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-2-12a7d7157c2d> in <module>
    ----> 1 data = p0.load('./data.csv')
          2 data[:1]


    ~/Projects/p0/proofzero_sdk/proofzero_sdk/core.py in load(filename)
          9     Convenience function for loading files using `pandas`. Full version supports XLSX, etc.
         10     """
    ---> 11     return pd.read_csv(filename)
         12 
         13 # Cell


    ~/Projects/p0/proofzero_sdk/venv/lib/python3.7/site-packages/pandas/io/parsers.py in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)
        608     kwds.update(kwds_defaults)
        609 
    --> 610     return _read(filepath_or_buffer, kwds)
        611 
        612 


    ~/Projects/p0/proofzero_sdk/venv/lib/python3.7/site-packages/pandas/io/parsers.py in _read(filepath_or_buffer, kwds)
        460 
        461     # Create the parser.
    --> 462     parser = TextFileReader(filepath_or_buffer, **kwds)
        463 
        464     if chunksize or iterator:


    ~/Projects/p0/proofzero_sdk/venv/lib/python3.7/site-packages/pandas/io/parsers.py in __init__(self, f, engine, **kwds)
        817             self.options["has_index_names"] = kwds["has_index_names"]
        818 
    --> 819         self._engine = self._make_engine(self.engine)
        820 
        821     def close(self):


    ~/Projects/p0/proofzero_sdk/venv/lib/python3.7/site-packages/pandas/io/parsers.py in _make_engine(self, engine)
       1048             )
       1049         # error: Too many arguments for "ParserBase"
    -> 1050         return mapping[engine](self.f, **self.options)  # type: ignore[call-arg]
       1051 
       1052     def _failover_to_python(self):


    ~/Projects/p0/proofzero_sdk/venv/lib/python3.7/site-packages/pandas/io/parsers.py in __init__(self, src, **kwds)
       1865 
       1866         # open handles
    -> 1867         self._open_handles(src, kwds)
       1868         assert self.handles is not None
       1869         for key in ("storage_options", "encoding", "memory_map", "compression"):


    ~/Projects/p0/proofzero_sdk/venv/lib/python3.7/site-packages/pandas/io/parsers.py in _open_handles(self, src, kwds)
       1366             compression=kwds.get("compression", None),
       1367             memory_map=kwds.get("memory_map", False),
    -> 1368             storage_options=kwds.get("storage_options", None),
       1369         )
       1370 


    ~/Projects/p0/proofzero_sdk/venv/lib/python3.7/site-packages/pandas/io/common.py in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        645                 encoding=ioargs.encoding,
        646                 errors=errors,
    --> 647                 newline="",
        648             )
        649         else:


    FileNotFoundError: [Errno 2] No such file or directory: './data.csv'

