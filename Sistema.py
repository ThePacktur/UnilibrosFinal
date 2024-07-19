class Sistema:
    def __init__(self):
        
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []
        self.multa = []

    def registrar_libro(self, codigo, titulo, autor, stock):
        if codigo in self.libros:
            return 'Libro ya registrado.'
        registro_libro = {'titulo': titulo, 'autor': autor, 'stock': stock, 'historico': []}
        self.libros[codigo] = registro_libro
        return 'Libro registrado con éxito.'

    def registrar_usuario(self, tipo, nombre, rut, contacto, contrasena):
        if rut in self.usuarios:
           return 'El usuario ya esta Registrado'
       
        nuevo_usuario = {'tipo': tipo, 'nombre': nombre, 'rut': rut, 'contacto': contacto, 'contrasena': contrasena, 'multa': 0, 'prestamos': []}
        self.usuarios[rut] = nuevo_usuario
        print(f"Usuario registrado: {self.usuarios[rut]}")  # Debug: imprimir usuario registrado
        return 'Registro Exitoso'

    def iniciar_sesion(self, rut, contrasena):
        usuario = self.buscar_usuario(rut)
        if usuario is not None and usuario['contrasena'] == contrasena:
            self.usuario_actual = usuario
            return usuario  
        return None

    def prestar_libro(self, rut_usuario, codigo_libro, dias_prestamo):
        usuario = self.buscar_usuario(rut_usuario)
        if usuario and codigo_libro in self.libros and self.libros[codigo_libro]['stock'] > 0:
            self.libros[codigo_libro]['stock'] -= 1
            if 'prestamos' not in usuario:
                usuario['prestamos'] = []
            usuario['prestamos'].append({'codigo_libro': codigo_libro, 'dias_prestamo': dias_prestamo})
            return "Prestamo realizado Correstamente"
        return "Error al Realizar el prestamo"

    def devolver_prestamo(self, rut, codigo_libro):
        usuario = self.buscar_usuario(rut)
        if usuario:
            for prestamo in usuario['prestamos']:
                if prestamo['codigo_libro'] == codigo_libro:
                    self.libros[codigo_libro]['stock'] += 1
                    usuario['prestamos'].remove(prestamo)
                    return True
        return False
    
    def buscar_libro(self, codigo):
        return self.libros.get(codigo, None)

    def buscar_usuario(self, rut):
        return self.usuarios.get(rut, None)
    
    def registrar_pago_multa(self, rut, monto_multa):
        usuario = self.buscar_usuario(rut)
        if usuario:
        # Asegúrate de que 'multa' existe y no es menor que el monto a pagar
            if 'multa' in usuario and usuario['multa'] >= monto_multa:
                usuario['multa'] -= monto_multa
                return True
            else:
                return False
        return False

    def modificar_stock_libro(self, codigo, nuevo_stock):
        if codigo in self.libros:
            # Verifica que self.libros[codigo] sea un diccionario antes de modificar
            libro = self.libros[codigo]
            if isinstance(libro, dict):
                libro['stock'] = nuevo_stock
                print(f'Se ha modificado: {libro}')  # Mostrar el libro modificado
                return 'Stock modificado con éxito.'
            else:
                return 'El registro del libro está corrupto.'
        else:
            return 'El código del libro no existe.'

    def aplicar_multa(self, rut,codigo_libro,monto_multa):
        usuario = self.buscar_usuario(rut)
        if usuario:
            if 'multas' not in usuario:
                usuario['multas'] = {}
            if codigo_libro not in usuario['multas']:
                usuario['multas'][codigo_libro] = 0
            usuario['multas'][codigo_libro] += monto_multa
        
            return True
        return False
