import re
import pyperclip
import tkinter as tk
from tkinter import scrolledtext

def extraer_ips(texto):
    # Regex para encontrar direcciones IP
    regex_ip = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    # Encuentra todas las IPs en el texto
    ips = re.findall(regex_ip, texto)
    return ips

def ordenar_ips(ips):
    # Convierte las IPs en tuplas de enteros para ordenar correctamente
    ips_ordenadas = sorted(ips, key=lambda ip: tuple(map(int, ip.split('.'))))
    return ips_ordenadas

def procesar_texto():
    texto = text_input.get("1.0", tk.END)
    ips_a_excluir_texto = text_exclude.get("1.0", tk.END)
    ips_a_excluir = set(extraer_ips(ips_a_excluir_texto))

    ips = extraer_ips(texto)
    ips_filtradas = [ip for ip in ips if ip not in ips_a_excluir]
    ips_ordenadas = ordenar_ips(ips_filtradas)

    resultado = "\n".join(ips_ordenadas)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, resultado)

def copiar_resultado():
    resultado = text_output.get("1.0", tk.END)
    pyperclip.copy(resultado)

def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Extractor y Ordenador de IPs")
    
    # Definir el tamaño inicial de la ventana
    ventana.geometry('1200x950')

    # Actualizar la geometría para posicionarla correctamente
    ventana.update_idletasks()
    
    # Posicionar la ventana en la esquina superior izquierda
    ventana.geometry('+300+50')
    
    # Usar grid para organizar la interfaz en columnas
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)
    ventana.columnconfigure(2, weight=1)

    # Cuadro de entrada de texto
    label_input = tk.Label(ventana, text="Introduce el texto:")
    label_input.grid(row=0, column=0, padx=10, pady=5, sticky='n')

    global text_input
    text_input = scrolledtext.ScrolledText(ventana, width=40, height=50)
    text_input.grid(row=1, column=0, padx=10, pady=5, sticky='n')

    # Cuadro de IPs a excluir
    label_exclude = tk.Label(ventana, text="IPs a excluir (una por línea):")
    label_exclude.grid(row=0, column=1, padx=10, pady=5, sticky='n')

    global text_exclude
    text_exclude = scrolledtext.ScrolledText(ventana, width=40, height=50)
    text_exclude.grid(row=1, column=1, padx=10, pady=5, sticky='n')

    # Cuadro de resultado
    label_output = tk.Label(ventana, text="Resultado:")
    label_output.grid(row=0, column=2, padx=10, pady=5, sticky='n')

    global text_output
    text_output = scrolledtext.ScrolledText(ventana, width=40, height=50)
    text_output.grid(row=1, column=2, padx=10, pady=5, sticky='n')

    # Botón para procesar
    boton_procesar = tk.Button(ventana, text="Procesar", command=procesar_texto)
    boton_procesar.grid(row=2, column=1, pady=10)
    
    # Botón para copiar el resultado
    boton_copiar = tk.Button(ventana, text="Copiar resultado", command=copiar_resultado)
    boton_copiar.grid(row=3, column=1, pady=10, sticky='n')

    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()



"""
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉

Programado por Braulio Alberto Vargas Garcia para mexico y el mundo

"""