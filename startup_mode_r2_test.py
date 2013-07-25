# Get Script Variables: timestamp: 46428760
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46428770
# generated script variable --> self.fan1_fault = True: timestamp: 46428775
# Convert value for fan2_fault (enum) to a (enum): timestamp: 46428790
# generated script variable --> self.fan2_fault = False: timestamp: 46428795
# Convert value for TEST_RUN to a (none): timestamp: 46428810
# generated script variable --> self.TEST_RUN = "r2": timestamp: 46428815
# Convert value for description to a (none): timestamp: 46428830
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 46428835
# Test Setup --> r2 Debug Level: 3: timestamp: 46428841
# Start Test --> : timestamp: 46429165
# Powerup Test Script: timestamp: 46429166
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46429166
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 46429166
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46429166
# Validation Timestamp: 46429207: timestamp: 46429207
# fan 2 should power on: timestamp: 46429207

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46430166: timestamp: 46430166
# fan 1 should not power on: timestamp: 46430166

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46430166: timestamp: 46430166
# Fan 2 is available EICAS message: timestamp: 46430166

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 46430166
