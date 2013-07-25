# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 73363776
# Get Test Data Variables: timestamp: 73363777
# test data variable --> self.fan1_fault = False: timestamp: 73363792
# test data variable --> self.fan2_fault = True: timestamp: 73363812
# test data variable --> self.TEST_RUN = "r3": timestamp: 73363832
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 73363852
# Test Setup --> r3 Debug Level: 3: timestamp: 73363858
# Start Test --> : timestamp: 73364089
# Powerup Test Script: timestamp: 73364090
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 73364090
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 73364090
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 73364090
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 73364090
# 
# Validation Timestamp: 73364125: timestamp: 73364125
# fan 1 should power on: timestamp: 73364125

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test1_test"


# 
# Validation Timestamp: 73365090: timestamp: 73365090
# fan 2 should not power on: timestamp: 73365090

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 73365090
# 
# Validation Timestamp: 73365115: timestamp: 73365115
# only fan 1 is available: timestamp: 73365115

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test3_test"


# 
# Validation Timestamp: 73365115: timestamp: 73365115
# low fan speed: timestamp: 73365115

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test4_test"


# Test Done --> r3: timestamp: 73365115
