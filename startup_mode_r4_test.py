# Get Script Variables: timestamp: 47261798
# Convert value for fan1_fault (enum) to a (enum): timestamp: 47261808
# generated script variable --> self.fan1_fault = True: timestamp: 47261813
# Convert value for fan2_fault (enum) to a (enum): timestamp: 47261828
# generated script variable --> self.fan2_fault = True: timestamp: 47261833
# Convert value for TEST_RUN to a (none): timestamp: 47261848
# generated script variable --> self.TEST_RUN = "r4": timestamp: 47261853
# Convert value for description to a (none): timestamp: 47261868
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 47261873
# Test Setup --> r4 Debug Level: 3: timestamp: 47261879
# Start Test --> : timestamp: 47262118
# Powerup Test Script: timestamp: 47262119
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47262119
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 47262119
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 47262119
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47262119
# Validation Timestamp: 47262162: timestamp: 47262162
# No Fans Available EICAS message: timestamp: 47262162

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47263119: timestamp: 47263119
# fan 2 should not power on: timestamp: 47263119

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47263119: timestamp: 47263119
# fan 1 should not power on: timestamp: 47263119

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 47263119
