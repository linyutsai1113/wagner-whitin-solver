# Wagner-Whitin Solver

This repository implements the **Wagner-Whitin algorithm**, a dynamic programming approach used to solve inventory optimization problems. It calculates the optimal production or ordering policy to minimize total costs (setup, holding, and production) over a finite time horizon.

## Features
- Solves the Wagner-Whitin inventory management problem.
- Supports fixed or variable setup costs, holding costs, and unit production costs.
- Returns cost matrices, optimal production quantities (`Q_t*`), and optimal decision periods (`j_t*`).

## Installation

Clone this repository:

```bash
git clone https://github.com/your-repo/wagner-whitin-solver.git
cd wagner-whitin-solver
```

## Usage

To use the Wagner-Whitin Solver, follow these steps in your Python code:

### Example
```python
from wagner_whitin_solver import WagnerWhitinSolver

# Define problem parameters
period = 10
period_demands = [20, 50, 10, 50, 50, 10, 20, 40, 20, 30]   # Demands for each period
setup_costs = [100]*period                                   # Fixed setup cost for all periods
unit_costs = [0]*period                                      # Fixed unit cost (optional: could be variable)
holding_costs = [1]*period                                   # Holding costs for each period

# Initialize the solver
ww = WagnerWhitinSolver(period, period_demands, setup_costs, unit_costs, holding_costs)

# Solve the problem
ww.solve()

# Display results
ww.get_cost_matrix()  # Get the cost matrix
ww.get_q_star()       # Get optimal production quantities
ww.get_j_t_star(9)    # Get optimal production decision for period 9
```
### Output
The solver generates a detailed cost matrix and returns the optimal production decisions and quantities.

#### Example Cost Matrix Output:
```
==========================================================================================
L_P\t    1        2        3        4        5        6        7        8        9        10      
1        100      150      170      320      0        0        0        0        0        0       
2        0        200      210      310      0        0        0        0        0        0       
3        0        0        250      300      0        0        0        0        0        0       
4        0        0        0        270      320      340      400      560      0        0       
5        0        0        0        0        370      380      420      540      0        0       
6        0        0        0        0        0        420      440      520      0        0       
7        0        0        0        0        0        0        440      480      520      610     
8        0        0        0        0        0        0        0        500      520      580     
9        0        0        0        0        0        0        0        0        580      610     
10       0        0        0        0        0        0        0        0        0        620     
------------------------------------------------------------------------------------------
Z_t:     100      150      170      270      320      340      400      480      520      580     
j_t:     1        1        1        4        4        4        4        7        (7, 8)   8       
==========================================================================================
```
#### Optimal Production Quantities (`Q_t*`):
```python
ww.get_q_star() 
>>> Q_t*:    {1: 80, 4: 130, 8: 90}
```
#### Optimal Production Decision (j_t*) for period 9:
``` 
ww.get_j_t_star(9)
>>> j_t* for 9 period problem:  (7, 8)
```
## Parameters
- period: Total number of periods.
- period_demands: List of demands for each period.
- setup_costs: List of setup costs for each period.
- unit_costs: List of unit production costs (fixed or variable).
- holding_costs: List of holding costs for each period.
## Methods
- solve(): Solves the Wagner-Whitin problem.
- get_cost_matrix(): Returns or prints the cost matrix.
- get_q_star(): Returns the optimal production quantities (Q_t*).
- get_j_t_star(index): Returns the optimal production decision for the given period (j_t*).