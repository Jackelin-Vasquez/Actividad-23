#Actividad
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x350")

etiqueta = tk.Label(ventana, text="Escribe un número:")
etiqueta.pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

etiqueta2 = tk.Label(ventana, text="Escribe un número:")
etiqueta2.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

def suma():
    num1= int(entrada.get())
    num2= int(entrada2.get())
    resultado= num1 + num2
    etiqueta.config(text=f"Suma de numeros: {resultado}")

def resta():
    num1= int(entrada.get())
    num2= int(entrada2.get())
    resultado= num1 - num2
    etiqueta.config(text=f"Resta de numeros: {resultado}")


def multi():
    num1 = int(entrada.get())
    num2 = int(entrada2.get())
    resultado = num1 * num2
    etiqueta.config(text=f"multiplciación de numeros: {resultado}")

def division():
    num1 = int(entrada.get())
    num2 = int(entrada2.get())
    resultado = num1 / num2
    etiqueta.config(text=f"division de numeros: {resultado}")

def limpiar():
    entrada.delete(0, tk.END)
    etiqueta.config(text="Escribe un numero:")
    entrada2.delete(0,tk.END)
    etiqueta2.config(text="Escribe un numero:")

boton_suma = tk.Button(ventana, text="Suma", command=suma)
boton_suma.pack(pady=5)

boton_resta = tk.Button(ventana, text="Resta", command=resta)
boton_resta.pack(pady=5)

boton_multipli= tk.Button(ventana, text="Multiplicar", command=multi)
boton_multipli.pack(pady=5)

boton_division = tk.Button(ventana, text="División", command=division)
boton_division.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

ventana.mainloop()