from typing import List

import numpy as np
import pandas as pd

from pypher.errors import ExecutionError
from pypher.functions.numeric_fns import _wrap_simple_fn


def pi(params: List[pd.Series], table: pd.DataFrame) -> pd.Series:
    if len(params) != 0:
        raise ExecutionError("Incorrect argument count")
    return pd.Series([np.pi] * len(table), dtype=float)


fn_map = {
    "acos": _wrap_simple_fn(np.arccos),
    "asin": _wrap_simple_fn(np.arcsin),
    "atan": _wrap_simple_fn(np.arctan),
    "atan2": _wrap_simple_fn(np.arctan2),
    "cos": _wrap_simple_fn(np.cos),
    "cot": _wrap_simple_fn(lambda x: 1 / np.tan(x)),
    "degrees": _wrap_simple_fn(np.rad2deg),
    "pi": pi,
    "radians": _wrap_simple_fn(np.deg2rad),
    "sin": _wrap_simple_fn(np.sin),
    "tan": _wrap_simple_fn(np.tan),
}
