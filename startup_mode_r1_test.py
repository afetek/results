# #######################################################
# Test Name: Powerup Mode Test
# Requirement Under Test: 5,6,7,8
# #######################################################
# : timestamp: 71648046
# Get Test Data Variables: timestamp: 71648047
# test data variable --> self.fan1_fault = False: timestamp: 71648062
# test data variable --> self.fan2_fault = False: timestamp: 71648082
# test data variable --> self.TEST_RUN = "r1": timestamp: 71648102
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 71648122
# Test Setup --> r1 Debug Level: 3: timestamp: 71648128
# Start Test --> : timestamp: 71648457
# Powerup Test Script: timestamp: 71648458
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 71648458
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 71648458
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 71648458
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 71648458
# 
# Validation Timestamp: 71648490: timestamp: 71648490
# fan 1 should power on: timestamp: 71648490

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 71649458: timestamp: 71649458
# fan 2 should not power on: timestamp: 71649458

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 71649458
# 
# Validation Timestamp: 71649509: timestamp: 71649509
# both fans are available: timestamp: 71649509

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 71649509: timestamp: 71649509
# low fan speed: timestamp: 71649509

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r1: timestamp: 71649509
