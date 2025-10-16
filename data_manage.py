import pandas as pd
from Specific_osc import *
print("Pandas importado")

def obtener_mediciones(mediciones):
    importaciones=[]
    n=0
    for medicion in mediciones:
        nombre = medicion.name
        # directorio = medicion.resolve()
        # extraido={'nombre':nombre, 'directorio':directorio}
        extraido = {'nombre':nombre,'canales':[]}
        archivos = list(medicion.glob("*.CSV"))
        archivos.extend(list(medicion.glob("*.csv")))
        mediciones = [str(archivo.name) for archivo in archivos]
        for archivo in archivos:
            tabla = leer_cvs2(archivo)
        #     extraido[archivo.name] = tabla
            extraido['canales'].append(archivo.name)
        importaciones.append(extraido)
        n+=1
    return importaciones

def leer_cvs(archivo):
    tabla = pd.read_csv(archivo.resolve(),header=None, index_col=None, names=["Caracteristica","valor","N3", "Tiempo", "Voltaje","N5"])
    caracteristicas = dict(zip(tabla["Caracteristica"], tabla["valor"]))
    #
    for k in list(caracteristicas.keys()):
        if pd.isna(k):
            del caracteristicas[k]
    # 
    tabla = tabla[["Tiempo","Voltaje"]]
    tabla.attrs = caracteristicas
    print("Tabla ", archivo.name,":")
    tabla.attrs["name"] = archivo.name
    print(tabla.head())
    print("Caracteristicas: ")
    for caracteristica,valor in caracteristicas.items(): print(f"{caracteristica} : \t{valor}")
    print("Parent name: ")
    tabla.attrs["parent_name"] = archivo.parent.name
    print(archivo.parent.name)
    tabla.attrs["parent_dir"] = archivo.parent.resolve()
    print("Parent dir: ")
    print(archivo.parent.resolve())
    tabla.attrs["dir"] = archivo.resolve()
    print(f"Tabla: {archivo.name}")
    tabla["Voltaje"] = multiplicar_ganancia()*tabla["Voltaje"]
    return tabla


def multiplicar_ganancia():
    ganancia = 1
    while True:
        # return ganancia
        multiplicar=input("¿Multiplicar voltaje por ganancia? (s/n): ").lower()
        if multiplicar not in ["s","n"]:
            continue
        break
    if multiplicar == "s":
        while True:
            try:
                ganancia = float(input("Ingrese la ganancia: "))
                return(ganancia)
            except ValueError:
                while True:
                    retry = input("Valor de ganancia inválido. Intentar nuevamente? (s/n): ")
                    if retry.lower() not in ["n","s"]: continue
                    break
                if retry.lower() == "s": continue
                else:
                    ganancia = 1 
                    break
    return(ganancia)


def leer_cvs2(archivo):
    tabla = pd.read_csv(archivo.resolve(),header=None)
    fila,columnas = detect_data_start(tabla)
    encabezados=["Tiempo","Voltaje"]
    if fila is None or columnas is None:
        print(f"No se pudo detectar los datos en el archivo {archivo.name}.")
        return None
    new_table = tabla.iloc[fila:,columnas]
    new_table = new_table.apply(pd.to_numeric, errors='coerce')
    if fila > 0:
        encabezados[0]= tabla.iloc[fila-1,columnas[0]]
        for i in columnas[1:]:
            if  len(encabezados) > i:
                encabezados[i] = tabla.iloc[fila-1,columnas[i]]
            else:
                encabezados.append(tabla.iloc[fila-1,columnas[i]])
    new_table.columns = encabezados
    new_table.attrs,common = usual_metadata(tabla,new_table,archivo.name,archivo.parent.name,archivo.parent.resolve())
    return new_table



def detect_data_start(df, min_numeric_cols=2, check_depth=10):
    n_rows, n_cols = df.shape

    numeric_mask = df.apply(pd.to_numeric, errors='coerce').notna()

    for i in range(n_rows - check_depth):
        num_cols = numeric_mask.iloc[i].sum() #Sum of numeric values in the row i

        if num_cols >= min_numeric_cols: #At least a min row of columns (sum of true numeric values) to check the deep of the candidate's data
            candidate_cols = numeric_mask.columns[numeric_mask.iloc[i]]#Select the columns by the value true or false in the boolean table, row i. Returns an array with the NAMES of the columns, not the columns

            is_consistent = check_depth == numeric_mask[candidate_cols].iloc[i:i+check_depth].sum()#For each column, if the depth of numeric values is complete
            stable_cols = list(is_consistent.index[is_consistent])

            if len(stable_cols) >= min_numeric_cols:
                return i, stable_cols
    return None

