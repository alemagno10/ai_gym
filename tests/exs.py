from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
from datetime import datetime
import pandas as pd

class SumOne(State):

    def __init__(self, n, op, g):
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
    df = pd.DataFrame(columns=['Tempo', 'Resultado'])
    for i in range(1,56,5):
        state = SumOne(1, '', i)
        #algorithm = BuscaLargura()
        #algorithm = BuscaProfundidade()
        algorithm = BuscaProfundidadeIterativa()
        start_time = datetime.now()
        result = algorithm.search(state)
        end_time = datetime.now()
        df.loc[str(i)] = (end_time - start_time).microseconds
        print(f'Tempo de processamento = {end_time - start_time}')
        if result != None:
            print('Achou!')
            print(result.show_path())
            df.loc[str(i)] = [(end_time - start_time), "sim"]
        else:
            print('Nao achou solucao')
            df.loc[str(i)] = [(end_time - start_time), "não"]
    df.to_csv("profundidadeIterativa2", index=True)

if __name__ == '__main__':
    main()

