import tkinter as tk
from tkinter import messagebox

from api_service import consultar_ruc, consultar_dni


def buscar_ruc():

    text_rpta_ruc.config(state="normal")
    text_rpta_ruc.delete("1.0", tk.END)

    try:

        res = consultar_ruc(entry_ruc.get())

        text_rpta_ruc.insert(
            tk.END,
            f"Nombre: {res.nombre}\n"
            f"Estado: {res.estado}\n"
            f"Condición: {res.condicion}\n"
            f"Dirección: {res.direccion}\n"
            f"Distrito: {res.distrito}\n"
            f"Departamento: {res.departamento}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

    finally:
        text_rpta_ruc.config(state="disabled")


def buscar_dni():

    text_rpta_dni.config(state="normal")
    text_rpta_dni.delete("1.0", tk.END)

    try:

        res = consultar_dni(entry_dni.get())

        text_rpta_dni.insert(
            tk.END,
            f"Nombre: {res.nombre}\n"
            f"Nombres: {res.nombres}\n"
            f"Apellido Paterno: {res.apellidoPaterno}\n"
            f"Apellido Materno: {res.apellidoMaterno}\n"
            f"N° Documento: {res.numeroDocumento}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

    finally:
        text_rpta_dni.config(state="disabled")


ventana = tk.Tk()
ventana.title("Consulta API – DNI y RUC")
ventana.geometry("500x420")

frame_ruc = tk.LabelFrame(ventana, text="Consulta RUC")
frame_ruc.pack(fill="x", padx=10, pady=10)

tk.Label(frame_ruc, text="Número RUC").grid(row=0, column=0)

entry_ruc = tk.Entry(frame_ruc)
entry_ruc.grid(row=0, column=1)

tk.Button(frame_ruc, text="Buscar", command=buscar_ruc).grid(row=0, column=2)

text_rpta_ruc = tk.Text(frame_ruc, height=5, state="disabled")
text_rpta_ruc.grid(row=1, column=0, columnspan=3)


frame_dni = tk.LabelFrame(ventana, text="Consulta DNI")
frame_dni.pack(fill="x", padx=10, pady=10)

tk.Label(frame_dni, text="Número DNI").grid(row=0, column=0)

entry_dni = tk.Entry(frame_dni)
entry_dni.grid(row=0, column=1)

tk.Button(frame_dni, text="Buscar", command=buscar_dni).grid(row=0, column=2)

text_rpta_dni = tk.Text(frame_dni, height=5, state="disabled")
text_rpta_dni.grid(row=1, column=0, columnspan=3)

ventana.mainloop()