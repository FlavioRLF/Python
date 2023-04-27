class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        p = self.a + self.b + self.c
        p = int(p)
        return p 