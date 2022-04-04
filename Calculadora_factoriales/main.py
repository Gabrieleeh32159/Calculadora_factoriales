from tkinter import *
from tkinter import messagebox


def factorial(x):
    if x >= 0:
        resultado = 1
        for i in range(1, x+1):
            resultado *= i

        resultado_txt.delete(0, 'end')
        resultado_txt.insert(0, resultado)
    else:
        messagebox.showinfo('Error', 'Número no válido.')


ventana_principal = Tk()
ventana_principal.geometry("700x400")
ventana_principal.title("Factoriales")

Label(text="Cálculo de Factorial", width="300", height="2", font=("Arial", 30)).pack()

#Ingresar el numero
Label(text="Ingrese un numero", bg="lightblue", font=("Arial", 15)).pack()
Label(text="").pack()
numero_ingresado = IntVar(ventana_principal, value='')
Entry(ventana_principal, textvariable=numero_ingresado, font=("Arial", 20)).pack()

#Mostrar el resultado
Label(text="").pack()
Label(text="El resultado es: ", bg="lightblue", font=("Arial", 15)).pack()
Label(text="").pack()

resultado_txt = Entry(ventana_principal, textvariable="", font=("Arial", 20))
resultado_txt.pack()
Label(text="").pack()

#Botón
Button(text="Calcular Factorial", height="2", width="30", font=("Arial", 15), bg="orange", command=lambda: factorial(numero_ingresado.get())).pack()

ventana_principal.mainloop()
