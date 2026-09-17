from funciones import conversion_tiempo, pago_semanal, triangulo

def main():
    conversion_tiempo.leerSegundos(),conversion_tiempo.convertirTiempo(),conversion_tiempo.mostrarTiempo()
    

    pago_semanal.leerHorasTarifa(), pago_semanal.calcularPago(), pago_semanal.mostrarPago()

    triangulo.leerBaseAltura(), triangulo.calcularArea(), triangulo.mostrarArea()

if __name__ == "__main__":
    main()
