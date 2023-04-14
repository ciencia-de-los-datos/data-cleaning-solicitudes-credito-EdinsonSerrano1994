"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df.dropna(subset=['tipo_de_emprendimiento','barrio','comuna_ciudadano'],inplace=True)
    df['línea_credito'] = df['línea_credito'].replace({'_':' '}, regex=True).replace({'-':' '}, regex=True)
    df['idea_negocio'] = df['idea_negocio'].replace({'_':' '}, regex=True).replace({'-':' '}, regex=True)
    df.sexo = df.sexo.str.lower()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.strip()
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace('-', ' ', regex=True).replace('_', ' ', regex=True)
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.strip()
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int).astype(str)
    df.estrato = df.estrato.astype(int).astype(str)
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    df.monto_del_credito = df.monto_del_credito.str.strip('$ ')
    df['monto_del_credito'] = df['monto_del_credito'].replace({'$ ':''}, regex=True).replace({',':''}, regex=True).astype(float).astype(int)
    df.drop_duplicates(inplace=True)

    return df
