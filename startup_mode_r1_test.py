# #######################################################: timestamp: 71314857
# Test Name: Powerup Mode Test
# Requirement Under Test: 5,6,7,8
# : timestamp: 71314857
# #######################################################
# : timestamp: 71314857
# Get Test Data Variables: timestamp: 71314858
# test data variable --> self.fan1_fault = False: timestamp: 71314873
# test data variable --> self.fan2_fault = False: timestamp: 71314893
# test data variable --> self.TEST_RUN = "r1": timestamp: 71314913
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 71314933
# Test Setup --> r1 Debug Level: 3: timestamp: 71314939
# Start Test --> : timestamp: 71315275
# Powerup Test Script: timestamp: 71315276
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 71315276
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 71315276
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 71315276
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 71315276
# 
# Validation Timestamp: 71315304: timestamp: 71315304
# fan 1 should power on: timestamp: 71315304

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 71316276: timestamp: 71316276
# fan 2 should not power on: timestamp: 71316276

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 71316276
# 
# Validation Timestamp: 71316324: timestamp: 71316324
# both fans are available: timestamp: 71316324

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 71316324: timestamp: 71316324
# low fan speed: timestamp: 71316324

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r1: timestamp: 71316324
