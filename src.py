import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def eliminar_duplicados(df):
    '''
    Identifica y elimina los duplicados de un DataFrame. 
    Devuelve el número de filas duplicadas y las que ha eliminado.
    ----------
    Parameters
    df : pandas.core.frame.DataFrame
    ----------
    Returns
    text : str
    '''
    if df.duplicated().sum()>0:
        print('¡Hay registros duplicados en tu DataSet!')
        print(f'Se han detectado {df.duplicated().sum} registros duplicados')
        df= df.drop_duplicates()
        print('Eliminando...')
        print('¡Enhorabuena! No hay duplicados en el DataFrame')
        print(f'Número de registros duplicados:{df.duplicated().sum()}')
    else:
        print('¡Enhorabuena! No hay duplicados en el DataFrame')

def porcentaje_nulos(df):
    '''
    Identifica el porcentaje de nulos por columna de un DataFrame.
    Devuelve un listado con la información de nulos por columnas.
    ----------
    Parameters
    df : pandas.core.frame.DataFrame
    ----------
    Returns
    serie : pandas.core.series.Series
    '''
    return df.isna().sum()/len(df)

def eliminar_nulos(df):
    '''
    Identifica la cantidad de nulos y los elimina.
    Devuelve información sobre el DataFrame.
    ----------
    Parameters
    df : pandas.core.frame.DataFrame
    ----------
    Returns
    text : str
    '''
    if df.isnull().sum().sum()>1:
        print('¡Hay nulos en tu DataSet! Inicialmente esta compuesto por:')
        print(f'{df.shape[0]} filas y {df.shape[1]} columnas')
        print(f'Se han encontrado un total de {df.isnull().sum().sum()} nulos')
        df.dropna(inplace=True)
        print(' \n Eliminando... \n ')
        print(f'Tras eliminar los nulos hay un total de {df.isnull().sum().sum()} nulos. \n')
        print('El DataSet sin nullos ahora esta compuesto por:')
        print(f'{df.shape[0]} filas y {df.shape[1]} columnas')
    else:
        '¡Enhorabuena! No hay nulos en tu DataFrame y esta compuesto por:'
        f'{df.shape[0]} filas y {df.shape[1]} columnas'

def eliminar_columnas(df,lst):
    '''
    Elimina las columnas de un DataFrame
    Requiere del nombre del DataFrame y el nombre de las columnas a eliminar en una lista.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    lst : list

    Returns
    -------
    df : pandas.core.frame.DataFrame
    '''
    df.drop(lst, axis=1, inplace=True)
    return df

def renombrar_columnas(df,dict):
    '''
    Cambia los nombres de las columnas de un DataFrame.
    Requiere de un diccionario, ejemplo:
    { nombre_column1 : nuevo_nombre_columna1 , nombre_column2 : nuevo_nombre_columna2 , ...}

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    dict : dict -> Diccionario con los nombres originales a cambiar como keys y con los nombres modificados como values.

    Returns
    -------
    df : pandas.core.frame.DataFrame
    '''
    df.rename(dict, axis=1, inplace=True)
    return df

def miles_to_km(df,serie1,serie2):
    '''
    Realiza la conversión de valores de millas terrestres a kilometros.
    Devuelve una serie con el valor en kilometros y la añade como columna en el DataFrame.
    Se introduce el DataFrame (df), la nueva columna (serie1) en kilometros y la columna a convertir (serie2) en millas.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    serie1 : pandas.core.series.Serie -> Serie con el valor en kilometros.
    serie2 : pandas.core.series.Serie -> Serie con el valor en millas.

    Returns
    -------
    serie1 : pandas.core.series.Series -> Serie con el valor en kilometros.
    '''
    df[serie1]=df[serie2].apply(lambda x: round(x*1.60934,3))
    return df

def trip_time_h(df,serie1,serie2,serie3):
    ''''
    Calcula el tiempo en horas entre dos fechas o dos tiempos.
    Devuelve una serie con el valor en horas y la añade como columna en el DataFrame.
    Se introduce el DataFrame (df), la fecha 

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    serie1 : pandas.core.series.Serie -> Serie con el valor de tiempo en horas.
    serie2 : pandas.core.series.Serie -> Serie con el valor de pickupdatetime .
    serie3 : pandas.core.series.Serie -> Serie con el valor en dropoffdatetime.

    Returns
    -------
    serie1 : pandas.core.series.Series -> Serie con el valor de tiempo en horas.
    '''
    lista_horas=[]
    for i in range(0,df.shape[0]):
        try:
            lista_horas.append(round((df.iloc[i][serie2]-df.iloc[i][serie3]).total_seconds()/3600,3))
        except:
            serie1.append(np.nan)
    df[serie1]=lista_horas
    return df[serie1]

def average_speed_kmh(df,serie1,serie2,serie3):
    '''
    Calcula el tiempo el tiempo medio de trayecto en km/h.
    Devuelve las cinco primeras columnas del DataFrame para su comprobación.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    serie1 : pandas.core.series.Serie -> Serie con el valor de velocidad media en km/h.
    serie2 : pandas.core.series.Serie -> Serie con el valor de la distancia en km.
    serie3 : pandas.core.series.Serie -> Serie con el valor del tiempo en h.

    Returns
    -------
    df : pandas.core.frame.DataFrame
    '''
    df[serie1]=round(df[serie2]/df[serie3],1)
    return df.head()

def dtype_datetime64(df,lst):
    '''
    Transforma el tipo de dato a datetime64[ns].
    Requiere de una lista con el nombre de las columnas a transformar.
    Devuelve información sobre los tipos de las columnas del DataFrame.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    lst : list

    Returns
    -------
    df.info() : Nontype
    '''
    for i in lst:
        df[i]=pd.to_datetime(df[i])
    return df.info()

def columns_year_month_weekday(df,serie1):
    '''
    Obtiene el año, el mes, el dia de la semana y la hora de una fecha completa (datetime)
    Genera 4 nuevas series y las introduce en el DataFrame.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    serie1 : pandas.core.series.Serie -> Serie con el valor de fecha inicial.

    Returns
    -------
    df : pandas.core.frame.DataFrame
    '''
    df['year']=df[serie1].apply(lambda x: x.year)
    df['month']=df[serie1].apply(lambda x: x.month)
    df['day']=df[serie1].apply(lambda x: x.weekday())
    df['hour']=df[serie1].apply(lambda x: x.hour)
    return df.head()

def df_filter(df,año,mes):
    '''
    Filtra el DataFrame según los siguientes parámetros variables y fijos:
    - Según el valor de año introducido en el parámtro año.
    - Según el mes introducido en el parámetro mes.
    - Número de pasajeros superior a cero e inferior a 5.
    - Distancia del trayecto superior a 100 metros.
    - Cantidad total de trayecto superior a $0.

    Devuelve el DataFrame con el filtro aplicado.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    año : int 
    mes : str

    Returns
    -------
    df : pandas.core.frame.DataFrame
    '''
    df=df[(df['year']==año) & (df['month']==mes) & (df['passenger_count']<=4) &(df['passenger_count']>0) & (df['trip_distance_km']>0.100) & (df['total_amount']>0)]
    return df

def df_filter2(df,min_speed,max_speed,min_trip_time_h):
    '''
    Filtra el DataFrame según los parámetros introducidos:
    - min_speed, velocidad mínima en km/h.
    - max_speed, velodidad máxima en km/h.
    - min_trip_time_h, duración mínima del tiempo de trayecto en horas.

    Devuelve el DataFrame para obervar los cambios.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    min_speed : int
    max_speed : int
    min_trip_time_h : int

    Returns
    -------
    df : pandas.core.frame.DataFrame
    '''
    df=df[(df['average_speed_kmh']>min_speed) & (df['average_speed_kmh']<max_speed) & (df['trip_time_h']>min_trip_time_h)]
    return df

def day_replace(df,serie,dictionary):
    '''
    Transforma los dias de la semana en formato numérico a formato escrito.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    serie : pandas.core.series.Serie -> Serie con el valor numerico del dia de la semana.
    dictionary : dict -> Diccionario con la conversión de valor numérico a valor escrito.
    
    Returns
    -------
    serie : pandas.core.series.Serie -> Serie con el valor numerico del dia de la semana.
    '''
    for i,j in dictionary.items():
        if i in dictionary:
            df[serie].replace(i,j,inplace=True)
    return df[serie]

def month_replace(df,serie,dictionary):
    '''
    Transforma los meses del año de formato numérico a formato escrito.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    serie : pandas.core.series.Serie -> Serie con el valor numérico del mes del año.
    dictionary : dict -> Diccionario con la conversión de valor numérico a valor escrito.
    
    Returns
    -------
    serie : pandas.core.series.Serie -> Serie con el valor numérico del mes del año.
    '''
    for i,j in dictionary.items():
        if i in dictionary:
            df[serie].replace(i,j,inplace=True)
    return df[serie]

def dtype_int(df,lst):
    for i in lst:
        df[i]=df[i].apply(lambda x: int(x))
    return df.info()

def dtype_str(df,lst):
    for i in lst:
        df[i]=df[i].apply(lambda x: str(x))
    return df.info()

def vendorID_replace(df,serie,dictionary):
    for i,j in dictionary.items():
        if i in dictionary:
            df[serie].replace(i,j,inplace=True)
    return df[serie]

def RatecodeID_replace(df,serie,dictionary):
    for i,j in dictionary.items():
        if i in dictionary:
            df[serie].replace(i,j,inplace=True)
    return df[serie]

def payment_type_replace(df,serie,dictionary):
    for i,j in dictionary.items():
        if i in dictionary:
            df[serie].replace(i,j,inplace=True)
    return df[serie]

def TLC_Zone(df,serie1,serie2,ls1,ls2,ls3,ls4,ls5):
    lista=[]
    for i in range(0,df.shape[0]):
        if df.iloc[i][serie1] in ls1:
            lista.append('Bronx')
        elif df.iloc[i][serie1] in ls2:
            lista.append('Brooklyn')
        elif df.iloc[i][serie1] in ls3:
            lista.append('Manhattan')
        elif df.iloc[i][serie1] in ls4:
            lista.append('Queens')
        elif df.iloc[i][serie1] in ls5:
            lista.append('Staten_Island')
        else:
            lista.append('Unknown')
    df[serie2]=pd.Series(lista)
    return df[serie2]

def sum_strings(df,serie1,serie2,serie3):
    df[serie1]=df[serie2]+'-'+df[serie3]
    return df[serie1]

def reset_index(df,serie1):
    df=df.reset_index()
    del df[serie1]
    return df

def basic_info_stats(df,lista):
    '''
    Devuelve información estadistica básica de un conjunto de columnas (series).
    Debe introducirse una lista con el nombre de las columnas (series) a analizar.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    lista : list
    
    Returns
    -------
    string : str 
    '''
    for i in lista:
        Media=df[i].mean()
        Mediana=df[i].median()
        Mínimo=df[i].min()
        Máximo=df[i].max()
        std_dev=df[i].std()
        print(f'Datos estadísticos de la variable {i}:')
        print('Calculando...')
        print(f'Desviación estándard: {round(std_dev,3)}')
        print(f'Media: {round(Media,3)}')
        print(f'Mediana: {Mediana}')
        print(f'Mínimo: {Mínimo}')
        print(f'Máximo: {Máximo} \n')

def stats_info(df,lista):
    '''
    Devuelve información estadistica de un conjunto de columnas (series).
    Debe introducirse una lista con el nombre de las columnas (series) a analizar.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    lista : list
    
    Returns
    -------
    string : str 
    '''
    for i in lista:
        Q1=df[i].quantile(0.25)
        Q3=df[i].quantile(0.75)
        IQR=round(Q3-Q1,3)
        outlier_sup=(Q3+1.5*IQR)
        outlier_inf=(Q1-1.5*IQR)
        Media=df[i].mean()
        Mediana=df[i].median()
        Mínimo=df[i].min()
        Máximo=df[i].max()
        std_dev=df[i].std()
        print(f'Datos estadísticos de la variable {i}:')
        print('Calculando...')
        print(f'Desviación estándard: {round(std_dev,3)}')
        print(f'Primer Cuartil -> Q1: {Q1}')
        print(f'Tercer Cuartil -> Q3: {Q3}')
        print(f'Rango intercuartilico (IQR): {IQR}')
        print(f'Se considera outlier valores superiores a {round(outlier_sup,3)} e inferior a {round(outlier_inf,3)}')
        print(f'Media: {round(Media,3)}')
        print(f'Mediana: {Mediana}')
        print(f'Mínimo: {Mínimo}')
        print(f'Máximo: {Máximo} \n')

def drop_outliers(df,serie):
    '''
    Devuelve información estadistica de una columna (serie)
    
    Transforma los meses del año de formato numérico a formato escrito.
    Limpia el DataFrame de outliers mediante su IQR, valor usado: media+-1.5*IQR.
    
    Parameters
    ----------
    df : pandas.core.frame.DataFrame
    serie : pandas.core.series.Serie
    
    Returns
    -------
    df : pandas.core.frame.DataFrame 
    '''
    Q1=df[serie].quantile(0.25)
    Q3=df[serie].quantile(0.75)
    IQR=Q3-Q1
    Media=df[serie].mean()
    Mediana=df[serie].median()
    Mínimo=df[serie].min()
    Máximo=df[serie].max()
    std_dev=df[serie].std()
    print(f'Datos estadísticos iniciales de la variable {serie}:')
    print('Calculando...')
    print(f'Primer Cuartil -> Q1: {Q1}')
    print(f'Tercer Cuartil -> Q3: {Q3}')
    print(f'Rango intercuartilico (IQR): {IQR}')
    print(f'Desviación estándard: {round(std_dev,3)}')
    print(f'Media: {Media}')
    print(f'Mediana: {Mediana}')
    print(f'Mínimo: {Mínimo}')
    print(f'Máximo: {Máximo} \n')
    BI_Calculado=(Q1-1.5*IQR)
    BS_Calculado=(Q3+1.5*IQR)
    print('Bigote superior e inferior:')
    print('Calculando...')
    print(f'Valor de bigote superior: {BS_Calculado}')
    print(f'Valor de bigote inferior: {BI_Calculado}')
    df=df[(df[serie]<BS_Calculado) & (df[serie]>BI_Calculado)]
    plt.title(serie)
    plt.boxplot(df[serie], vert=False)
    plt.show()
    Q1=df[serie].quantile(0.25)
    Q3=df[serie].quantile(0.75)
    IQR=Q3-Q1
    Media=df[serie].mean()
    Mediana=df[serie].median()
    Mínimo=df[serie].min()
    Máximo=df[serie].max()
    std_dev=df[serie].std()
    print(f'Datos estadísticos tras filtrar outliers de la variable {serie}:')
    print('Calculando...')
    print(f'Primer Cuartil -> Q1: {Q1}')
    print(f'Tercer Cuartil -> Q3: {Q3}')
    print(f'Rango intercuartilico (IQR): {IQR}')
    print(f'Desviación estándard: {round(std_dev,3)}')
    print(f'Media: {Media}')
    print(f'Mediana: {Mediana}')
    print(f'Mínimo: {Mínimo}')
    print(f'Máximo: {Máximo} \n')
    return df