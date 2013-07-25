# Get Script Variables: timestamp: 45923686
# Convert value for fan1_fault (enum) to a (enum): timestamp: 45923696
# generated script variable --> self.fan1_fault = False: timestamp: 45923701
# Convert value for fan2_fault to a (none): timestamp: 45923716
# generated script variable --> self.fan2_fault = "True": timestamp: 45923721
# Convert value for TEST_RUN to a (none): timestamp: 45923736
# generated script variable --> self.TEST_RUN = "r3": timestamp: 45923741
# Convert value for description to a (none): timestamp: 45923756
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 45923761
# Test Setup --> r3 Debug Level: 3: timestamp: 45923767
# Start Test --> : timestamp: 45924077
# Powerup Test Script: timestamp: 45924078
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 45924078
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 45924078
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 45924078
# Validation Timestamp: 45924109: timestamp: 45924109
# fan 1 should power on: timestamp: 45924109

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 45925078: timestamp: 45925078
# fan 2 should not power on: timestamp: 45925078

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 45925078: timestamp: 45925078
# Both fans are Available EICAS message: timestamp: 45925078

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1 and 1: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 45925078
