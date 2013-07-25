# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 73197711
# Get Test Data Variables: timestamp: 73197712
# test data variable --> self.fan1_fault = True: timestamp: 73197727
# test data variable --> self.fan2_fault = False: timestamp: 73197747
# test data variable --> self.TEST_RUN = "r2": timestamp: 73197767
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 73197787
# Test Setup --> r2 Debug Level: 3: timestamp: 73197793
# Start Test --> : timestamp: 73198168
# Powerup Test Script: timestamp: 73198169
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 73198169
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 73198169
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 73198169
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 73198169
# 
# Validation Timestamp: 73198203: timestamp: 73198203
# fan 2 should power on: timestamp: 73198203

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ####################
    test_passed = True
    ####################

    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 73199169: timestamp: 73199169
# fan 1 should not power on: timestamp: 73199169

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ####################
    test_passed = True
    ####################

    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 73199169
# 
# Validation Timestamp: 73199182: timestamp: 73199182
# only fan 2 is available: timestamp: 73199182

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ####################
    test_passed = True
    ####################

    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 73199182: timestamp: 73199182
# low fan speed: timestamp: 73199182

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ####################
    test_passed = True
    ####################

    assert test_passed, "Failed test4_test"


# Test Done --> r2: timestamp: 73199182
