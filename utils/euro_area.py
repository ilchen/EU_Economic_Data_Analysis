import pandas as pd

def load_cepr_recession_indicator(csv_path: str = './utils/CEPR_Recession_Indicator.csv') -> pd.Series:
    """
    Load the CEPR Euro Area recession indicator from CSV.
    Returns a clean DatetimeIndex Series (0/1) ready for plotting.
    """
    df = pd.read_csv(csv_path, index_col=0, sep=';', decimal=',')

    # Peak excluded matches the USRECQ-style trough method
    recession_ea = df['Peak excluded'].astype(int)

    # Convert fractional year to quarter end
    period_float = recession_ea.index.astype(float)
    years = period_float.astype(int)
    quarters = ((period_float % 1) * 4).round().astype(int) + 1

    period_idx = pd.PeriodIndex(
        years.astype(str) + "Q" + quarters.astype(str), 
        freq='Q'
    )

    recession_ea.index = period_idx.to_timestamp(how='end').normalize()
    recession_ea = recession_ea.sort_index()
    recession_ea.name = "CEPR_Recession"

    return recession_ea
