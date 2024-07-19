import mysql.connector
from mysql.connector import Error

class BibliotecaDAO:
    def __init__(self, db_config):
        """ Inicializa el DAO con la conexión a la base de datos """
        self.connection = self.create_connection(db_config)
        

    def create_connection(self, db_config):
        """ Crea una conexión a la base de datos MySQL """
        try:
            conn = mysql.connector.connect(**db_config)
            if conn.is_connected():
                print("Conexión establecida a la base de datos.")
            return conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    

    def insert_libro(self, libro):
        """ Inserta un libro en la tabla de libros """
        sql = ''' INSERT INTO Libros(codigo, titulo, autor, stock)
                  VALUES(%s, %s, %s, %s) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, libro)
            self.connection.commit()
            print("Libro agregado exitosamente.")
        except Error as e:
            print(f"Error al insertar libro: {e}")

    def select_libro_by_codigo(self, codigo):
        """ Selecciona un Libros por su código """
        sql = ''' SELECT * FROM libros WHERE codigo=%s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (codigo,))
            libro = cursor.fetchone()
            return libro
        except Error as e:
            print(f"Error al seleccionar libro: {e}")
            return None

    def update_libro_stock(self, codigo, stock):
        """ Actualiza el stock de un libro """
        sql = ''' UPDATE Libros
                  SET stock = %s
                  WHERE codigo = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (stock, codigo))
            self.connection.commit()
            print("Stock del libro actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar el stock del libro: {e}")

    def delete_libro(self, codigo):
        """ Elimina un libro por su código """
        sql = ''' DELETE FROM Libros WHERE codigo = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (codigo,))
            self.connection.commit()
            print("Libro eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar el libro: {e}")

    def insert_usuario(self, usuario):
        """ Inserta un usuario en la tabla de usuarios """
        sql = ''' INSERT INTO Usuario( tipo, nombre, rut, contacto, contraseña)
                  VALUES(%s, %s, %s, %s,%s) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, usuario)
            self.connection.commit()
            print("Usuario registrado exitosamente.")
        except Error as e:
            print(f"Error al insertar usuario: {e}")

    def registrar_deudor(self, rut_usuario):
        """ Registra un usuario como deudor en la tabla de deudores """
        sql = ''' INSERT INTO Deudores(Usuario_idUsuario)
                  VALUES(%s) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (rut_usuario,))
            self.connection.commit()
            print("Usuario registrado como deudor exitosamente.")
        except Error as e:
            print(f"Error al registrar deudor: {e}")

    def buscar_usuario_por_rut(self, rut):
        """ Busca un usuario por su rut """
        sql = ''' SELECT * FROM Usuario WHERE rut=%s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (rut,))
            usuario = cursor.fetchone()
            return usuario
        except Error as e:
            print(f"Error al buscar Usuario por rut: {e}")
            return None
    def insert_prestamo(self, libro_id, usuario_id, fecha_prestamo, fecha_devolucion):
        """ Inserta un nuevo préstamo en la tabla de préstamos """
        sql = ''' INSERT INTO Prestamos (Libro_codigo, Usuario_idUsuario, fecha_prestamo, fecha_devolucion)
                  VALUES (%s, %s, %s, %s, %s) '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (libro_id, usuario_id, fecha_prestamo, fecha_devolucion))
            self.connection.commit()
            print("Préstamo registrado exitosamente.")
        except Error as e:
            print(f"Error al registrar préstamo: {e}")

    def delete_prestamo(self, libro_id, usuario_id):
        """ Elimina un préstamo específico de la tabla de préstamos """
        sql = ''' DELETE FROM Prestamos WHERE codigo = %s AND idUsuario = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (libro_id, usuario_id))
            self.connection.commit()
            print("Préstamo eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar préstamo: {e}")

    def select_prestamos_by_libro(self, libro_id):
        """ Selecciona todos los préstamos asociados a un libro """
        sql = ''' SELECT * FROM Prestamos WHERE libro_codigo = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (libro_id,))
            prestamos = cursor.fetchall()
            return prestamos
        except Error as e:
            print(f"Error al seleccionar préstamos por libro: {e}")
            return None

    def select_prestamos_by_usuario(self, usuario_id):
        """ Selecciona todos los préstamos asociados a un usuario """
        sql = ''' SELECT * FROM Prestamos WHERE Usuario_idUsuario = %s '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (usuario_id,))
            prestamos = cursor.fetchall()
            return prestamos
        except Error as e:
            print(f"Error al seleccionar préstamos por usuario: {e}")
            return None