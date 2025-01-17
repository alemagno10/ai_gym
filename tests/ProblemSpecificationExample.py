from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State

class ProblemSpecification(State):

    def __init__(self, op, posRobo, s_esq, s_dir):
        # You must use this name for the operator!
        self.operator = op
        self.pos = posRobo
        self.situacaoEsq = s_esq
        self.situacaoDir = s_dir
    
    def sucessors(self):
        sucessors = []
        sucessors.append()
        return sucessors
    
    def is_goal(self):
        return True if self.situacaoEsq == "Limpo" and self.situacaoDir == "Limpo" and self.pos == "ESQ" else False
    
    def description(self):
        return "Implementa robo aspirador para dois quartos."
    
    def cost(self):
        return 1
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None


def main():
    print('Busca em profundidade iterativa')
    state = ProblemSpecification('')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()