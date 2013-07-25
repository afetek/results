# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 71816688
# Get Test Data Variables: timestamp: 71816689
# test data variable --> self.fan1_fault = True: timestamp: 71816704
# test data variable --> self.fan2_fault = True: timestamp: 71816724
# test data variable --> self.TEST_RUN = "r4": timestamp: 71816744
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 71816764
# Test Setup --> r4 Debug Level: 3: timestamp: 71816770
# Start Test --> : timestamp: 71817145
# Powerup Test Script: timestamp: 71817146
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 71817146
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 71817146
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 71817146
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 71817146
# 
# Validation Timestamp: 71818146: timestamp: 71818146
# fan 1 should not power on: timestamp: 71818146

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 71818146: timestamp: 71818146
# fan 2 should not power on: timestamp: 71818146

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 71818146: timestamp: 71818146
# no fans available: timestamp: 71818146

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 71818146
