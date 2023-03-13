from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
import copy

class Aspirador2x2(State):
    def __init__(self, op, pos, limpo):
        self.operator = op
        self.pos = pos
        self.limpo = limpo
    
    def sucessors(self):
        sucessors = []
        #walk
        if self.pos[0][0] == 1:
            sucessors.append(Aspirador2x2("Baixo", [[0,0],[1,0]], self.limpo))
            sucessors.append(Aspirador2x2("Direita", [[0,1],[0,0]], self.limpo))
        if self.pos[0][1] == 1:
            sucessors.append(Aspirador2x2("Baixo", [[0,0],[0,1]], self.limpo))
            sucessors.append(Aspirador2x2("Esquerda", [[1,0],[0,0]], self.limpo))
        if self.pos[1][0] == 1:
            sucessors.append(Aspirador2x2("Cima", [[1,0],[0,0]], self.limpo))
            sucessors.append(Aspirador2x2("Direita", [[0,1],[0,0]], self.limpo))
        if self.pos[1][1] == 1:
            sucessors.append(Aspirador2x2("Cima", [[1,0],[0,0]], self.limpo))
            sucessors.append(Aspirador2x2("Esquerda", [[1,0],[0,0]], self.limpo))
        
        #clean
        if self.pos[0][0] == 1:
            limpo = copy.deepcopy(self.limpo)
            limpo[0][0] = 1
            sucessors.append(Aspirador2x2("Limpa", self.pos, limpo))
        if self.pos[0][1] == 1:
            limpo = copy.deepcopy(self.limpo)
            limpo[0][1] = 1
            sucessors.append(Aspirador2x2("Limpa", self.pos, limpo))
        if self.pos[1][0] == 1:
            limpo = copy.deepcopy(self.limpo)
            limpo[1][0] = 1
            sucessors.append(Aspirador2x2("Limpa", self.pos, limpo))
        if self.pos[1][1] == 1:
            limpo = copy.deepcopy(self.limpo)
            limpo[1][1] = 1
            sucessors.append(Aspirador2x2("Limpa", self.pos, limpo))

        return sucessors

    def is_goal(self):
        return self.pos == [[1,0],[0,0]] and self.limpo == [[1,1],[1,1]]

    def description(self):
        return "Descrição do problema"
    
    def cost(self):
        return 1
    
    def env(self):
        return self.operator

def main():
    print('Busca em profundidade iterativa')
    state = Aspirador2x2('', [[1,0],[0,0]], [[1,0],[0,1]])
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()