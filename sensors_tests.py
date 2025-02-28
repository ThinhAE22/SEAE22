import sensors_main
import unittest
import sys # needed for setting the command line parameters for test cases
from unittest.mock import patch # needed for the integration test case

# Unit tests implemented with Python's built-in unittest need to be classes,
# so here we use TestSensors class for the tests.
class TestSensors(unittest.TestCase):
    ###################
    # Unit test cases #
    ###################

    # Test case test_check_limits1 (UT1) that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    # Test case test_check_limits2 (UT2) that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect.
    def test_check_limits2(self):
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)
    
    def test_check_limits3(self):
        limits = [20, 20]
        result = sensors_main.check_limits(limits)
        self.assertFalse(result, False)

    #Check user test
    #2nd priority mean only access to monitoring temperature and being attendance check
    def test_check_operator(self):
        priority = "operator"
        result = sensors_main.check_role(priority)
        self.assertFalse(result, False)
    #1st priority mean the user having 2nd access with addition to sensor number configurate and change time interval for the sensors
    def test_check_administrator(self):
        priority = "administrator"
        result = sensors_main.check_role(priority)
        self.assertTrue(result, True)

    ##########################
    # Integration test cases #
    ##########################
    
    '''@patch('builtins.print')
    def test_check_role_administrator_integration2(self, mock_print):
        pass

        
        sys.argv = [["sensors_main.py"],"administrator"]

        # 2. call main with the command line parameters set up
        sensors_main.cri()

        mock_print.assert_called_with("Hello Administrator")'''

    @patch('builtins.print')
    def test_check_role_operator_integration3(self, mock_print):
        pass

        
        sys.argv = [["sensors_main.py"],"operator"]

        # 2. call main with the command line parameters set up
        sensors_main.main()

        mock_print.assert_called_with("Hello Operator")

    
    '''@patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        pass

        
        # 1. set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"],[22],[18]]

        # 2. call main with the command line parameters set up
        sensors_main.main()

        # 3. check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

        # 4. If you want to see what is in mock_print, you can use the following
        # (requires that there is import sys (as this module has) because this
        # test case sets the command line arguments that are in sys.argv)
        #
        # sys.stdout.write(str(mock_print.call_args) + "\n")
        # sys.stdout.write(str(mock_print.call_args_list) + "\n")'''

if __name__ == '__main__':
    unittest.main()
