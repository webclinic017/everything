import pandas as pd
import time
import yfinance as yf
from finta import TA
import numpy as np
import pandas as pd
import datetime as dt
import copy
import json
from py5paisa import FivePaisaClient
import datetime as dt

client = FivePaisaClient(email="sudhanshu8833@gmail.com", passwd="Madhya246###", dob="20010626")
client.login()

tickers=['AARTIIND','AMARAJABAT','ANDHRSUGAR','GODREJAGRO','APOLLOTYRE','ASHOKLEY','IEX','AUROPHARMA','BALMLAWRIE','BALRAMCHIN','NAM-INDIA','BEL','BEPL','BHARATFORG','KHADIM','HDFCLIFE','BIRLACABLE','MAZDOCK','BPCL','UTIAMC','GRAPHITE','CENTURYTEX','IGARASHI','CHAMBLFERT','EXIDEIND','CHOLAFIN','CIPLA','SHALBY','TATACOFFEE','COROMANDEL','DABUR','DALMIASUG','DHAMPURSUG','EIDPARRY','EIHOTEL','FACT','FINPIPE','ZENSARTECH','GREAVESCOT','GSFC','AMBUJACEM','HINDALCO','HINDOILEXP','HINDPETRO','HSIL','HINDZINC','BURGERKING','ASTERDM','INDHOTEL','INDIACEM','IOC','ITC','HGINFRA','ITI','KABRAEXTRU','KCP','CUMMINSIND','LIBERTSHOE','LICHSGFIN','M&M','CHENNPETRO','BANDHANBNK','RAILTEL','NOCIL','MIDHANI','ONGC','BCLIND','PHILIPCARB','JUBLINGREA','EASEMYTRIP','RALLIS','LXCHEM','RAYMOND','RIIL','SAIL','ORIENTELEC','JINDALSAW','SBIN','SCI','VEDL','TATACHEM','TATAPOWER','TATACONSUM','TATAMOTORS','TNPETRO','WIPRO','WSTCSTPAPR','ZEEL','NBVENTURES','MARICO','MOTHERSUMI','GAIL','CONCOR','ICICIBANK','JAICORPLTD','CUB','AXISBANK','JINDALSTEL','BSOFT','HCLTECH','GLENMARK','WOCKPHARMA','NRBBEARING','CADILAHC','TVSMOTOR','NETFMID150','CHALET','VRLLOG','GAEL','MSTCLTD','PNCINFRA','GODREJCP','MCDOWELL-N','NIFTYBEES','KRBL','GUJGASLTD','BHARTIARTL','OLECTRA','PONNIERODE','GODREJIND','JSL','IGL','DREDGECORP','UPL','PETRONET','PTC','BIOCON','ZOTA','BANKBEES','CCL','ASTRAMICRO','NTPC','JSWSTEEL','EVEREADY','SHOPERSTOP','WELCORP','JKPAPER','GRANULES','JSLHISAR','SWSOLAR','TRIVENI','NITINSPIN','KEC','M&MFIN','KEI','UTTAMSUGAR','SUNTV','RSYSTEMS','ALLCARGO','ELECON','GEECEE','GATI','VISHWARAJ','DCBBANK','TORNTPOWER','MINDAIND','REDINGTON','PFC','FSL','INDIANB','JKTYRE','IBREALEST','BFUTILITIE','FORTIS','GUJAPOLLO','DLF','SPARC','ASIANTILES','MAHINDCIE','CSBBANK','POWERGRID','DELTACORP','RELIGARE','ADANIPORTS','IRB','NMDC','RAIN','RECLTD','VGUARD','HCG','KIRIINDUS','TATAMTRDVR','AJMERA','SHILPAMED','DLINKINDIA','JSWENERGY','HINDCOPPER','SUVENPHAR','SBICARD','RBLBANK','ICICIPRULI','VBL','MANAPPURAM','LAURUSLABS','GPPL','ASHOKA','COALINDIA','MOIL','AVADHSUGAR','COCHINSHIP','ABCAPITAL','MAXHEALTH','BODALCHEM','VSSL','ROSSELLIND','INDUSTOWER','SCHNEIDER','CANBK','GLOBUSSPR','OIL','AEGISCHEM','HAPPSTMNDS','SUNPHARMA','JUSTDIAL','ORIENTCEM','ABFRL','IBULHSGFIN']
