from src.load_data import load_csv
from src.clean_data import transform_data
from src.analyze import get_country_summary
from src.visualize import plot_country_trend

if __name__ == '__main__':
    df_raw = load_csv("data/time_series_covid19_confirmed_global.csv")
    df_clean = transform_data(df_raw)

    # Análisis para algunos países
    countries = ['Italy', 'Spain', 'US', 'Brazil']

    for country in countries:
        get_country_summary(df_clean, country)

    # Graficar
    plot_country_trend(df_clean, countries)
