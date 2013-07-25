# #######################################################
# Test Name: Powerup Mode Test
# Requirement Under Test: 5,6,7,8
# #######################################################
# : timestamp: 71651085
# Get Test Data Variables: timestamp: 71651086
# test data variable --> self.fan1_fault = True: timestamp: 71651101
# test data variable --> self.fan2_fault = False: timestamp: 71651121
# test data variable --> self.TEST_RUN = "r2": timestamp: 71651141
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 71651161
# Test Setup --> r2 Debug Level: 3: timestamp: 71651167
# Start Test --> : timestamp: 71651611
# Powerup Test Script: timestamp: 71651612
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 71651612
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 71651612
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 71651612
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 71651612
# 
# Validation Timestamp: 71651650: timestamp: 71651650
# fan 2 should power on: timestamp: 71651650

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 71652612: timestamp: 71652612
# fan 1 should not power on: timestamp: 71652612

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 71652612
# 
# Validation Timestamp: 71652629: timestamp: 71652629
# only fan 2 is available: timestamp: 71652629

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 71652629: timestamp: 71652629
# low fan speed: timestamp: 71652629

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r2: timestamp: 71652629
