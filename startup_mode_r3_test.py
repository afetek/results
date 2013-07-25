# Get Script Variables: timestamp: 46160402
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46160412
# generated script variable --> self.fan1_fault = False: timestamp: 46160417
# Convert value for fan2_fault to a (none): timestamp: 46160432
# generated script variable --> self.fan2_fault = "True": timestamp: 46160437
# Convert value for TEST_RUN to a (none): timestamp: 46160452
# generated script variable --> self.TEST_RUN = "r3": timestamp: 46160457
# Convert value for description to a (none): timestamp: 46160472
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 46160477
# Test Setup --> r3 Debug Level: 3: timestamp: 46160483
# Start Test --> : timestamp: 46160776
# Powerup Test Script: timestamp: 46160777
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46160777
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 46160777
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46160777
# Validation Timestamp: 46160810: timestamp: 46160810
# fan 1 should power on: timestamp: 46160810

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46161777: timestamp: 46161777
# fan 2 should not power on: timestamp: 46161777

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46161777: timestamp: 46161777
# Both fans are Available EICAS message: timestamp: 46161777

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1 and 1: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 46161777
