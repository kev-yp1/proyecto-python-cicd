def calcular_area(base, altura):
    # Valida que base y altura sean positivos (Punto 18)
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser valores positivos")
    return base + altura