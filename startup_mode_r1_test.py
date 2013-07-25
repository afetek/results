# Get Script Variables: timestamp: 57007023
# generated script variable --> self.fan1_fault = False: timestamp: 57007038
# generated script variable --> self.fan2_fault = False: timestamp: 57007058
# generated script variable --> self.TEST_RUN = "r1": timestamp: 57007078
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 57007098
# Test Setup --> r1 Debug Level: 3: timestamp: 57007104
# Start Test --> : timestamp: 57007338
# Powerup Test Script: timestamp: 57007339
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57007339
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 57007339
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 57007339
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57007339
# 
# Validation Timestamp: 57007370: timestamp: 57007370
# fan 1 should power on: timestamp: 57007370

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57008339: timestamp: 57008339
# fan 2 should not power on: timestamp: 57008339

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 57008339
# Test Done --> r1: timestamp: 57008339
