import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Eliminar columnas innecesarias
    df = df.drop(['Lat', 'Long', 'Province/State'], axis=1, errors='ignore')

    # Agrupar por país y sumar los casos
    df = df.groupby('Country/Region').sum()

    # Transponer: fechas como filas
    df = df.transpose()

    # Convertir el índice (que ahora son fechas tipo string) a datetime
    df.index = pd.to_datetime(df.index, format='%m/%d/%y')

    return df
