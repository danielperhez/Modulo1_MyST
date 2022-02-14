import functions as fn
import pandas as pd

naftrac = pd.read_csv('files/NAFTRAC_holdings.csv')

naftrac_limpio = fn.nuevo_DataFrame(naftrac,"Nombre",25,"Fecha","Ticker")

print(fn.df_pasiva_a(naftrac_limpio))

print(fn.df_pasiva_b(naftrac_limpio))

print(fn.df_activa(naftrac_limpio))

print(fn.medias())