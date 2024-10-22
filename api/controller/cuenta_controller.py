from fastapi import APIRouter, HTTPException
from api.model.cuenta_model import CuentaAhorro, CuentaCorriente
from api.service.cuenta_service import obtener_cuenta_por_id

router = APIRouter()

# 1. Mostrar saldo actual
@router.get("/{cuenta_id}/saldo")
def mostrar_saldo(cuenta_id: int):
    cuenta = obtener_cuenta_por_id(cuenta_id)
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return {"saldo": cuenta.mostrar_saldo()}

# 2. Mostrar interés aplicado (solo para cuentas de ahorro)
@router.get("/{cuenta_id}/interes")
def mostrar_interes(cuenta_id: int):
    cuenta = obtener_cuenta_por_id(cuenta_id)
    if not cuenta or not isinstance(cuenta, CuentaAhorro):
        raise HTTPException(status_code=404, detail="Cuenta de ahorro no encontrada")
    return cuenta.mostrar_interes()

# 3. Mostrar límite de descubierto (solo para cuentas corrientes)
@router.get("/{cuenta_id}/limite_descubierto")
def mostrar_limite_descubierto(cuenta_id: int):
    cuenta = obtener_cuenta_por_id(cuenta_id)
    if not cuenta or not isinstance(cuenta, CuentaCorriente):
        raise HTTPException(status_code=404, detail="Cuenta corriente no encontrada")
    return cuenta.mostrar_limite_descubierto()

# 4. Mostrar información del titular
@router.get("/{cuenta_id}/info_titular")
def mostrar_info_titular(cuenta_id: int):
    cuenta = obtener_cuenta_por_id(cuenta_id)
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return cuenta.mostrar_info_titular()
