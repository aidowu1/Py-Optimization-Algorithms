import unittest as ut 
import inspect

import Population as p 
import Constants as c


class TestPopulations(ut.TestCase):
    """
    test suit for the Populations class
    """

    def setUp(self) -> None:
        """
        Test setp fixture
        """
        self.__n_vars = c.ProblemConstants.COST_FUNC_MAP["case_1"]["n_dims"]
        self.__cost_func = c.ProblemConstants.COST_FUNC_MAP["case_1"]["func"]
        self.__domain_bounds = c.ProblemConstants.COST_FUNC_MAP["case_1"]["bounds"]
        self.__n_pop = c.AcoConstants.N_POP
        self.__test_msg = "Invalid test!!"

    def test_Population_Constructor_Is_Valid(self):
        """
        Test the validity of the Population constructor
        """
        pops = p.Populations(self.__n_pop, self.__n_vars, self.__cost_func, self.__domain_bounds)
        self.assertIsNotNone(pops, self.__test_msg)

    def test_Population_Initialization_Is_valid(self):
        """
        Test the validity of the population initilaization
        """
        pops = p.Populations(self.__n_pop, self.__n_vars, self.__cost_func, self.__domain_bounds)
        ant_populations = pops.ant_populations
        ant_populations_best = pops.best_population
        expected_n_pops = self.__n_pop
        actual_n_pops = len(ant_populations)
        self.assertIsNotNone(ant_populations, self.__test_msg)
        self.assertEqual(expected_n_pops, actual_n_pops, self.__test_msg)
        self.assertIsNotNone(ant_populations_best, self.__test_msg)


        



if __name__ == "__main__":
    ut.main()
