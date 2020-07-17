
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

############################# Variables ################################
dn = ["billete", "billete", "billete", "billete", "billete",
      "billete", "moneda", "moneda", "moneda", "moneda"]  # denominacion del billete
va = [50000, 20000, 10000, 5000, 2000, 1000,
      500, 200, 100, 50]  # valor del billete
ex = [5, 5, 10, 10, 10, 10, 10, 20, 50, 50]  # exixtencia billetes
cd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # cantidad a devolver
restante = 0
totalEncaja = 0

############################# Crear ventana ############################
v = Tk()
v.wm_title("Sistema de devueltas")
# v.minsize(500, 500)
v.geometry("550x400")
v.resizable(0, 0)

# labels
Label(v, text="Denominación").grid(row=2, column=1)
Label(v, text="Existencia").grid(row=2, column=2)
Label(v, text="Devuelta").grid(row=2, column=3)
######################## Caja de texto desplegable ######################


############################### Funciones ###############################


def generarCamposTexto():

    # crear campos denominación
    for i in range(0, len(va)):
        txtDen = tk.Entry(v, width=10)
        txtDen.grid(row=i + 3, column=1, padx=2, pady=2)
        txtDen.insert(END, str(va[i]))
        txtDen.config(state="readonly")

    # crear campos existencia
    for i in range(0, len(ex)):
        txtDen = tk.Entry(v, width=5)
        txtDen.grid(row=i + 3, column=2, padx=2, pady=2)
        txtDen.insert(END, str(ex[i]))
        txtDen.config(state="readonly")

    # crear campos existencia
    for i in range(0, len(cd)):
        txtDen = tk.Entry(v, width=5)
        txtDen.grid(row=i + 3, column=3, padx=2, pady=2)
        txtDen.insert(END, str(cd[i]))
        txtDen.config(state="readonly")


def obtenerDevolver():

    devolver = textoDevolve.get()

    if(devolver.isdigit() == False):
        messagebox.showinfo(message=(textoDevolve.get()+" no es un número"))
    else:
        devolver = int(textoDevolve.get())
        restante = devolver

        # lo que no se pued edevolver por que no hay denominacion o no hay dinero en caja

    # primero se
        if devolver < 50:
            print()
            messagebox.showinfo(message=("No se pueden devolver " +
                                         str(devolver) + " pesos"), title="No hay denominacion")
        else:
            totalEncaja = 0
            for i in range(0, len(ex)):
                totalEncaja = totalEncaja+(ex[i] * va[i])

        if totalEncaja >= devolver:

            # reinicia cantidad de billetes para devuelta
            for i in range(0, len(cd)):
                cd[i] = 0

            # utilizando for
            for i in range(0, len(va)):
                # print(int(devolver / va[i]))

                if ((ex[i] >= int(devolver / va[i]) & (devolver >= va[i])) | (va[i] * ex[i] >= devolver)):
                    if (ex[i] >= int(devolver / va[i])):
                        cantidad = int(devolver / va[i])
                        devolver = devolver % va[i]  # utilizando modulo %
                        restante = devolver
                        ex[i] -= cantidad
                        cd[i] += cantidad
                    else:
                        cantidad = ex[i]
                        devolver = devolver - (cantidad * va[i])
                        restante = devolver
                        ex[i] -= cantidad
                        cd[i] += cantidad

            mostrarResultado(restante)
        else:
            messagebox.showinfo(message=("No hay suficnete dinero en caja, solo hay " +
                                         str(totalEncaja)), title="No hay dinero suficiente")


def mostrarResultado(restante):
    rowInicial = 2
    pos = 0
    totalEncafa = 0

    # utilizando el while
    # limpiar labels de salida
    while pos < len(va):
        Label(v, text=" La devuleta de compone de:").grid(
            row=rowInicial, column=4)
        Label(v, text="███████████", fg="#F0F0F0").grid(
            row=rowInicial + pos + 1, column=4)
        pos = pos + 1

    # nuevas salida
    pos = 0
    while pos < len(va):
        Label(v, text=" La devuleta de compone de:").grid(
            row=rowInicial, column=4)
        if cd[pos] > 0:
            Label(v, text=(str(cd[pos]) + "  " + str(dn[pos]) + "s  de  $" +
                           str(va[pos]))).grid(row=rowInicial + pos + 1, column=4)

        pos = pos + 1

    # si hay restante
    if restante > 0:
        Label(v, text=("No se pueden devolver "+str(restante)+" pesos")
              ).grid(row=rowInicial + pos + 1, column=4)

    generarCamposTexto()


def actualizarExistencia():
    if(textoActualizar.get().isdigit() == False):
        messagebox.showinfo(message=(textoActualizar.get()+" no es un número"))
    else:
        print(textoActualizar.get())
        ex[cbxActualizar.current()] = int(textoActualizar.get())
        generarCamposTexto()


generarCamposTexto()

################### caja y boton de texto devolver ######################

textoBoton = StringVar(value="Devolver")
btnDevolver = Button(v, textvariable=textoBoton, command=obtenerDevolver)
btnDevolver.grid(row=1, column=3)
btnDevolver.config(bd=2)

textoDevolve = StringVar()
txtDevolver = Entry(v, width=20, textvariable=textoDevolve)
txtDevolver.grid(row=1, column=4, padx=10, pady=10)
txtDevolver.config(justify="center")
txtDevolver.focus()

################### fin caja y boton de texto devolver ##################

######################### actuazar billetes #############################

textoBotonAct = StringVar(value="Actualizar")
btnActualizar = Button(v, textvariable=textoBotonAct,
                       command=actualizarExistencia)
btnActualizar.grid(row=0, column=3)
btnActualizar.config(bd=2)

textoActualizar = StringVar()
txtActualizar = Entry(v, width=20, textvariable=textoActualizar)
txtActualizar.grid(row=0, column=4, padx=10, pady=10)
txtActualizar.config(justify="center")
txtActualizar.focus()

######################### fin actuazar billetes #########################

####################### menu actuazar billetes ##########################

cbxActualizar = ttk.Combobox(
    v, values=va, state="readonly")
cbxActualizar.current(0)
cbxActualizar.grid(row=0, column=5, padx=10, pady=10)

####################### menu fin actuazar billetes ######################


# Lanzar ventana
v.mainloop()

# Vea, los temas son: ciclo mientras, para, operación modulo, vectores y condicionales
