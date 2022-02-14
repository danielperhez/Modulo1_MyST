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