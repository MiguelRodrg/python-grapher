from .convertions import to_second

# def estandarize(table):
#     print(f"Atributos: {table.attrs}")
#     interval = to_second(table.attrs['Time interval'][0])
#     print(f"Intervalo de tiempo en segundos: {interval}")
#     print(new_tale['Tiempo'])
#     table['Tiempo'] = table['Tiempo']*interval[0]
#     print(f"Primeros 5 valores de tiempo estandarizados: {table['Tiempo'].head()}")
#     print("Estandarización completa.")

def time(time_interval,list):
    units = to_second(time_interval)
    list = [x*units for x in list]
    return list
