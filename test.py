from proofzero_sdk.util import *

#export
import pandas as pd
import itertools
import functools
from typing import Callable, NewType

# The `TokenFrame` type is a wrapper around a `pandas` DataFrame that represents a DataFrame that has been tokenized using the `tokenize` function.
TokenFrame = NewType('TokenFrame', pd.DataFrame)

def tokenize(
    df: pd.DataFrame, schema: dict, suffix_delim: str = ""
) -> TokenFrame:
    """
    Takes a `pandas` DataFrame and a schema. The schema is a `dict` that maps columns in the DataFrame to a list of parsers that are executed in order.
    
    Denormalizes the passed DataFrame by applying the parsers in the schema.
    
    Returns the denormalized DataFrame.
    """
    def map_schema(map_row, map_schema, map_delim):
        results = [
            functools.reduce(
                lambda data, fxn: fxn(data), map_schema[i], map_row[i]
            )
            for i in map_row.index
        ]
        print(results)
        indicies = [
            # Allow parsers to return a named component and use that name to index
            # our new columns, else use the index number as a string.
            map_delim.join(
                [map_row.index[i], v[0] if isinstance(v, tuple) else str(j)]
            )
            for i, u in enumerate(map_row.index)
            for j, v in enumerate(results[i])
        ]
        print('got indicies')
        series = pd.Series(
            data=list(itertools.chain(*results)), index=indicies
        )
        print('got series')
        return series

    return pd.concat(
        [
            df,
            df.apply(
                map_schema,
                axis=1,
                args=(schema, suffix_delim),
                result_type="expand",
            ),
        ],
        axis=1,
    )

from proofzero_sdk.core import load

data = load('./data.csv')
print(tokenize(data[:1], schema={
    'acct_num': [parseString],
    'name': [parseName],
    'address': [parseAddress],
    'phone': [parsePhone],
    'SIN': [parseSIN],
    'DOB': [parseDate]
}))
