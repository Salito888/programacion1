from fastapi import HTTPException

from api.model.cuenta_model import CuentaBancaria, CuentaAhorro, CuentaCorriente, TipoCuenta

# Lista simulada de cuentas
cuentas_bancarias = [
    CuentaAhorro(id=1, nombre="Carlos", balance=1000, tipo=TipoCuenta.ahorro, tasa_interes=0.03),
    CuentaCorriente(id=2, nombre="Ana", balance=500, tipo=TipoCuenta.corriente, limite_descubierto=200),
]

def obtener_cuenta_por_id(cuenta_id: int) -> CuentaBancaria:
    for cuenta in cuentas_bancarias:
        if cuenta.id == cuenta_id:
            return cuenta
        raise
    HTTPException(status_code=404,detail="Cuenta no encontrada")





