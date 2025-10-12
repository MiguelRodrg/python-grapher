import pandas as pd

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

# def escribir_metadatos(archivo):
#     with open(archivo)


def leer_cvs2(archivo):
    tabla = pd.read_csv(archivo.resolve(),header=None)
    inicio_datos = detect_data_start(tabla)
    if inicio_datos is None:
        print(f"No se pudo detectar los datos en el archivo {archivo.name}.")
        return None
    tiempo = tabla[inicio_datos[1][0]][inicio_datos[0]:]
    voltajes = []
    for indice in inicio_datos[1][1:]:
        voltajes.append(tabla[indice][inicio_datos[0]:])
    return tabla



def detect_data_start(df, min_numeric_cols=2, check_depth=10):
    n_rows, n_cols = df.shape

    numeric_mask = df.apply(pd.to_numeric, errors='coerce').notna()

    for i in range(n_rows - check_depth):
        num_cols = numeric_mask.iloc[i].sum()

        if num_cols >= min_numeric_cols:
            candidate_cols = numeric_mask.columns[numeric_mask.iloc[i]]

            is_consistent = numeric_mask[candidate_cols].iloc[i:i+check_depth].sum()
            stable_cols_mask = is_consistent == check_depth
            stable_cols = list(is_consistent.index[stable_cols_mask])

            if len(stable_cols) >= min_numeric_cols:
                return i, stable_cols
    return None  