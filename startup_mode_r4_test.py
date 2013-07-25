# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 73457280
# Get Test Data Variables: timestamp: 73457281
# test data variable --> self.fan1_fault = True: timestamp: 73457296
# test data variable --> self.fan2_fault = True: timestamp: 73457316
# test data variable --> self.TEST_RUN = "r4": timestamp: 73457336
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 73457356
# Test Setup --> r4 Debug Level: 3: timestamp: 73457362
# Start Test --> : timestamp: 73457607
# Powerup Test Script: timestamp: 73457608
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 73457608
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 73457608
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 73457608
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 73457608
# 
# Validation Timestamp: 73458608: timestamp: 73458608
# fan 1 should not power on: timestamp: 73458608

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test1_test"


# 
# Validation Timestamp: 73458608: timestamp: 73458608
# fan 2 should not power on: timestamp: 73458608

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test2_test"


# 
# Validation Timestamp: 73458608: timestamp: 73458608
# no fans available: timestamp: 73458608

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test3_test"


# Test Done --> r4: timestamp: 73458608
