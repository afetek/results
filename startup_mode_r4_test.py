# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 72675588
# Get Test Data Variables: timestamp: 72675589
# test data variable --> self.fan1_fault = True: timestamp: 72675604
# test data variable --> self.fan2_fault = True: timestamp: 72675624
# test data variable --> self.TEST_RUN = "r4": timestamp: 72675644
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 72675664
# Test Setup --> r4 Debug Level: 3: timestamp: 72675670
# Start Test --> : timestamp: 72675997
# Powerup Test Script: timestamp: 72675998
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 72675998
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 72675998
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 72675998
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 72675998
# 
# Validation Timestamp: 72676998: timestamp: 72676998
# fan 1 should not power on: timestamp: 72676998

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 72676998: timestamp: 72676998
# fan 2 should not power on: timestamp: 72676998

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 72676998: timestamp: 72676998
# no fans available: timestamp: 72676998

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 72676998
