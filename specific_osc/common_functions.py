from . import osc_data, osc_all
import re
import pandas as pd

def usual_metadata(table,new_table,namedata,nameall0,father):
    common = False
    if nameall0.lower().startswith("all0"):
        table.attrs=dict(zip(table.iloc[0:,0], table.iloc[0:,1]))
        # estandarize(table)
        common = True
    if namedata.lower().startswith("data_"):
        table.attrs = {key: [v1, v2] for key, v1, v2 in zip(table.iloc[0:7, 0], table.iloc[0:7, 1], table.iloc[0:7, 2])}
        table.attrs = {key.strip('\:').strip(): v for key , v in table.attrs.items()}
        new_table = osc_data.estandarize(table,new_table)
        new_table.attrs = table.attrs
        df = pd.DataFrame(new_table.attrs)
        df.to_csv(f"{father}/{nameall0}.cvs",index=False,sep='\t')
    print(f"Atributos a exportar: \n{table.attrs}")
    return new_table,common

