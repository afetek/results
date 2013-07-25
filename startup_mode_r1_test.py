# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 73357696
# Get Test Data Variables: timestamp: 73357697
# test data variable --> self.fan1_fault = False: timestamp: 73357712
# test data variable --> self.fan2_fault = False: timestamp: 73357732
# test data variable --> self.TEST_RUN = "r1": timestamp: 73357752
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 73357772
# Test Setup --> r1 Debug Level: 3: timestamp: 73357778
# Start Test --> : timestamp: 73358027
# Powerup Test Script: timestamp: 73358028
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 73358028
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 73358028
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 73358028
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 73358028
# 
# Validation Timestamp: 73358065: timestamp: 73358065
# fan 1 should power on: timestamp: 73358065

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test1_test"


# 
# Validation Timestamp: 73359028: timestamp: 73359028
# fan 2 should not power on: timestamp: 73359028

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 73359028
# 
# Validation Timestamp: 73359076: timestamp: 73359076
# both fans are available: timestamp: 73359076

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test3_test"


# 
# Validation Timestamp: 73359076: timestamp: 73359076
# low fan speed: timestamp: 73359076

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test4_test"


# Test Done --> r1: timestamp: 73359076
