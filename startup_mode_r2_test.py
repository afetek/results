# Get Script Variables: timestamp: 47423100
# Convert value for fan1_fault (enum) to a boolean: timestamp: 47423110
# generated script variable --> self.fan1_fault = True: timestamp: 47423115
# Convert value for fan2_fault (enum) to a boolean: timestamp: 47423130
# generated script variable --> self.fan2_fault = False: timestamp: 47423135
# Convert value for TEST_RUN to a str | float: timestamp: 47423150
# generated script variable --> self.TEST_RUN = "r2": timestamp: 47423155
# Convert value for description to a str | float: timestamp: 47423170
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 47423175
# Test Setup --> r2 Debug Level: 3: timestamp: 47423181
# Start Test --> : timestamp: 47423421
# Powerup Test Script: timestamp: 47423422
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47423422
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 47423422
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47423422
# Validation Timestamp: 47423464: timestamp: 47423464
# fan 2 should power on: timestamp: 47423464

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47424422: timestamp: 47424422
# fan 1 should not power on: timestamp: 47424422

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47424422: timestamp: 47424422
# Fan 2 is available EICAS message: timestamp: 47424422

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 47424422
