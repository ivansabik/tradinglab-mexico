import datetime
import pandas as pd
import pandas.io.data

empresas = pd.read_csv('../empresas_bmv.csv')
empresas = list(empresas['clave_yahoo'].values)

print empresas

datos_consolidados = pd.DataFrame()

for empresa in empresas:
    if(empresa != 'NONEXISTUM.NA'):
        datos = pd.io.data.get_data_yahoo(empresa, 
                                         start=datetime.datetime(2006, 10, 1), 
                                         end=datetime.datetime(2012, 1, 1))
        datos['clave_empresa'] = empresa
        print empresa
        print datos.head()
        datos_consolidados = datos_consolidados.append(datos)
        datos.to_csv('./csv/' + empresa + '.csv')
print datos_consolidados.head()
datos_consolidados.to_csv('./historicos-bmv.csv')

