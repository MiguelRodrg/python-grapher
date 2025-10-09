from navegacion import *
from data_manage import *
from Plot import *
import matplotlib.pyplot as plt

def main():
    directorio = obtenerDirectorio()
    explorar(directorio)
    objetos = obtener_objetos(directorio)
    mediciones = obtener_mediciones(objetos)
    graficar(mediciones)
    # for tabla,medicion in mediciones.items():
    #     plt.figure(figsize=(8,5))
    #     plt.plot(medicion['Tiempo'], medicion['Voltaje'], linestyle='-', lw=0.5, color='b')
    #     plt.title(tabla)
    #     plt.xlabel('Tiempo')
    #     plt.ylabel('Voltaje')
    #     plt.grid(True)
    #     plt.show()
    print("")
	# nombres = [elemento.glob("*.cvs") for elemento in objetos]
    # print("Elementos encontrados: ", nombres)
    



if __name__ == "__main__":
    main()

