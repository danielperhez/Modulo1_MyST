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
    
    
    a[columna_fecha] = pd.to_datetime(a[columna_fecha])
    
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

