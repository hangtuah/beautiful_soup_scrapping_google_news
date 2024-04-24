import pandas as pd

def create_dataframe(data, columns=None):
    """Create a DataFrame from a list of data."""
    return pd.DataFrame(data, columns=columns)

def check_duplicates(df, column_name):
    """Check and report any duplicates in a specified column."""
    return df[column_name].duplicated().sum()

def export_dataframe(df, filename):
    """Export DataFrame to CSV, without the index."""
    df.to_csv(filename, index=False)

