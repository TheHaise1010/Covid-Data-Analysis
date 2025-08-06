import pandas as pd

def get_country_summary(df: pd.DataFrame, country: str):
    print(f"\nResumen de casos de COVID-19 en {country}")
    print(f"Casos totales: {df[country].max()}")
    print(f"Primer caso reportado: {df[country].ne(0).idxmax().date()}")
