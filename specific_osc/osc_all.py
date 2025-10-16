from .convertions import to_second

def estandarize(table,new_table):
    interval = to_second(table.attrs['Time interval'][0])
    new_table['index'] = new_table['index']*interval
    new_table.rename(columns={"index":"Tiempo"},inplace=True)
    return new_table

