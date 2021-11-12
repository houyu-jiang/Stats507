# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ### Author: Houyu Jiang
# ### Email: houyuj@umich.edu

# + [Topic: pd.diff()](#Topic:-pd.diff()) 
# + [Direction of the difference](#Direction-of-the-difference)
# + [Distance of difference](#Distance-of-difference)

# ## Topic: pd.diff()
#
# - ```pd.diff()``` is a pandas method that we could use to
# compute the difference between rows or columns in DataFrame.
# - We could import it through ```import pandas as pd```.
# - Suppose ```df``` is a pandas DataFrame, we could use 
# ```diff``` method to compute.

df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6],
                   'b': [1, 1, 2, 3, 5, 8],
                   'c': [1, 4, 9, 16, 25, 36]})
df.diff(axis=0)

# ## Direction of the difference
# - ```pd.diff()``` by default would calculate the 
# difference between different rows.
# - We could let it compute the difference between 
# previous columns by setting ```axis=1```

df.diff(axis=1)

# ## Distance of difference
# - ```pd.diff()``` by default would calculate the difference
# between this row/column and previous row/column
# - We could let it compute the difference between this row/column
# and the previous n row/column by setting ```periods=n```

df.diff(periods=3)

