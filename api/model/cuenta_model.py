from pydantic import BaseModel
from enum import Enum

# Se definen los tipos de cuenta como un enumerador
class TipoCuenta(str, Enum):
    ahorro = "Ahorro"
    corriente = "Corriente"

# Clase base con atributos comunes
class CuentaBancaria(BaseModel):
    id: int
    nombre: str
    balance: float
    tipo: TipoCuenta

    def mostrar_saldo(self):
        return self.balance

    def mostrar_info_titular(self):
        return {"nombre": self.nombre, "balance": self.balance}

# Subclase CuentaAhorro, hereda de CuentaBancaria
class CuentaAhorro(CuentaBancaria):
    tasa_interes: float

    def mostrar_interes(self):
        interes = self.balance * self.tasa_interes
        nuevo_saldo = self.balance + interes
        return {"interes_acumulado": interes, "nuevo_saldo": nuevo_saldo}

# Subclase CuentaCorriente, hereda de CuentaBancaria
class CuentaCorriente(CuentaBancaria):
    limite_descubierto: float

    def mostrar_limite_descubierto(self):
        return {"limite_descubierto": self.limite_descubierto}






