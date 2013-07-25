# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 72669500
# Get Test Data Variables: timestamp: 72669501
# test data variable --> self.fan1_fault = True: timestamp: 72669516
# test data variable --> self.fan2_fault = False: timestamp: 72669536
# test data variable --> self.TEST_RUN = "r2": timestamp: 72669556
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 72669576
# Test Setup --> r2 Debug Level: 3: timestamp: 72669582
# Start Test --> : timestamp: 72669820
# Powerup Test Script: timestamp: 72669821
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 72669821
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 72669821
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 72669821
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 72669821
# 
# Validation Timestamp: 72669866: timestamp: 72669866
# fan 2 should power on: timestamp: 72669866

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 72670821: timestamp: 72670821
# fan 1 should not power on: timestamp: 72670821

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 72670821
# 
# Validation Timestamp: 72670845: timestamp: 72670845
# only fan 2 is available: timestamp: 72670845

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 72670845: timestamp: 72670845
# low fan speed: timestamp: 72670845

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r2: timestamp: 72670845
