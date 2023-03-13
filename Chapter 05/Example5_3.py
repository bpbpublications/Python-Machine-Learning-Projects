### 1. Import libraries
import numpy as np
from mealpy.swarm_based import WOA
from models.tsp_model import TravellingSalesmanProblem
from models.tsp_solution import generate_stable_solution, generate_unstable_solution
### 2. Define data
np.random.seed(10)
N_CITIES = 15
CITY_POSITIONS = np.random.rand(N_CITIES, 2)
TSP = TravellingSalesmanProblem(n_cities=N_CITIES, city_positions=CITY_POSITIONS)
TSP.plot_cities(pathsave="./results/WOA-TSP", filename="cities_map")
### 3. Design problem dictionary
## Let's take the function that can generate stable solution
LB = [0, ] * TSP.n_cities
UB = [(TSP.n_cities - 0.01), ] * TSP.n_cities
problem = {
    "fit_func": TSP.fitness_function,
    "lb": LB,
    "ub": UB,
    "minmax": "min",        # Trying to find the minimum distance
    "log_to": "console",
    "amend_position": generate_stable_solution
}
solution = np.array([1, 5, 9, 7, 8, 0, 2, 4, 6, 3])
fit_value = TSP.fitness_function(solution)
optimal_solution = np.array([6, 4, 0, 10, 2, 8, 12, 13, 14, 7, 9, 5, 1, 11, 3])
optimal_dist = TSP.fitness_function(optimal_solution)
### 4. Call the model
model = WOA.BaseWOA(problem, epoch=10, pop_size=50) 
### 5. Train the model
best_position, best_fitness = model.solve()
### 6. Show the results
print(f"Best solution: {best_position}, Obj = Total Distance: {best_fitness}")
