# Get Script Variables: timestamp: 46806360
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46806370
# generated script variable --> self.fan1_fault = False: timestamp: 46806375
# Convert value for fan2_fault (enum) to a (enum): timestamp: 46806390
# generated script variable --> self.fan2_fault = False: timestamp: 46806395
# Convert value for TEST_RUN to a (none): timestamp: 46806410
# generated script variable --> self.TEST_RUN = "r1": timestamp: 46806415
# Convert value for description to a (none): timestamp: 46806430
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 46806435
# Test Setup --> r1 Debug Level: 3: timestamp: 46806441
# Start Test --> : timestamp: 46806756
# Powerup Test Script: timestamp: 46806757
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46806757
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46806757
# Validation Timestamp: 46806782: timestamp: 46806782
# fan 1 should power on: timestamp: 46806782

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46807757: timestamp: 46807757
# fan 2 should not power on: timestamp: 46807757

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46807757: timestamp: 46807757
# Both fans are Available EICAS message: timestamp: 46807757

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 46807757
