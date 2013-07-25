# Get Script Variables: timestamp: 45917599
# Convert value for fan1_fault (enum) to a (enum): timestamp: 45917609
# generated script variable --> self.fan1_fault = False: timestamp: 45917614
# Convert value for fan2_fault to a (none): timestamp: 45917629
# generated script variable --> self.fan2_fault = "False": timestamp: 45917634
# Convert value for TEST_RUN to a (none): timestamp: 45917649
# generated script variable --> self.TEST_RUN = "r1": timestamp: 45917654
# Convert value for description to a (none): timestamp: 45917669
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 45917674
# Test Setup --> r1 Debug Level: 3: timestamp: 45917680
# Start Test --> : timestamp: 45918019
# Powerup Test Script: timestamp: 45918020
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 45918020
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 45918020
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 45918020
# Validation Timestamp: 45918070: timestamp: 45918070
# fan 1 should power on: timestamp: 45918070

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 45919020: timestamp: 45919020
# fan 2 should not power on: timestamp: 45919020

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 45919020: timestamp: 45919020
# Both fans are Available EICAS message: timestamp: 45919020

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 45919020
