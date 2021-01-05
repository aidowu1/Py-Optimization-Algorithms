
import CostFunctions as cf

class HelperConstants(object):
    """
    General helper constants
    """
    DIVIDER = "-----" * 10
    CARRIAGE_RETURN = "\n"
    N_EPOCHS_FOR_DISPLAY = 50
    RANDOM_SEED = 100

class ProblemConstants(object):
    """
    Problem specific constants
    """
    COST_FUNC_MAP = {
    "case_1": {
        "bounds": [0.5, 1.5],                # Lower/upper domain bounds
        "n_dims": 10,                        # Number of Decision Variables
        "func": cf.dp,                       # Cost function
        "func_title": "Diagonal Plane",                    # Function title
    },
    "case_2": {
        "bounds": [-5.12, 5.12],
        "n_dims": 10,
        "func": cf.sphere,
        "func_title": "Sphere",                   
    },
    "case_3": {
        "bounds": [-5.0, 5.0],
        "n_dims": 10,
        "func": cf.stybtangm,
        "func_title": "Styblinski-Tang",                    
    },    
    "case_4": {
        "bounds": [-5.12, 5.12],
        "n_dims": 10,
        "func": cf.rastrigin,
        "func_title": "Rastrigin",                   
    },
}

class AcoConstants(object):
    """
    ACO Constant specifications
    """    
    MAX_ITERATIONS = 1000                   # Maximum Number of Iterations
    N_POP = 10                              # Population Size (Archive Size)
    N_ANTS = 40                             # Number of ants
    #Q = 0.5
    Q = 0.5                                 # Intensification Factor (Selection Pressure)
    ZETA = 1                                # Deviation-Distance Ratio
