# Get Script Variables: timestamp: 46926409
# Convert value for fan1_fault  to a (none): timestamp: 46926419
# generated script variable --> self.fan1_fault = "False": timestamp: 46926424
# Convert value for TEST_RUN to a (none): timestamp: 46926439
# generated script variable --> self.TEST_RUN = "r1": timestamp: 46926444
# Convert value for fan2_fault (enum) to a (enum): timestamp: 46926459
# generated script variable --> self.fan2_fault = False: timestamp: 46926464
# Convert value for description to a (none): timestamp: 46926479
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 46926484
# Test Setup --> r1 Debug Level: 3: timestamp: 46926490
# Start Test --> : timestamp: 46926733
# Powerup Test Script: timestamp: 46926734
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46926734
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 46926734
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46926734
# Validation Timestamp: 46926766: timestamp: 46926766
# fan 2 should not power on: timestamp: 46926766

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 1.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46927734: timestamp: 46927734
# fan 1 should power on: timestamp: 46927734

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46927734: timestamp: 46927734
# Both fans are Available EICAS message: timestamp: 46927734

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 46927734
