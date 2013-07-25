# #######################################################
# Test Name: Powerup Mode Test
# Requirement Under Test: 5,6,7,8
# #######################################################
# : timestamp: 71657161
# Get Test Data Variables: timestamp: 71657162
# test data variable --> self.fan1_fault = True: timestamp: 71657177
# test data variable --> self.fan2_fault = True: timestamp: 71657197
# test data variable --> self.TEST_RUN = "r4": timestamp: 71657217
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 71657237
# Test Setup --> r4 Debug Level: 3: timestamp: 71657243
# Start Test --> : timestamp: 71657479
# Powerup Test Script: timestamp: 71657480
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 71657480
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 71657480
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 71657480
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 71657480
# 
# Validation Timestamp: 71658480: timestamp: 71658480
# fan 1 should not power on: timestamp: 71658480

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 71658480: timestamp: 71658480
# fan 2 should not power on: timestamp: 71658480

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 71658480: timestamp: 71658480
# no fans available: timestamp: 71658480

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 71658480
