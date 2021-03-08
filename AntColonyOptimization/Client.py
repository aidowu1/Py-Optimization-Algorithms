import matplotlib.pyplot as plt
from pprint import pformat

import Population as p 
import Constants as c
import Acor as a
import Utils as u



class Client(object):
    """
    """
    def __init__(self, 
                 n_pop, 
                 n_vars, 
                 cost_func, 
                 domain_bounds,
                 func_title,
                 problem_use_case="case_1"
                 ):
        """
        Constructor
        """
        self.__problem_use_case = problem_use_case
        self.__n_vars = n_vars
        self.__cost_func = cost_func
        self.__domain_bounds = domain_bounds
        self.__func_title = func_title       
        self.__n_pop = n_pop
        self.__solutions = None

    def runOptimizationRoutine(self):
        """
        Entry Point used to run the ACO algorithm
        """
        start_time = u.Helpers.getStartTime()
        acor = a.AcorContinuousDomain(n_pop=self.__n_pop, 
                                       n_vars=self.__n_vars, 
                                       cost_func=self.__cost_func, 
                                       domain_bounds=self.__domain_bounds)
        print(f"The main loop computation is now running..")
        print(f"{c.HelperConstants.CARRIAGE_RETURN}")
        print(f"{c.HelperConstants.CARRIAGE_RETURN}")
        acor.runMainLoop()
        self.__solutions = acor.best_solutions
        print(f"Now Plotting the optimization performance..")
        print(f"{c.HelperConstants.CARRIAGE_RETURN}")
        print(f"{c.HelperConstants.CARRIAGE_RETURN}")
        print(f"{c.HelperConstants.CARRIAGE_RETURN}")
        self.__plotAlgorithmperformance()
        run_time = u.Helpers.computeTotalRunTime(start_time)
        result = u.Helpers.printAcoResults(acor.final_best_solution)
        print(f"Best soltion:{c.HelperConstants.CARRIAGE_RETURN}{c.HelperConstants.CARRIAGE_RETURN}{result}")
        print(f"ACO compute time is: {run_time}")
        print(f"{c.HelperConstants.CARRIAGE_RETURN}")
        print(f"{c.HelperConstants.CARRIAGE_RETURN}")


    @property
    def __plotData(self):
        """
        getter propert to retrieve the data use to plot the ACO performance
        """
        X = [x.position for x in self.__solutions]
        f_x = [x.cost_function for x in self.__solutions]
        return X, f_x

    def __plotAlgorithmperformance(self):
        """
        Plots the performance/convergence of the ACO algorithm  for a specified optimization problem
        """            
        X, f_x = self.__plotData
        best_f_x = f_x[-1] 
        title_msg = f"ACO performance for the '{self.__func_title}' problem with optimal f_x = {best_f_x:.4e}, bounds = {str(self.__domain_bounds)} and dimensions = {str(self.__n_vars)}"
        iterations = range(len(X))
        #fig, ax = plt.subplots()
        fig = plt.figure(figsize=(10,6))
        ax = fig.add_subplot(111) 
        ax.plot(iterations, f_x, label='ACO performance') 
        ax.set_xlabel('Iterations')  
        ax.set_ylabel('Fitness') 
        ax.set_title(title_msg, fontdict={'fontsize': 8})  
        ax.legend() 
        plt.show() 

def runAcoClient():
    """
    Entry point used to demo the invocation of the ACO algorithm
    """
    problem_case = "case_4"
    n_vars = c.ProblemConstants.COST_FUNC_MAP[problem_case]["n_dims"]
    cost_func = c.ProblemConstants.COST_FUNC_MAP[problem_case]["func"]
    domain_bounds = c.ProblemConstants.COST_FUNC_MAP[problem_case]["bounds"]
    func_title = c.ProblemConstants.COST_FUNC_MAP[problem_case]["func_title"]
    n_pop = c.AcoConstants.N_POP
    c.AcoConstants.MAX_ITERATIONS = 1000
    print(f"{c.HelperConstants.DIVIDER}")
    print(f"{c.HelperConstants.CARRIAGE_RETURN}")
    print(f"Start of the demonstration of the minimization of the Continuous domain function {func_title} using Ant Colony Optimization..")
    print(f"{c.HelperConstants.CARRIAGE_RETURN}")
    client = Client(n_pop=n_pop, 
                 n_vars=n_vars, 
                 cost_func=cost_func, 
                 domain_bounds=domain_bounds,
                 func_title=func_title,
                 problem_use_case=problem_case
                 )
    client.runOptimizationRoutine()
    print(f"{c.HelperConstants.CARRIAGE_RETURN}")
    print(f"End of the Ant Colony optimization demo..")
    print(f"{c.HelperConstants.CARRIAGE_RETURN}")
    print(f"{c.HelperConstants.DIVIDER}")
    print(f"{c.HelperConstants.CARRIAGE_RETURN}")
    print(f"{c.HelperConstants.CARRIAGE_RETURN}")



if __name__ == "__main__":
    runAcoClient()