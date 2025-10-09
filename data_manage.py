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
        mediciones = [str(archivo.name) for archivo in archivos]
        for archivo in archivos:
            tabla = leer_cvs(archivo)
            extraido[archivo.name] = tabla
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

