# Get Script Variables: timestamp: 47252686
# Convert value for fan1_fault (enum) to a (enum): timestamp: 47252696
# generated script variable --> self.fan1_fault = False: timestamp: 47252701
# Convert value for fan2_fault (enum) to a (enum): timestamp: 47252716
# generated script variable --> self.fan2_fault = False: timestamp: 47252721
# Convert value for TEST_RUN to a (none): timestamp: 47252736
# generated script variable --> self.TEST_RUN = "r1": timestamp: 47252741
# Convert value for description to a (none): timestamp: 47252756
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 47252761
# Test Setup --> r1 Debug Level: 3: timestamp: 47252767
# Start Test --> : timestamp: 47253008
# Powerup Test Script: timestamp: 47253009
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47253009
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47253009
# Validation Timestamp: 47253043: timestamp: 47253043
# fan 1 should power on: timestamp: 47253043

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47254009: timestamp: 47254009
# fan 2 should not power on: timestamp: 47254009

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47254009: timestamp: 47254009
# Both fans are Available EICAS message: timestamp: 47254009

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 47254009
