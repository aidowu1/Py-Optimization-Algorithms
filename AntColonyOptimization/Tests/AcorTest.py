import unittest as ut 
import numpy as np

import Population as p 
import Constants as c
import Acor as a


class TestAcorContiniousDomain(ut.TestCase):
    """
    test suit for the Populations class
    """
    def setUp(self) -> None:
        """
        Test setup fixture
        """
        self.__n_vars = c.ProblemConstants.COST_FUNC_MAP["case_1"]["n_dims"]
        self.__cost_func = c.ProblemConstants.COST_FUNC_MAP["case_1"]["func"]
        self.__domain_bounds = c.ProblemConstants.COST_FUNC_MAP["case_1"]["bounds"]
        self.__n_pop = c.AcoConstants.N_POP
        c.AcoConstants.MAX_ITERATIONS = 10
        self.__test_msg = "Invalid test!!"

    def test_AcorContiniousDomain_Constructor_Is_Valid(self):
        """
        Test 'AcorContiniousDomain' constructor is valid
        """
        acor = a.AcorContiniousDomain(n_pop=self.__n_pop, 
                                       n_vars=self.__n_vars, 
                                       cost_func=self.__cost_func, 
                                       domain_bounds=self.__domain_bounds)
        self.assertIsNotNone(acor, self.__test_msg)

    def test_AcorContiniousDomain_Population_Initialization_Is_Valid(self):
        """
        Test 'AcorContiniousDomain' population initialization is valid
        """
        acor = a.AcorContiniousDomain(n_pop=self.__n_pop, 
                                       n_vars=self.__n_vars, 
                                       cost_func=self.__cost_func, 
                                       domain_bounds=self.__domain_bounds)
        acor.initialization()
        self.assertIsNotNone(acor, self.__test_msg)
        self.assertIsNotNone(acor.pops, self.__test_msg)
        self.assertIsNotNone(acor.probs, self.__test_msg)
        self.assertIsNotNone(acor.final_best_solution, self.__test_msg)

    def test_AcorContiniousDomain_CreateMeans_Is_Valid(self):
        """
        Test 'AcorContiniousDomain' mean creation is valid
        """
        acor = a.AcorContiniousDomain(n_pop=self.__n_pop, 
                                       n_vars=self.__n_vars, 
                                       cost_func=self.__cost_func, 
                                       domain_bounds=self.__domain_bounds)
        acor.initialization()
        acor.createMeans()
        self.assertIsNotNone(acor, self.__test_msg)
        self.assertIsNotNone(acor.means, self.__test_msg)

    def test_AcorContiniousDomain_CreateStandardDeviation_Is_Valid(self):
        """
        Test 'AcorContiniousDomain' sigma creation is valid
        """
        acor = a.AcorContiniousDomain(n_pop=self.__n_pop, 
                                       n_vars=self.__n_vars, 
                                       cost_func=self.__cost_func, 
                                       domain_bounds=self.__domain_bounds)
        acor.initialization()
        acor.createMeans()
        acor.createStandardDeviation()
        self.assertIsNotNone(acor, self.__test_msg)
        self.assertIsNotNone(acor.means, self.__test_msg)
        self.assertIsNotNone(acor.sigmas, self.__test_msg)

    def test_AcorContiniousDomain_RouletteWheelSelection_Is_Valid(self):
        """
        Test 'AcorContiniousDomain' Roulette Wheel selection is valid
        """
        acor = a.AcorContiniousDomain(n_pop=self.__n_pop, 
                                       n_vars=self.__n_vars, 
                                       cost_func=self.__cost_func, 
                                       domain_bounds=self.__domain_bounds)
        acor.initialization()
        index = acor.rouletteWheelSelection()
        self.assertIsNotNone(acor, self.__test_msg)
        self.assertTrue(isinstance(index, np.int64), self.__test_msg)

    def test_AcorContiniousDomain_ConstructNewPopulationSolution_Is_Valid(self):
        """
        Test 'AcorContiniousDomain' construction of a new ACO population is valid
        """
        acor = a.AcorContiniousDomain(n_pop=self.__n_pop, 
                                       n_vars=self.__n_vars, 
                                       cost_func=self.__cost_func, 
                                       domain_bounds=self.__domain_bounds)
        acor.initialization()
        acor.constructNewPopulationSolution()
        self.assertIsNotNone(acor, self.__test_msg)
        self.assertIsNotNone(acor.new_pops, self.__test_msg)

    def test_AcorContiniousDomain_RunMainLoop_Is_Valid(self):
        """
        Test 'AcorContiniousDomain' invocation of the ACO population main loop is valid
        """
        acor = a.AcorContiniousDomain(n_pop=self.__n_pop, 
                                       n_vars=self.__n_vars, 
                                       cost_func=self.__cost_func, 
                                       domain_bounds=self.__domain_bounds)
        acor.runMainLoop()
        self.assertIsNotNone(acor, self.__test_msg)
        self.assertIsNotNone(acor.final_best_solution, self.__test_msg)
        self.assertIsNotNone(acor.best_solutions, self.__test_msg)
        

if __name__ == "__main__":
    ut.main()