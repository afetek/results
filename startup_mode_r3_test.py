# #######################################################
# Test Name: Powerup Mode Test
# Requirement Under Test: 5,6,7,8
# #######################################################
# : timestamp: 71654118
# Get Test Data Variables: timestamp: 71654119
# test data variable --> self.fan1_fault = False: timestamp: 71654134
# test data variable --> self.fan2_fault = True: timestamp: 71654154
# test data variable --> self.TEST_RUN = "r3": timestamp: 71654174
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 71654194
# Test Setup --> r3 Debug Level: 3: timestamp: 71654200
# Start Test --> : timestamp: 71654519
# Powerup Test Script: timestamp: 71654520
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 71654520
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 71654520
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 71654520
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 71654520
# 
# Validation Timestamp: 71654570: timestamp: 71654570
# fan 1 should power on: timestamp: 71654570

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 71655520: timestamp: 71655520
# fan 2 should not power on: timestamp: 71655520

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 71655520
# 
# Validation Timestamp: 71655549: timestamp: 71655549
# only fan 1 is available: timestamp: 71655549

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 71655549: timestamp: 71655549
# low fan speed: timestamp: 71655549

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r3: timestamp: 71655549
