import tkinter as tk
from tkinter import messagebox
from Sistema import Sistema

class BibliotecaGUI:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Préstamos de Biblioteca")
        self.tipo_usuario = None   #Almacena el tipo de usuario logueado
        self.usuario_actual = None
        self.frame_contenido = tk.Frame(self.root, padx=20, pady=20)
        self.frame_contenido.pack(fill='both', expand=True)
        self.crear_menuinicio()

    def crear_menuinicio(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Bienvenido al Sistema de Préstamos de Biblioteca", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.frame_contenido, text="Iniciar Sesión", command=self.crear_pantalla_login, width=20, height=2).pack(pady=5)
        tk.Button(self.frame_contenido, text="Registrarse", command=self.interfaz_registrar_usuario, width=20, height=2).pack(pady=5)
    
    def limpiar_frame(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def crear_pantalla_login(self):
        self.limpiar_frame()
        rut = tk.StringVar()
        contrasena = tk.StringVar()
        
        tk.Label(self.frame_contenido, text="Iniciar Sesión", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT:", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.frame_contenido, textvariable= rut, width=30).pack(pady=5)
        

        tk.Label(self.frame_contenido, text="Contraseña:", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.frame_contenido, textvariable= contrasena, show='*', width=30).pack(pady=5)

        tk.Button(self.frame_contenido, text="Iniciar Sesión", command=lambda: self.iniciar_sesion(rut.get(), contrasena.get()), width=15).pack(pady=20)
        tk.Button(self.frame_contenido, text="Volver", command=self.crear_menuinicio, width=15).pack(pady=5)

    def interfaz_registrar_usuario(self):
        self.limpiar_frame()

        tk.Label(self.frame_contenido, text="Registrar Usuario", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame_contenido, text="Tipo de Usuario:", font=("Arial", 12)).pack()
        tipo_usuario_var = tk.StringVar(value="Seleccionar usuario")
        tk.OptionMenu(self.frame_contenido, tipo_usuario_var, "Estudiante", "Docente", "Administrador").pack()

        tk.Label(self.frame_contenido, text="Nombre:", font=("Arial", 12)).pack()
        nombre = tk.Entry(self.frame_contenido, width=30)
        nombre.pack(pady=5)

        tk.Label(self.frame_contenido, text="RUT:", font=("Arial", 12)).pack()
        rut = tk.Entry(self.frame_contenido, width=30)
        rut.pack(pady=5)

        tk.Label(self.frame_contenido, text="Contacto:", font=("Arial", 12)).pack()
        contacto = tk.Entry(self.frame_contenido, width=30)
        contacto.pack(pady=5)

        tk.Label(self.frame_contenido, text="Contraseña:", font=("Arial", 12)).pack()
        contrasena = tk.Entry(self.frame_contenido, show="*", width=30)
        contrasena.pack(pady=5)

        tk.Button(self.frame_contenido, text="Registrar", command=lambda: self.probar_registro(tipo_usuario_var.get(), nombre.get(), rut.get(), contacto.get(), contrasena.get()), width=15).pack(pady=20)
        tk.Button(self.frame_contenido, text="Volver", command=self.crear_menuinicio, width=15).pack(pady=5)

    def probar_registro(self, tipo, nombre, rut, contacto, contrasena):
        print(f"Tipo: {tipo}, Nombre: {nombre}, RUT: {rut}, Contacto: {contacto}, Contraseña: {contrasena}")
        self.registrar_usuario(tipo, nombre, rut, contacto, contrasena)

    def registrar_usuario(self, tipo, nombre, rut, contacto, contrasena):
        try:
            resultado = self.sistema.registrar_usuario(tipo, nombre, rut, contacto, contrasena)
            tk.messagebox.showinfo("Resultado", resultado)
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def iniciar_sesion(self, rut, contrasena):
        rut = rut.strip()
        contrasena = contrasena.strip()
        usuario = self.sistema.iniciar_sesion(rut, contrasena)
        if usuario:
            self.tipo_usuario = usuario['tipo']
            self.usuario_actual = usuario  # Asegúrate de establecer el usuario actual
            tk.messagebox.showinfo('Éxito', 'Inicio de Sesión Exitoso')
            self.crear_menu()
        else:
            tk.messagebox.showerror("Error", "RUT o contraseña incorrectos")


    def crear_menu(self):
        #print(f'Tipo de Usuario: {self.tipo_usuario}')  Debug: imprimir tipo de usuario.
        self.limpiar_frame()
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        volver_menu = tk.Menu(self.menu, tearoff=0)
        volver_menu.add_command(label="Volver", command=self.crear_menuinicio)
        self.menu.add_cascade(label="Opciones", menu=volver_menu)

        if self.tipo_usuario == "Administrador":
            self.libros_menu = tk.Menu(self.menu, tearoff=0)
            self.usuarios_menu = tk.Menu(self.menu, tearoff=0)
            self.prestamos_menu = tk.Menu(self.menu, tearoff=0)
            
            self.menu.add_cascade(label="Libros", menu=self.libros_menu)
            self.menu.add_cascade(label="Usuarios", menu=self.usuarios_menu)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            
            self.libros_menu.add_command(label="Agregar Libro", command=self.agregar_libro)
            self.libros_menu.add_command(label="Modificar Stock", command=self.modificar_stock_libro)
            
            
            self.usuarios_menu.add_command(label="Buscar Usuario", command=self.buscar_usuario)
            
            
            self.prestamos_menu.add_command(label="Aplicar Multa", command=self.aplicar_multa)
        
        elif self.tipo_usuario == "Docente":
            self.prestamos_menu = tk.Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.prestar_libro)
            self.prestamos_menu.add_command(label="Devolver Libro", command=self.devolver_libro)
            self.prestamos_menu.add_command(label="Pagar Multa", command=self.pagar_multa_docente)

        elif self.tipo_usuario == "Estudiante":
            self.prestamos_menu = tk.Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label="Préstamos", menu=self.prestamos_menu)
            self.prestamos_menu.add_command(label="Realizar Préstamo", command=self.prestar_libro)
            self.prestamos_menu.add_command(label="Devolver Libro", command=self.devolver_libro)
            self.prestamos_menu.add_command(label="Pagar Multa", command=self.pagar_multa_estudiante)
        

    def agregar_libro(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Agregar Libro", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.frame_contenido, text="Código:", font=("Arial", 12)).grid(row=1, column=0, sticky='e')
        tk.Label(self.frame_contenido, text="Título:", font=("Arial", 12)).grid(row=2, column=0, sticky='e')
        tk.Label(self.frame_contenido, text="Autor:", font=("Arial", 12)).grid(row=3, column=0, sticky='e')
        tk.Label(self.frame_contenido, text="Stock:", font=("Arial", 12)).grid(row=4, column=0, sticky='e')

        codigo = tk.Entry(self.frame_contenido, width=30)
        titulo = tk.Entry(self.frame_contenido, width=30)
        autor = tk.Entry(self.frame_contenido, width=30)
        stock = tk.Entry(self.frame_contenido, width=30)

        codigo.grid(row=1, column=1)
        titulo.grid(row=2, column=1)
        autor.grid(row=3, column=1)
        stock.grid(row=4, column=1)

        tk.Button(self.frame_contenido, text="Agregar", command=lambda: self.guardar_libro(codigo.get(), titulo.get(), autor.get(), stock.get()), width=15).grid(row=5, columnspan=2, pady=10)

    def guardar_libro(self, codigo, titulo, autor, stock):
        try:
            resultado = self.sistema.registrar_libro(codigo, titulo, autor, int(stock))
            messagebox.showinfo("Éxito", resultado)
            self.crear_menu()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def modificar_stock_libro(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Modificar Stock", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="Código del Libro:", font=("Arial", 12)).pack(pady=5)
        codigo = tk.Entry(self.frame_contenido, width=30)
        codigo.pack(pady=5)

        tk.Label(self.frame_contenido, text="Nuevo Stock:", font=("Arial", 12)).pack(pady=5)
        nuevo_stock = tk.Entry(self.frame_contenido, width=30)
        nuevo_stock.pack(pady=5)

        tk.Button(self.frame_contenido, text="Modificar", command=lambda: self.guardar_modificacion_stock(codigo.get(), nuevo_stock.get()), width=15).pack(pady=20)

    def guardar_modificacion_stock(self, codigo, nuevo_stock):
        try:
            resultado = self.sistema.modificar_stock_libro(codigo, int(nuevo_stock))
            messagebox.showinfo("Éxito", resultado)
            self.crear_menu()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def prestar_libro(self):
        rut_usuario = tk.StringVar()
        codigo_libro = tk.StringVar()
        dias_prestamo = tk.StringVar()
        self.limpiar_frame()

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.frame_contenido, textvariable= rut_usuario, width=30).pack(pady=5)
      
        tk.Label(self.frame_contenido, text="Código del Libro:", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.frame_contenido, textvariable= codigo_libro, width=30).pack(pady=5)
        
        tk.Label(self.frame_contenido, text="Días de Préstamo:", font=("Arial", 12)).pack(pady=5)
        tk.Entry(self.frame_contenido, textvariable= dias_prestamo, width=30).pack(pady=5)
        

        tk.Button(self.frame_contenido, text="Prestar", command=lambda: self.procesar_prestamo(rut_usuario.get(), codigo_libro.get(), dias_prestamo.get()), width=15).pack(pady=20)

    def procesar_prestamo(self, rut_usuario, codigo_libro, dias_prestamo): 
        exito = self.sistema.prestar_libro(rut_usuario, codigo_libro, int(dias_prestamo))
        if exito == 'Prestamo Exitoso':
            tk.messagebox.showinfo("Éxito", "Préstamo realizado correctamente")
            self.crear_menu()
        else:
            tk.messagebox.showerror("Error", 'No se ha podido realizar el Prestamo.')

    def registrar_pago_multa(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Registrar Pago de Multa", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        rut_usuario = tk.Entry(self.frame_contenido, width=30)
        rut_usuario.pack(pady=5)

        tk.Label(self.frame_contenido, text="Monto a Pagar:", font=("Arial", 12)).pack(pady=5)
        monto_pagar = tk.Entry(self.frame_contenido, width=30)
        monto_pagar.pack(pady=5)

        tk.Button(self.frame_contenido, text="Registrar Pago", command=lambda: self.procesar_pago_multa(rut_usuario.get(), float(monto_pagar.get())), width=15).pack(pady=20)

    def procesar_pago_multa(self, rut_usuario, monto_pagar):
        if self.usuario_actual is None:
            messagebox.showwarning("Error", "No hay usuario actual")
            return

        rut_usuario = self.usuario_actual.get('rut')
        if rut_usuario:
            exito = self.sistema.registrar_pago_multa(rut_usuario, monto_pagar)
            if exito:
                messagebox.showinfo("Éxito", "Pago registrado correctamente")
                self.crear_menu()
            else:
                messagebox.showwarning("Error", "No se pudo registrar el pago")
        else:
            messagebox.showwarning("Error", "Usuario no tiene un RUT válido")

    def aplicar_multa(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Aplicar Multa", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        rut_usuario = tk.Entry(self.frame_contenido, width=30)
        rut_usuario.pack(pady=5)

        tk.Label(self.frame_contenido, text="Código del Libro:", font=("Arial", 12)).pack(pady=5)
        codigo_libro = tk.Entry(self.frame_contenido, width=30)
        codigo_libro.pack(pady=5)

        tk.Label(self.frame_contenido, text="Monto de la Multa:", font=("Arial", 12)).pack(pady=5)
        monto_multa = tk.Entry(self.frame_contenido, width=30)
        monto_multa.pack(pady=5)

        # Corrección: llamar al método `procesar_aplicar_multa` con los argumentos correctos
        tk.Button(self.frame_contenido, text="Aplicar Multa", command=lambda: self.procesar_aplicar_multa(rut_usuario.get(), codigo_libro.get(), float(monto_multa.get())), width=15).pack(pady=20)

    def procesar_aplicar_multa(self, rut_usuario, codigo_libro, monto_multa):
     
        exito = self.sistema.aplicar_multa(rut_usuario, codigo_libro, monto_multa)
        if exito:
            messagebox.showinfo("Éxito", "Multa aplicada correctamente")
            self.crear_menu()
        else:
            messagebox.showwarning("Error", "No se pudo aplicar la multa")

    def devolver_libro(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Devolver Libro", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        rut_usuario = tk.Entry(self.frame_contenido, width=30)
        rut_usuario.pack(pady=5)

        tk.Label(self.frame_contenido, text="Código del Libro:", font=("Arial", 12)).pack(pady=5)
        codigo_libro = tk.Entry(self.frame_contenido, width=30)
        codigo_libro.pack(pady=5)

        tk.Button(self.frame_contenido, text="Devolver", command=lambda: self.procesar_devolucion(rut_usuario.get(), codigo_libro.get()), width=15).pack(pady=20)


    def procesar_devolucion(self,rut_usuario ,codigo_libro):
        exito = self.sistema.devolver_prestamo( rut_usuario ,codigo_libro)
        if exito:
            tk.messagebox.showinfo("Éxito", "Libro devuelto correctamente")
            self.crear_menu()
        else:
            tk.messagebox.showwarning("Error", "No se pudo devolver el libro")

    def pagar_multa_docente(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Pagar Multa (Docente)", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="Monto de la Multa:", font=("Arial", 12)).pack(pady=5)
        monto_multa = tk.Entry(self.frame_contenido, width=30)
        monto_multa.pack(pady=5)

        tk.Button(self.frame_contenido, text="Pagar", command=lambda: self.procesar_pago_multa(self.usuario_actual['rut'], float(monto_multa.get())), width=15).pack(pady=20)

    def pagar_multa_estudiante(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Pagar Multa (Estudiante)", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="Monto de la Multa:", font=("Arial", 12)).pack(pady=5)
        monto_multa = tk.Entry(self.frame_contenido, width=30)
        monto_multa.pack(pady=5)

        tk.Button(self.frame_contenido, text="Pagar", command=lambda: self.procesar_pago_multa(self.usuario_actual['rut'], float(monto_multa.get())), width=15).pack(pady=20)

    def buscar_usuario(self):
        self.limpiar_frame()
        tk.Label(self.frame_contenido, text="Buscar Usuario", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_contenido, text="RUT del Usuario:", font=("Arial", 12)).pack(pady=5)
        rut_usuario = tk.Entry(self.frame_contenido, width=30)
        rut_usuario.pack(pady=5)

        tk.Button(self.frame_contenido, text="Buscar", command=lambda: self.procesar_busqueda_usuario(rut_usuario.get()), width=15).pack(pady=20)
    def procesar_busqueda_usuario(self, rut_usuario):
        usuario = self.sistema.buscar_usuario(rut_usuario)
        if usuario:
            info_usuario = f"Tipo: {usuario['tipo']}\nNombre: {usuario['nombre']}\nRUT: {usuario['rut']}\nContacto: {usuario['contacto']}"
            messagebox.showinfo("Usuario Encontrado", info_usuario)
        else:
            messagebox.showwarning("Error", "Usuario no encontrado")

# Crear una instancia del sistema y de la interfaz gráfica
if __name__ == '__main__':
    sistema = Sistema()
    root = tk.Tk()
    app = BibliotecaGUI(root, sistema)
    root.mainloop()
