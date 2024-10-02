class WagnerWhitinSolver():
    def __init__(self, period=0, period_demands=[], setup_costs=[], unit_costs=[], holding_costs=[]) :
        self.period = period
        self.period_demands = period_demands
        self.setup_costs = setup_costs
        self.unit_costs = unit_costs
        self.holding_costs = holding_costs
        self.cost_matrix = [[0]*period for _ in range(period)] 
        self.j_ts = [0]*period
        self.z_stars = [0]*period

    def solve(self):
        last_produced_time = 0 
        i = 0 # i = time_period (column)
        while i < self.period:
            if i == 0:
                self.cost_matrix[i][0] = self.setup_costs[0] + self.unit_costs[0] * self.period_demands[0]
                self.z_stars[0] = self.cost_matrix[i][0]
                self.j_ts[0] = 1
                i += 1
            else:
                for j in range(last_produced_time, i+1): # j = last_produced_time (row)
                    previous_min_cost = self.z_stars[j-1]
                    setup_cost = self.setup_costs[j]
                    produce_cost = self.unit_costs[j] * sum(self.period_demands[k] for k in range(j, i+1))
                    holding_cost = 0
                    for k in range(j, i):
                        if k+1 <= i:
                            holding_cost += sum(self.holding_costs[j:k+1]) * self.period_demands[k+1] 
                    self.cost_matrix[j][i] = previous_min_cost + setup_cost + produce_cost + holding_cost 
                    self.z_stars[i] = min((self.cost_matrix[j][i] for j in range(last_produced_time, i+1)))

                j_t_tuple = [] 
                for j in range(last_produced_time, i+1):  
                    if self.z_stars[i] == self.cost_matrix[j][i]:
                        j_t_tuple.append(j+1)
                        if len(j_t_tuple) >= 2:
                            break # incase of tie in z_stars, still need to find the z value of the tie in next period
                        last_produced_time = j 
                
                if len(j_t_tuple) >= 2: # tie in z_stars
                    self.j_ts[i] = tuple(j_t_tuple)
                else:
                    self.j_ts[i] = j_t_tuple[0]
                i+=1
        
    # print cost matrix and z_stars and j_ts
    def get_cost_matrix(self):
        print('='*period*9)
        print('L_P\\t   ', end=' ') # L_P = last_period_with_production
        print(' '.join(f"{str(i+1):8}" for i in range(self.period)))
        for i in range(self.period):
            print(f"{str(i+1):8}",' '.join(f"{str(value):8}" for value in self.cost_matrix[i]))
        print('-'*period*9)
        print('Z_t:    ', end=' ')
        print(' '.join(f"{str(value):8}" for value in self.z_stars))
        print('j_t:    ', end=' ')
        print(' '.join(f"{str(value):8}" for value in self.j_ts))
        print('='*period*9)

    # print Q_t*
    def get_q_star(self):
        q_stars = {}
        for i in self.j_ts:
            if i not in q_stars:
                q_stars[i] = 0
        for i in range(self.period):
            current_period = self.j_ts[i]  
            if current_period not in q_stars:
                q_stars[current_period] = 0
            q_stars[current_period] += self.period_demands[i]
        print("Q_t*:   ", q_stars)

    # print j_t* for a given period
    def get_j_t_star(self, period):
        j_stars = []
        for i in range(period):
            if self.j_ts[i] not in j_stars:
                j_stars.append(self.j_ts[i])
        print(f"j_t* for {period} period problem: ", j_stars[-1])


if __name__ == '__main__':
    period = 10
    period_demands = [20, 50, 10, 50, 50, 10, 20, 40, 20, 30]
    setup_costs = [100]*period
    unit_costs = [0]*period # fixed unit cost case 
    #unit_costs = [10 , 10, 20, 15, 1, 20, 10, 15, 20, 10] # variable unit cost case
    holding_costs = [1]*period
    ww = WagnerWhitinSolver(period, period_demands, setup_costs, unit_costs, holding_costs)
    ww.solve()
    ww.get_cost_matrix()
    ww.get_q_star()
    ww.get_j_t_star(9)
    