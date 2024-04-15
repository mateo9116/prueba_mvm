import tkinter as tk

def app():
    app = tk.Tk()
    app.geometry(newGeometry="700x700")
    tk.Wm.wm_title(app,string="Consulta base de datos SQL")
    tk.Button(master=app,text="Buscar").pack(fill=tk.X, expand=True)
    app.mainloop()