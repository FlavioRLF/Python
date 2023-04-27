'''
Busca Sequencial

def busca_sequencial(seq, x):
    #(list, float) -> bool
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False

'''
# Exemplo

class Musica:
    def __init__(self, titulo, compositor, ano):
        self.titulo = titulo
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, playlist, titulo):
        for i in range(len(playlist)):
            if playlist[i].titulo == titulo:
                return i
        return -1

    def vamos_buscar(self):
        playlist = [Musica("Fade to Black","James Hetfild", 1984)
        , Musica("Nothing Else Matters","James Hetfild", 1991)
        , Musica("Seek & Destroy","James Hetfild", 1982)]

        onde_achou = self.busca_por_titulo(playlist, "Fade to Black")

        if onde_achou == -1:
            print("A música não foi encontrada.")

        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.compositor, preferida.ano, sep=', ')



x = Buscador()

x.vamos_buscar()