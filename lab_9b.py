from numpy import random, mean

params = {'world_size':(30,30),
          'num_agents':100,
          'same_pref' :0.6,
          'max_iter'  :1000,
          'out_path'  :r'C:\Users\shefo\GitHub\week-9\abm_results.csv' }

class Agent():
    def __init__(self, world, color):
        self.world = world
        self.color = color
        self.location = location
        self.same_pref = same_pref
        self.location = None


class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
 

    def report(self, to_file=True):
        """report final results after run ends"""
        reports = self.reports

        print('\nAll results begin at time=0 and go in order to the end.\n')
        print('The average number of neighbors an agent has not like them:', reports['integration'])
        print('The number of happy agents:', reports['log_of_happy'])
        print('The number of moves per turn:', reports['log_of_moved'])
        print('The number of agents who failed to find a new home:', reports['log_of_stay'])

        if to_file:
            out_path = self.params['out_path']
            with open(out_path, 'w') as f:
                headers = 'turn,integration,num_happy,num_moved,num_stayed\n'
                f.write(headers)
                for i in range(len(reports['log_of_happy'])):
                    line = ','.join([str(i),
                                     str(reports['integration'][i]),
                                     str(reports['log_of_happy'][i]),
                                     str(reports['log_of_moved'][i]),
                                     str(reports['log_of_stay'][i]),
                                     '\n'
                                     ])
                    f.write(line)
            print('\nResults written to:', out_path)

world = World(params)
world.run()