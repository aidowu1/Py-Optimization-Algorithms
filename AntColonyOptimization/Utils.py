from time import time, sleep
import datetime
from pprint import pformat
from typing import List

import Constants as c

class Helpers(object):
    """
    A collection of helper functions
    """

    @staticmethod
    def formatTD(td):
        """ Format time output for report"""
        days = td.days
        hours = td.seconds // 3600
        minutes = (td.seconds % 3600) // 60
        seconds = td.seconds % 60
        result = f"{minutes} mins {seconds} secs"
        #return '%s days %s h %s m %s s' % (days, hours, minutes, seconds)
        return result

    @staticmethod
    def getStartTime():
        """
        Gets the current time
        """
        return time()

    @staticmethod
    def computeTotalRunTime(start_time):
            """
            Computes the total run time for the ACO main loop
            """
            total_time_s = time() - start_time
            total_time = datetime.timedelta(seconds=total_time_s)
            total_time = Helpers.formatTD(total_time)
            return total_time

    @staticmethod
    def printAcoResults(aco_best_results: object):
        """
        Prints the ACO results
        """
        best_results_msg = ""
        best_results_msg += f"Optimal points:{c.HelperConstants.CARRIAGE_RETURN}{pformat(aco_best_results.position)}{c.HelperConstants.CARRIAGE_RETURN}{c.HelperConstants.CARRIAGE_RETURN}"
        best_results_msg += f"Optimal value:{c.HelperConstants.CARRIAGE_RETURN}{pformat(aco_best_results.cost_function)}{c.HelperConstants.CARRIAGE_RETURN}"
        best_results_msg += f"{c.HelperConstants.CARRIAGE_RETURN}"
        return best_results_msg
