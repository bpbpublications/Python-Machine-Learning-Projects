### 1. Import Libraries
import numpy as np
from sko.GA import GA, GA_TSP
from sko.operators import ranking, selection, crossover, mutation
### 2. Create Demo function
demo_func = lambda x: x[0] ** 2 + (x[1] - 0.05) ** 2 + (x[2] - 0.5) ** 2
### 3. Setup the GA environment
ga = GA(func=demo_func, n_dim=3, size_pop=100, max_iter=500, prob_mut=0.001,lb=[-1, -10, -5], ub=[2, 10, 2], precision=[1e-7, 1e-7, 1])
ga.register(operator_name='selection',operator=selection_tournament, tourn_size=3)
ga.register(operator_name='ranking', operator=ranking.ranking). \
    register(operator_name='crossover', operator=crossover.crossover_2point). \
    register(operator_name='mutation', operator=mutation.mutation)
### 4.Execute the call to GA function
best_x, best_y = ga.run()
### 5. Print the optimal solution
print('best_x:', best_x, '\n', 'best_y:', best_y)
