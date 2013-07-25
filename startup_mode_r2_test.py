# Get Script Variables: timestamp: 47255721
# Convert value for fan1_fault (enum) to a (enum): timestamp: 47255731
# generated script variable --> self.fan1_fault = True: timestamp: 47255736
# Convert value for fan2_fault (enum) to a (enum): timestamp: 47255751
# generated script variable --> self.fan2_fault = False: timestamp: 47255756
# Convert value for TEST_RUN to a (none): timestamp: 47255771
# generated script variable --> self.TEST_RUN = "r2": timestamp: 47255776
# Convert value for description to a (none): timestamp: 47255791
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 47255796
# Test Setup --> r2 Debug Level: 3: timestamp: 47255802
# Start Test --> : timestamp: 47256140
# Powerup Test Script: timestamp: 47256141
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47256141
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 47256141
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47256141
# Validation Timestamp: 47256183: timestamp: 47256183
# fan 2 should power on: timestamp: 47256183

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47257141: timestamp: 47257141
# fan 1 should not power on: timestamp: 47257141

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47257141: timestamp: 47257141
# Fan 2 is available EICAS message: timestamp: 47257141

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 47257141
