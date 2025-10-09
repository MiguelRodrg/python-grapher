import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

def graficar(mediciones):
    for medicion in mediciones:
        graphs = []
        for canal in medicion['canales']:
            tabla = medicion[canal]
            x = tabla["Tiempo"]
            y = tabla["Voltaje"]
            legend = canal
            title = medicion['nombre']
            graphs.append({'x':x, 'y':y, 'label': legend, 'title':title})
            
        plot_continuous(graphs)
    

def plot_continuous(graphs, title="Grafica"):
    # xlabel="Eje X", ylabel="Eje Y",linestyle='-', lw=0.5, color='b',grid=True
    plt.figure(figsize=(8, 5))
    plt.plot(graphs[0]['x'],graphs[0]['y'],marker='o',ms = 0.1, linestyle='-', lw=0.5)
    plt.plot(graphs[1]['x'],graphs[1]['y'])
    plt.legend([graph['label'] for graph in graphs], loc=4,bbox_to_anchor=(1, 0))
    # plt.legend(loc=4)
    plt.grid(True)
    plt.minorticks_on()
    plt.title(graphs[0]['title'])
    ax = plt.gca()
    cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
    plt.show()


def plot_basic(data, title="Grafica", xlabel="Eje X", ylabel="Eje Y",linestyle='-', lw=0.5, color='b',grid=True):
    if type(data) is list:
        if len(data) != 2:
            raise ValueError("Data must be a list of two elements: [x, y]")
    else:
        if type(data) is dict:
            if 'x' in data and 'y' in data:
                data = [data['x'], data['y']]
            else:
                raise ValueError("Data dictionary must contain 'x' and 'y' keys.")
    
    plt.figure(figsize=(8, 5))
    plt.plot(data[0],data[1], linestyle=linestyle, lw=lw, color=color)
    plt.title(title)
    plt.xlabel('Tiempo')
    plt.ylabel('Voltaje')
    plt.grid(True)
    plt.show()

            

    
