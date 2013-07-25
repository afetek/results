# Get Script Variables: timestamp: 46935620
# Convert value for fan1_fault  to a (none): timestamp: 46935630
# generated script variable --> self.fan1_fault = "True": timestamp: 46935635
# Convert value for TEST_RUN to a (none): timestamp: 46935650
# generated script variable --> self.TEST_RUN = "r4": timestamp: 46935655
# Convert value for fan2_fault (enum) to a (enum): timestamp: 46935670
# generated script variable --> self.fan2_fault = True: timestamp: 46935675
# Convert value for description to a (none): timestamp: 46935690
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 46935695
# Test Setup --> r4 Debug Level: 3: timestamp: 46935701
# Start Test --> : timestamp: 46936059
# Powerup Test Script: timestamp: 46936060
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46936060
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 46936060
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 46936060
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46936060
# Validation Timestamp: 46936136: timestamp: 46936136
# No Fans Available EICAS message: timestamp: 46936136

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46937060: timestamp: 46937060
# fan 2 should not power on: timestamp: 46937060

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46937060: timestamp: 46937060
# fan 1 should not power on: timestamp: 46937060

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 46937060
