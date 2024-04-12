import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Definir una estructura de datos para los productos
productos = [
    {'nombre': 'Artículo 1', 'categoria': 'Electrónica', 'ubicacion': (1.5, 1.5)},
    {'nombre': 'Artículo 2', 'categoria': 'Electrodomésticos', 'ubicacion': (1.5, 4)},
    {'nombre': 'Artículo 3', 'categoria': 'Hogar', 'ubicacion': (3, 3)},
    {'nombre': 'Artículo 4', 'categoria': 'Hogar', 'ubicacion': (3, 6)},
    {'nombre': 'Artículo 5', 'categoria': 'Electrodomésticos', 'ubicacion': (6, 6)}
]

# Función para buscar productos por nombre
def buscar_por_nombre(nombre):
    resultados = [producto for producto in productos if nombre.lower() in producto['nombre'].lower()]
    return resultados

# Función para buscar productos por categoría
def buscar_por_categoria(categoria):
    resultados = [producto for producto in productos if categoria.lower() in producto['categoria'].lower()]
    return resultados

# Función para mostrar la ubicación de los productos en el plano del local
def mostrar_ubicacion(ax, productos):
    for producto in productos:
        nombre = producto['nombre']
        ubicacion = producto['ubicacion']
        ax.text(ubicacion[0], ubicacion[1], nombre, ha='center', va='center', fontsize=8, color='red')

# Función para generar el plano del local con los productos encontrados
def generar_plano_con_productos(dim_x, dim_y, estanterias, productos, etiquetas=None):
    # Crear figura y ejes
    fig, ax = plt.subplots()
    
    # Establecer límites de los ejes
    ax.set_xlim(0, dim_x)
    ax.set_ylim(0, dim_y)
    
    # Dibujar las estanterías
    for i, (x, y, width, height) in enumerate(estanterias):
        ax.add_patch(Rectangle((x, y), width, height, color='gray'))
        
        # Mostrar el nombre de la estantería en la parte superior
        if etiquetas is not None and i < len(etiquetas):
            etiqueta_x = x + width / 2
            etiqueta_y = y + height + 0.5  # Ajuste la posición vertical
            ax.text(etiqueta_x, etiqueta_y, etiquetas[i], ha='center', va='center', fontsize=8)
    
    # Mostrar la ubicación de los productos
    mostrar_ubicacion(ax, productos)
    
    # Mostrar el plano
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('Longitud (metros)')
    plt.ylabel('Anchura (metros)')
    plt.title('Plano del local con productos')
    plt.grid(True)
    plt.show()

# Función para manejar la búsqueda de productos
def buscar_producto():
    nombre_buscado = entry_nombre.get()
    categoria_buscada = entry_categoria.get()
    
    if not nombre_buscado and not categoria_buscada:
        messagebox.showerror('Error', 'Por favor, ingresa un nombre o una categoría para buscar.')
        return
    
    if nombre_buscado:
        resultados = buscar_por_nombre(nombre_buscado)
    else:
        resultados = buscar_por_categoria(categoria_buscada)
    
    if not resultados:
        messagebox.showinfo('Información', 'No se encontraron resultados para la búsqueda.')
    else:
        generar_plano_con_productos(10, 8, [(1, 1, 2, 6)], resultados)

# Crear ventana principal
root = tk.Tk()
root.title('Búsqueda de Productos')

# Crear etiquetas y entradas para ingresar el nombre y la categoría
tk.Label(root, text='Nombre del Producto:').pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text='Categoría del Producto:').pack()
entry_categoria = tk.Entry(root)
entry_categoria.pack()

# Botón de búsqueda
btn_buscar = tk.Button(root, text='Buscar', command=buscar_producto)
btn_buscar.pack()

# Ejecutar la aplicación
root.mainloop()
