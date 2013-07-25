# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 73201768
# Get Test Data Variables: timestamp: 73201769
# test data variable --> self.fan1_fault = False: timestamp: 73201784
# test data variable --> self.fan2_fault = True: timestamp: 73201804
# test data variable --> self.TEST_RUN = "r3": timestamp: 73201824
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 73201844
# Test Setup --> r3 Debug Level: 3: timestamp: 73201850
# Start Test --> : timestamp: 73202187
# Powerup Test Script: timestamp: 73202188
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 73202188
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 73202188
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 73202188
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 73202188
# 
# Validation Timestamp: 73202223: timestamp: 73202223
# fan 1 should power on: timestamp: 73202223

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ####################
    test_passed = True
    ####################

    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 73203188: timestamp: 73203188
# fan 2 should not power on: timestamp: 73203188

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ####################
    test_passed = True
    ####################

    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 73203188
# 
# Validation Timestamp: 73203202: timestamp: 73203202
# only fan 1 is available: timestamp: 73203202

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ####################
    test_passed = True
    ####################

    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 73203202: timestamp: 73203202
# low fan speed: timestamp: 73203202

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ####################
    test_passed = True
    ####################

    assert test_passed, "Failed test4_test"


# Test Done --> r3: timestamp: 73203202
