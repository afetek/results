# Get Script Variables: timestamp: 46154322
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46154332
# generated script variable --> self.fan1_fault = False: timestamp: 46154337
# Convert value for fan2_fault to a (none): timestamp: 46154352
# generated script variable --> self.fan2_fault = "False": timestamp: 46154357
# Convert value for TEST_RUN to a (none): timestamp: 46154372
# generated script variable --> self.TEST_RUN = "r1": timestamp: 46154377
# Convert value for description to a (none): timestamp: 46154392
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 46154397
# Test Setup --> r1 Debug Level: 3: timestamp: 46154403
# Start Test --> : timestamp: 46154658
# Powerup Test Script: timestamp: 46154659
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46154659
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 46154659
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46154659
# Validation Timestamp: 46154691: timestamp: 46154691
# fan 1 should power on: timestamp: 46154691

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46155659: timestamp: 46155659
# fan 2 should not power on: timestamp: 46155659

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46155659: timestamp: 46155659
# Both fans are Available EICAS message: timestamp: 46155659

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 46155659
