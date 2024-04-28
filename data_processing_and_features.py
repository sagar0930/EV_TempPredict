import pandas as pd

def convert_dtpye(df):
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

#there very few values were null so we removed those records instead of imputation.
def null_value_imputation(df):
    df=df[~(df['motor_speed'].isna())&~(df['u_d'].isna())&~(df['i_q'].isna())]
    return df
