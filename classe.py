class Polynome:
    def __init__(self, coefficients):
        # Les coefficients sont stockés du terme constant jusqu'au terme de plus haut degré
        self.coefficients = coefficients

    def __str__(self):
        # Permet de convertir le polynôme en une chaîne de caractères lisible
        result = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                term = f"{coef}x^{i}" if i > 0 else str(coef)
                if i == 1:
                    term = f"{coef}x"
                result.append(term)
        return " + ".join(result[::-1]).replace(" + -", " - ")

    def evaluate(self, x):
        # Calcule la valeur du polynôme pour une valeur donnée de x
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
        return result

# Programme principal
if __name__ == "__main__":
    # Création du polynôme p(x) = 0.1x^4 + 0.1x^3 - 1.3x^2 - 0.1x + 1.2
    p = Polynome([1.2, -0.1, -1.3, 0.1, 0.1])

    # Affichage du polynôme
    print("Polynôme p(x):", p)

    # Évaluation du polynôme en différents points
    points = [0, 1, -1, 2]
    for x in points:
        print(f"p({x}) = {p.evaluate(x)}")
