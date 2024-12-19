import pandas as pd

data = pd.DataFrame({
    "A": [1, 1, 1],
    "B": [1, 2, 3]
})

print(data.columns[data.nunique() <= 1])