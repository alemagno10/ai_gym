from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
from datetime import datetime
import pandas as pd

class SumOne(State):

    def _init_(self, n, op, g):
        self.operator = op
        self.number = n
        self.goal = g

    def sucessors(self):
        sucessors = []
        if self.number < self.goal:
            sucessors.append(SumOne(self.number+1, "+1 ", self.goal))
            sucessors.append(SumOne(self.number+2, "+2 ", self.goal))
        return sucessors

    def is_goal(self):
        if self.goal == self.number:
            return True
        return False

    def description(self):
        return "Este é um agente simples que sabe somar 1 e 2"

    def cost(self):
        return 1

    def env(self):
        return self.number
    
def main():
    # criar um DataFrame para armazenar os resultados
    df = pd.DataFrame(columns=['Algoritmo', 'Objetivo', 'Tempo de processamento', 'Achou solucao?'])

    # definir os valores iniciais
    start = 1
    end = 50

    for objetivo in range(start, end+1):
        state = SumOne(1, '', objetivo)
        algorithm = BuscaProfundidadeIterativa()
        start_time = datetime.now()
        result = algorithm.search(state)
        end_time = datetime.now()
        tempo = (end_time - start_time).microseconds
        if result != None:
            pass
        else:
            pass
        # colocar os resultados no df
        df.loc[len(df)] = ['Busca em Profundidade Iterativa', objetivo, tempo, result != None]

    # salvar o df em um arquivo csv
    df.to_csv('dados_profundidade_iterativa.csv', index=False)

if __name__ == '__main__':
    main()