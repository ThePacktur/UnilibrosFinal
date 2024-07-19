from datetime import datetime, timedelta

class Prestamo:
    MULTA_POR_DIA = 1000

    def __init__(self, libro, usuario, fecha_prestamo):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = self.calcular_fecha_devolucion()
        self.renovaciones = 0

    def calcular_fecha_devolucion(self):
        if self.usuario.tipo == "estudiante":
            return self.fecha_prestamo + timedelta(days=7)
        elif self.usuario.tipo == "docente":
            return self.fecha_prestamo + timedelta(days=20)

    def renovar(self):
        if self.usuario.tipo == "estudiante" and self.renovaciones < 1:
            self.fecha_devolucion += timedelta(days=3)
            self.renovaciones += 1
        elif self.usuario.tipo == "docente" and self.renovaciones < 3:
            self.fecha_devolucion += timedelta(days=7)
            self.renovaciones += 1

    def retrasado(self):
        return datetime.now().date() > self.fecha_devolucion

    @property
    def multa(self):
        if self.retrasado():
            dias_retraso = (datetime.now().date() - self.fecha_devolucion).days
            return dias_retraso * self.MULTA_POR_DIA
        return 0