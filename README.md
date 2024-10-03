# wagner_whitin_solver

## example usage
```python
from wagner_whitin_solver import WagnerWhitinSolver

period = 10
period_demands = [20, 50, 10, 50, 50, 10, 20, 40, 20, 30]
setup_costs = [100]*period # fixed setup cost case 
unit_costs = [0]*period # fixed unit cost case 
holding_costs = [1]*period # fixed holding cost case 
ww = WagnerWhitinSolver(period, period_demands, setup_costs, unit_costs, holding_costs)

ww.solve() 
```
Output:
```
ww.get_cost_matrix() >>>
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

ww.get_q_star()
>>> Q_t*:    {1: 80, 4: 130, 8: 90}

ww.get_j_t_star(9)
>>> j_t* for 9 period problem:  (7, 8)
```
