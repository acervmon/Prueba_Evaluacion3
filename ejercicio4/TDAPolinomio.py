class Nodo(object):
    def __init__(self):
        self.info, self.sig = None, None

    class Polinomio(object):
        def __init__(self):
            self.coeficientes = []

        def agregar_termino(self, coeficiente):
            self.coeficientes.append(coeficiente)

        def evaluar(self, x):
            resultado = 0
            for i, coeficiente in enumerate(self.coeficientes):
                resultado += coeficiente * (x ** i)
            return resultado


    polinomio = Polinomio()
    grado = int(input("Ingrese el grado del polinomio: "))
    for i in range(grado + 1):
        coeficiente = float(input(f"Ingrese el coeficiente para x^{i}: "))
        polinomio.agregar_termino(coeficiente)

    valor_x = float(input("Ingrese el valor de x para evaluar el polinomio: "))
    resultado = polinomio.evaluar(valor_x)
    print(f"El resultado de evaluar el polinomio en x = {valor_x} es: {resultado}")

    # Crear otro polinomio
    polinomio2 = Polinomio()
    grado2 = int(input("Ingrese el grado del segundo polinomio: "))
    for i in range(grado2 + 1):
        coeficiente = float(input(f"Ingrese el coeficiente para x^{i} del segundo polinomio: "))
        polinomio2.agregar_termino(coeficiente)

    # Sumar los polinomios
    polinomio_suma = Polinomio()
    for i in range(max(grado, grado2) + 1):
        coeficiente1 = polinomio.coeficientes[i] if i <= grado else 0
        coeficiente2 = polinomio2.coeficientes[i] if i <= grado2 else 0
        polinomio_suma.agregar_termino(coeficiente1 + coeficiente2)

    # Restar los polinomios
    polinomio_resta = Polinomio()
    for i in range(max(grado, grado2) + 1):
        coeficiente1 = polinomio.coeficientes[i] if i <= grado else 0
        coeficiente2 = polinomio2.coeficientes[i] if i <= grado2 else 0
        polinomio_resta.agregar_termino(coeficiente1 - coeficiente2)

    # Multiplicar los polinomios
    polinomio_multiplicacion = Polinomio()
    for i in range(grado + grado2 + 1):
        coeficiente = 0
        for j in range(i + 1):
            coeficiente1 = polinomio.coeficientes[j] if j <= grado else 0
            coeficiente2 = polinomio2.coeficientes[i - j] if i - j <= grado2 else 0
            coeficiente += coeficiente1 * coeficiente2
        polinomio_multiplicacion.agregar_termino(coeficiente)

    # Dividir los polinomios
    polinomio_division = Polinomio()
    if grado2 > grado:
        print("No se puede realizar la división, el grado del segundo polinomio es mayor")
    else:
        for i in range(grado - grado2 + 1):
            coeficiente = polinomio.coeficientes[i] / polinomio2.coeficientes[0]
            polinomio_division.agregar_termino(coeficiente)

    # Imprimir resultados
    print("Polinomio 1:", polinomio.coeficientes)
    print("Polinomio 2:", polinomio2.coeficientes)
    print("Suma:", polinomio_suma.coeficientes)
    print("Resta:", polinomio_resta.coeficientes)
    print("Multiplicación:", polinomio_multiplicacion.coeficientes)
    print("División:", polinomio_division.coeficientes)
