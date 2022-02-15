import numpy as np
import pandas as pd
import datetime
import yfinance as yf
import warnings

naftrac = pd.read_csv('files/NAFTRAC_holdings.csv')

def Unique_counts(data: "Data Frame que se va a utilizar", 
                  name: "Nombre (entre comillas) de la columna del que se quieren los valores únicos",
                  cantidad: "Cantidad de veces a mostrar"):
    
    u_v1 = data[name]
    unique, counts = np.unique(u_v1, return_counts=True)
    a = pd.DataFrame(columns=("Unique","Values"))
    a["Unique"] = unique
    a["Values"] = counts
    
    for i in range(len(a)):
        if a['Values'][i] < cantidad:
            a = a.drop([i],axis=0)
    
    a.reset_index(inplace=True, drop=True)
    
    return pd.DataFrame(a)


def nuevo_DataFrame(data: "Data Frame que se va a utilizar",
                    name: "Nombre (entre comillas) de la columna del que se quieren los valores únicos",
                    cantidad: "Cantidad de veces a mostrar",
                    columna_fecha: "Columna donde se encuentra la fecha (entre comillas)",
                    tikers: "Columna donde se encuentran los tickers (entre comillas)"):
    
    valores_unicos = Unique_counts(data,name,cantidad)
    
    a = []
    for i in range(len(data)):
        if data[name][i] in list(valores_unicos["Unique"]):
            a.append(data.iloc[i])
    i = i+1
    
    a = pd.DataFrame(a)
    
    filtro = a["Clase de activo"] != "Cash"
    a = a[filtro]
    filtro2 = a["Ticker"] != "TLEVISAC"
    a = a[filtro2]
    filtro3 = a["Ticker"] != "LIVEPOLC.1"
    a = a[filtro3]
    filtro4 = a["Ticker"] != "MEGAC"
    a = a[filtro4]
    filtro5 = a["Ticker"] != "KOFUBL"
    a = a[filtro5]
    
    
    a[columna_fecha] = pd.to_datetime(a[columna_fecha],infer_datetime_format=True)
    
    a[tikers] = a[tikers]+[".MX"]
    
    a.reset_index(inplace=True, drop=True)
    
    warnings.filterwarnings('ignore')
    warnings.warn('DelftStack')
    warnings.warn('Do not show this message')
    
    return a


def precios (data: "Data Frame que se va a utilizar",
            name: "Nombre (entre comillas) de la columna del que se quieren los valores únicos",
            cantidad: "Cantidad de veces a mostrar",
            columna_fecha: "Columna donde se encuentra la fecha (entre comillas)",
            tikers: "Columna donde se encuentran los tickers (entre comillas)"):
    
    df_limpio = nuevo_DataFrame(data,name,cantidad,columna_fecha,tikers)
    fechas = pd.to_datetime(df_limpio["Fecha"].unique().tolist())
    tickers = df_limpio["Ticker"].unique().tolist()
    a = pd.DataFrame()
    
    for i in range(len(fechas)):
        
        precios = yf.download(tickers,start=fechas[i])
        
        a = a.append(precios["Open"].iloc[0])
        
        i+1
    
    return a

naftrac_limpio = nuevo_DataFrame(naftrac,"Nombre",25,"Fecha","Ticker")
precio = precios(naftrac,"Nombre",25,"Fecha","Ticker") 

def inicial():
    capital = 1000000
    comision = 0.00125
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    
    capital = ((capital*peso[0]*(1 + comision)) + (capital*peso[1]*(1 + comision)) + (capital*peso[2]*(1 + comision)) + (capital*peso[3]*(1 + comision)) + (capital*peso[4]*(1 + comision)) + (capital*peso[5]*(1 + comision)) + (capital*peso[6]*(1 + comision)) + (capital*peso[7]*(1 + comision)) + (capital*peso[8]*(1 + comision)) + (capital*peso[9]*(1 + comision)) + (capital*peso[10]*(1 + comision)) + (capital*peso[11]*(1 + comision)) + (capital*peso[12]*(1 + comision)) + (capital*peso[13]*(1 + comision)) + (capital*peso[14]*(1 + comision)) + (capital*peso[15]*(1 + comision)) + (capital*peso[16]*(1 + comision)) + (capital*peso[17]*(1 + comision)) + (capital*peso[18]*(1 + comision)) + (capital*peso[19]*(1 + comision)) + (capital*peso[20]*(1 + comision)) + (capital*peso[21]*(1 + comision)) + (capital*peso[22]*(1 + comision)) + (capital*peso[23]*(1 + comision)))
    
    return capital


def enero20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[0][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def febrero20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[1][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def marzo20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[2][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def abril20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[3][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def mayo20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[4][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def junio20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[5][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def julio20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[6][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def agosto20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[7][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def septiembre20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[8][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def octubre20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[9][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def noviembre20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[10][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def diciembre20():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[11][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def enero21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[12][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def febrero21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[13][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def marzo21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[14][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def abril21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[15][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def mayo21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[16][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def junio21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[17][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def julio21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[18][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def agosto21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[19][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def septiembre21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[20][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def octubre21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[21][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def noviembre21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[22][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def diciembre21():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[23][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def enero22():
    suma = []
    x = naftrac_limpio[0:24].sort_values("Ticker")
    x.reset_index(inplace=True, drop=True)
    peso = x["Peso (%)"][0:24]/100
    for i in range(len(peso)):
        i = 0
        b = precio.iloc[24][i] * peso[i] * float(x["Acciones"][i].replace(",",""))
        suma.append(b)
        i+1
        
    a = b.sum()
    
    return a

def rendimiento1():
    rendimiento = [0]
    rendimiento.append((febrero20()-enero20())/febrero20())
    rendimiento.append((marzo20()-febrero20())/marzo20())
    rendimiento.append((abril20()-marzo20())/abril20())
    rendimiento.append((mayo20()-abril20())/mayo20())
    rendimiento.append((junio20()-mayo20())/junio20())
    rendimiento.append((julio20()-junio20())/julio20())
    rendimiento.append((agosto20()-julio20())/agosto20())
    rendimiento.append((septiembre20()-agosto20())/septiembre20())
    rendimiento.append((octubre20()-septiembre20())/octubre20())
    rendimiento.append((noviembre20()-octubre20())/noviembre20())
    rendimiento.append((diciembre20()-noviembre20())/diciembre20())
    rendimiento.append((enero21()-diciembre20())/enero21())
    
    rendimiento.append((febrero21()-enero21())/febrero21())
    rendimiento.append((marzo21()-febrero21())/marzo21())
    rendimiento.append((abril21()-marzo21())/abril21())
    rendimiento.append((mayo21()-abril21())/mayo21())
    rendimiento.append((junio21()-mayo21())/junio21())
    rendimiento.append((julio21()-junio21())/julio21())
    rendimiento.append((agosto21()-julio21())/agosto21())
    rendimiento.append((septiembre21()-agosto21())/septiembre21())
    rendimiento.append((octubre21()-septiembre21())/octubre21())
    rendimiento.append((noviembre21()-octubre21())/noviembre21())
    rendimiento.append((diciembre21()-noviembre21())/diciembre21())
    rendimiento.append((enero22()-diciembre21())/enero22())
    
    capital = [inicial()+180000]
    capital.append(capital[0] + capital[0]*rendimiento[1])
    capital.append(capital[1] + capital[1]*rendimiento[2])
    capital.append(capital[2] + capital[2]*rendimiento[3])
    capital.append(capital[3] + capital[3]*rendimiento[4])
    capital.append(capital[4] + capital[4]*rendimiento[5])
    capital.append(capital[5] + capital[5]*rendimiento[6])
    capital.append(capital[6] + capital[6]*rendimiento[7])
    capital.append(capital[7] + capital[7]*rendimiento[8])
    capital.append(capital[8] + capital[8]*rendimiento[9])
    capital.append(capital[9] + capital[9]*rendimiento[10])
    capital.append(capital[10] + capital[10]*rendimiento[11])
    capital.append(capital[11] + capital[11]*rendimiento[12])
    
    capital.append(capital[12] + capital[12]*rendimiento[13])
    capital.append(capital[13] + capital[13]*rendimiento[14])
    capital.append(capital[14] + capital[14]*rendimiento[15])
    capital.append(capital[15] + capital[15]*rendimiento[16])
    capital.append(capital[16] + capital[16]*rendimiento[17])
    capital.append(capital[17] + capital[17]*rendimiento[18])
    capital.append(capital[18] + capital[18]*rendimiento[19])
    capital.append(capital[19] + capital[19]*rendimiento[20])
    capital.append(capital[20] + capital[20]*rendimiento[21])
    capital.append(capital[21] + capital[21]*rendimiento[22])
    capital.append(capital[22] + capital[22]*rendimiento[23])
    capital.append(capital[23] + capital[23]*rendimiento[24])
    
    return np.array(rendimiento),capital

def acum1():
    acum = [0]
    acum.append(((febrero20()-enero20())/febrero20()))
    acum.append(acum[1] + ((marzo20()-febrero20())/marzo20()))
    acum.append(acum[2] + ((abril20()-marzo20())/abril20()))
    acum.append(acum[3] + ((mayo20()-abril20())/mayo20()))
    acum.append(acum[4] + ((junio20()-mayo20())/junio20()))
    acum.append(acum[5] + ((julio20()-junio20())/julio20()))
    acum.append(acum[6] + ((agosto20()-julio20())/agosto20()))
    acum.append(acum[7] + ((septiembre20()-agosto20())/septiembre20()))
    acum.append(acum[8] + ((octubre20()-septiembre20())/octubre20()))
    acum.append(acum[9] + ((noviembre20()-octubre20())/noviembre20()))
    acum.append(acum[10] + ((diciembre20()-noviembre20())/diciembre20()))
    acum.append(acum[11] + ((enero21()-diciembre20())/enero21()))
    
    acum.append(acum[12] + ((febrero21()-enero21())/febrero21()))
    acum.append(acum[13] + ((marzo21()-febrero21())/marzo21()))
    acum.append(acum[14] + ((abril21()-marzo21())/abril21()))
    acum.append(acum[15] + ((mayo21()-abril21())/mayo21()))
    acum.append(acum[16] + ((junio21()-mayo21())/junio21()))
    acum.append(acum[17] + ((julio21()-junio21())/julio21()))
    acum.append(acum[18] + ((agosto21()-julio21())/agosto21()))
    acum.append(acum[19] + ((septiembre21()-agosto21())/septiembre21()))
    acum.append(acum[20] + ((octubre21()-septiembre21())/octubre21()))
    acum.append(acum[21] + ((noviembre21()-octubre21())/noviembre21()))
    acum.append(acum[22] + ((diciembre21()-noviembre21())/diciembre21()))
    acum.append(acum[23] + ((enero22()-diciembre21())/enero22()))
        
    return np.array(acum)

def df_pasiva_a(df_limpio):

    fecha = pd.to_datetime(df_limpio["Fecha"].unique().tolist())[0:13]
    df_pasiva_a = pd.DataFrame({'Timestamp':fecha,"Capital":rendimiento1()[1][0:13],"Rendimiento":rendimiento1()[0][0:13],"Rend_Acum":acum1()[0:13]})
    print("Pre-Pandemia")
    return df_pasiva_a

def df_pasiva_b(df_limpio):
    fecha = pd.to_datetime(df_limpio["Fecha"].unique().tolist())[12:25]
    df_pasiva_b = pd.DataFrame({'Timestamp':fecha,"Capital":rendimiento1()[1][12:25],"Rendimiento":rendimiento1()[0][12:25],"Rend_Acum":acum1()[12:25]})
    print("Pandemia")
    return df_pasiva_b

def rendimiento2():
    rendimiento = [0]
    rendimiento.append((febrero21()-enero21())/febrero21())
    rendimiento.append((marzo21()-febrero21())/marzo21())
    rendimiento.append((abril21()-marzo21())/abril21())
    rendimiento.append((mayo21()-abril21())/mayo21())
    rendimiento.append((junio21()-mayo21())/junio21())
    rendimiento.append((julio21()-junio21())/julio21())
    rendimiento.append((agosto21()-julio21())/agosto21())
    rendimiento.append((septiembre21()-agosto21())/septiembre21())
    rendimiento.append((octubre21()-septiembre21())/octubre21())
    rendimiento.append((noviembre21()-octubre21())/noviembre21())
    rendimiento.append((diciembre21()-noviembre21())/diciembre21())
    rendimiento.append((enero22()-diciembre21())/enero22())
    
    capital = [inicial()-157227]
    capital.append(capital[0] + capital[0]*rendimiento[1])
    capital.append(capital[1] + capital[1]*rendimiento[2])
    capital.append(capital[2] + capital[2]*rendimiento[3])
    capital.append(capital[3] + capital[3]*rendimiento[4])
    capital.append(capital[4] + capital[4]*rendimiento[5])
    capital.append(capital[5] + capital[5]*rendimiento[6])
    capital.append(capital[6] + capital[6]*rendimiento[7])
    capital.append(capital[7] + capital[7]*rendimiento[8])
    capital.append(capital[8] + capital[8]*rendimiento[9])
    capital.append(capital[9] + capital[9]*rendimiento[10])
    capital.append(capital[10] + capital[10]*rendimiento[11])
    capital.append(capital[11] + capital[11]*rendimiento[12])
    
    return np.array(rendimiento),capital

def acum2():
    acum = [0]
    acum.append(((febrero21()-enero21())/febrero21()))
    acum.append(acum[1] + ((marzo21()-febrero21())/marzo21()))
    acum.append(acum[2] + ((abril21()-marzo21())/abril21()))
    acum.append(acum[3] + ((mayo21()-abril21())/mayo21()))
    acum.append(acum[4] + ((junio21()-mayo21())/junio21()))
    acum.append(acum[5] + ((julio21()-junio21())/julio21()))
    acum.append(acum[6] + ((agosto21()-julio21())/agosto21()))
    acum.append(acum[7] + ((septiembre21()-agosto21())/septiembre21()))
    acum.append(acum[8] + ((octubre21()-septiembre21())/octubre21()))
    acum.append(acum[9] + ((noviembre21()-octubre21())/noviembre21()))
    acum.append(acum[10] + ((diciembre21()-noviembre21())/diciembre21()))
    acum.append(acum[11] + ((enero22()-diciembre21())/enero22()))
        
    return np.array(acum)

def df_activa(df_limpio):
    fecha = pd.to_datetime(df_limpio["Fecha"].unique().tolist())[12:25]
    df_activo = pd.DataFrame({'Timestamp':fecha,"Capital":rendimiento2()[1],"Rendimiento":rendimiento2()[0],"Rend_Acum":acum2()})
    print("Df Activa")
    return df_activo

def medias():
    s1 = (np.array(rendimiento1()[0]).mean())/np.array(rendimiento1()[0].std())
    s2 = (np.array(rendimiento2()[0]).mean())/np.array(rendimiento2()[0]).std() - 0.465
    
    r1 = np.array(rendimiento1()[0]).mean()
    r2 = np.array(rendimiento2()[0]).mean()
    
    ra1 = acum1().mean()
    ra2 = acum2().mean()
    
    df_medias = pd.DataFrame({"Medidas": ["Rend_m","Rend_c","sharpe"], "Descripción": ["Rendimiento Promedio Mensual","Rendimiento mensual acumulado","Sharpe Ratio"],"inv_activa":[r1,ra1,s1],"inv_pasiva":[r2,ra2,s2]})
    
    return df_medias