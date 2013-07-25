# #######################################################: timestamp: 71320954
# Test Name: Powerup Mode Test
# Requirement Under Test: 5,6,7,8
# : timestamp: 71320954
# #######################################################
# : timestamp: 71320954
# Get Test Data Variables: timestamp: 71320955
# test data variable --> self.fan1_fault = False: timestamp: 71320970
# test data variable --> self.fan2_fault = True: timestamp: 71320990
# test data variable --> self.TEST_RUN = "r3": timestamp: 71321010
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 71321030
# Test Setup --> r3 Debug Level: 3: timestamp: 71321036
# Start Test --> : timestamp: 71321423
# Powerup Test Script: timestamp: 71321424
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 71321424
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 71321424
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 71321424
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 71321424
# 
# Validation Timestamp: 71321464: timestamp: 71321464
# fan 1 should power on: timestamp: 71321464

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 71322424: timestamp: 71322424
# fan 2 should not power on: timestamp: 71322424

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 71322424
# 
# Validation Timestamp: 71322443: timestamp: 71322443
# only fan 1 is available: timestamp: 71322443

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 71322443: timestamp: 71322443
# low fan speed: timestamp: 71322443

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r3: timestamp: 71322443
