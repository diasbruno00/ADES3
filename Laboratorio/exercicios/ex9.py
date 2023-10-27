

class Estudent:

    def __init__(self, nome, nota, freq) -> None:
            self.nome = nome
            self.nota = nota
            self.freq = freq
        
    def is_approved(self):
        if self.nota >= 6 and self.freq >= 6:
            return True
        else:
            return False
        

    

s1 = Estudent('Bruno', 10, 10)

print(s1.is_approved())