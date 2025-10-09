from pathlib import Path

def obtenerDirectorio():
    directorio =Path.cwd()
    print("\n\nDirectorio actual:\t", directorio.resolve(),"\n")
    return(directorio)



def explorar(elemento,dirBase=None):
    if elemento.name in ["venv","__pycache__"]:return(None)
    if dirBase is None: dirBase = elemento.resolve() 
    else: print("\nElementos en el directorio /",elemento.relative_to(dirBase)," :")
    if elemento.is_file():
        print(elemento.name, "\t /", elemento.relative_to(dirBase))
        return()
    items = sorted(elemento.iterdir(), key = lambda x: x.name)
    
    for item in items:
        if item.name in ["venv","__pycache__"]:continue
        isDir = "\t\t Directorio"if item.is_dir() else ""
        print(item.name, "\t/", item.relative_to(dirBase), isDir)
        if item.is_dir(): explorar(item,dirBase)
    print("\n")



def obtener_objetos(directorio):
    while(1):
        # elementos_a_buscar = input("Ingrese los nombres de los muestreos del osciloscopio a graficar, separados por comas. (Ejemplo: ALL0001, ALL0000): ")
        # elementos_a_buscar = "ALL0004, ALL0003, ALL0005, ALL0006"
        elementos_a_buscar = "ALL0001"
        objetos = buscar(directorio,elementos_a_buscar)
        if objetos == "" or objetos is None:
            input_s = ""
            while (input_s not in ["s","n"]):
                input_s = input("Desea intentar de nuevo? (s/n): ").lower()
            if  input_s== "n": return()
            else: continue
        return(objetos)




def buscar(directorio,objetos = []):
    if objetos == [] or objetos == "": return(None)
    if type(objetos) == str: objetos = [x.strip() for x in objetos.split(",")]
    resultados = [item for item in list(directorio.rglob("*")) if item.name in objetos and item.is_dir()]
    if resultados == []:
        print("\nNo se encontró ningún muestreo con ese/esos nombres.")
        return(None)
    print("\nElementos encontrados: ", [item.name for item in resultados])
    return resultados


