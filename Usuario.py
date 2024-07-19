class Usuario:
    def __init__(self, nombre, rut, contacto, tipo, contrasena, idUsuario: int=0):
        self.nombre = nombre
        self.rut = rut
        self.contacto = contacto
        self.tipo = tipo
        self.contrasena = contrasena
        self.idUsusario = idUsuario
        self.prestamos = []
        self.multa = 0

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def calcular_multa(self):
        return sum(p.multa for p in self.prestamos)

    def tiene_deudas(self):
        return any(p.retrasado() for p in self.prestamos) or self.calcular_multa() > 0

    def puede_prestar(self):
        if self.tipo == "estudiante":
            return len(self.prestamos) < 4 and not self.tiene_deudas()
        return not self.tiene_deudas()
