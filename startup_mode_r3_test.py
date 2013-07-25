# Get Script Variables: timestamp: 46932574
# Convert value for fan1_fault  to a (none): timestamp: 46932584
# generated script variable --> self.fan1_fault = "False": timestamp: 46932589
# Convert value for TEST_RUN to a (none): timestamp: 46932604
# generated script variable --> self.TEST_RUN = "r3": timestamp: 46932609
# Convert value for fan2_fault (enum) to a (enum): timestamp: 46932624
# generated script variable --> self.fan2_fault = True: timestamp: 46932629
# Convert value for description to a (none): timestamp: 46932644
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 46932649
# Test Setup --> r3 Debug Level: 3: timestamp: 46932655
# Start Test --> : timestamp: 46933030
# Powerup Test Script: timestamp: 46933031
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46933031
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 46933031
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 46933031
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46933031
# Validation Timestamp: 46934031: timestamp: 46934031
# fan 1 should power on: timestamp: 46934031

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46934031: timestamp: 46934031
# fan 2 should not power on: timestamp: 46934031

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46934031: timestamp: 46934031
# Both fans are Available EICAS message: timestamp: 46934031

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1 and 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 46934031
