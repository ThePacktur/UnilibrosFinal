from tkinter import Tk
from Bibliotecagui import BibliotecaGUI
from Sistema import Sistema
from BibliotecaDAO import BibliotecaDAO

db_config = {
    'host': 'srv8.cpanelhost.cl',
    'user': 'cun102652_SPGN2024',
    'password': 'unilibrostrabajofinal',
    'database': 'cun102652_UniLibros',
    'port': 21
}

if __name__ == "__main__":
    try:
        dao = BibliotecaDAO(db_config)
        sistema = Sistema(dao)  # Inicializa el sistema con la instancia de BibliotecaDAO
        root = Tk()
        app = BibliotecaGUI(root, sistema)
        root.mainloop()
    except Exception as e:
        print(f"No se pudo conectar a la base de datos: {e}")