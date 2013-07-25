# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 73360738
# Get Test Data Variables: timestamp: 73360739
# test data variable --> self.fan1_fault = True: timestamp: 73360754
# test data variable --> self.fan2_fault = False: timestamp: 73360774
# test data variable --> self.TEST_RUN = "r2": timestamp: 73360794
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 73360814
# Test Setup --> r2 Debug Level: 3: timestamp: 73360820
# Start Test --> : timestamp: 73361121
# Powerup Test Script: timestamp: 73361122
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 73361122
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 73361122
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 73361122
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 73361122
# 
# Validation Timestamp: 73361165: timestamp: 73361165
# fan 2 should power on: timestamp: 73361165

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test1_test"


# 
# Validation Timestamp: 73362122: timestamp: 73362122
# fan 1 should not power on: timestamp: 73362122

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 73362122
# 
# Validation Timestamp: 73362135: timestamp: 73362135
# only fan 2 is available: timestamp: 73362135

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test3_test"


# 
# Validation Timestamp: 73362135: timestamp: 73362135
# low fan speed: timestamp: 73362135

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ####################
    TEST_PASSED = True
    ####################

    assert TEST_PASSED, "Failed test4_test"


# Test Done --> r2: timestamp: 73362135
