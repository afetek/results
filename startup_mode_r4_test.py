# Get Script Variables: timestamp: 69171142
# test data variable --> self.fan1_fault = True: timestamp: 69171157
# test data variable --> self.fan2_fault = True: timestamp: 69171177
# test data variable --> self.TEST_RUN = "r4": timestamp: 69171197
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 69171217
# Test Setup --> r4 Debug Level: 3: timestamp: 69171223
# Start Test --> : timestamp: 69171421
# Powerup Test Script: timestamp: 69171422
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 69171422
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 69171422
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 69171422
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 69171422
# 
# Validation Timestamp: 69172422: timestamp: 69172422
# fan 1 should not power on: timestamp: 69172422

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 69172422: timestamp: 69172422
# fan 2 should not power on: timestamp: 69172422

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 69172422: timestamp: 69172422
# no fans available: timestamp: 69172422

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 69172422
