class Libro:
    def __init__(self,titulo, autor, stock, codigo:int =0):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
        self.historico = []

   

    def prestamo_disponible(self):
        return self.stock > 0

    def registrar_prestamo(self, prestamo):
        if self.prestamo_disponible():
            self.stock -= 1
            self.historico.append(prestamo)

    def devolver(self):
        self.stock += 1
