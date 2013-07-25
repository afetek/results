# Get Script Variables: timestamp: 46425675
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46425685
# generated script variable --> self.fan1_fault = False: timestamp: 46425690
# Convert value for fan2_fault (enum) to a (enum): timestamp: 46425705
# generated script variable --> self.fan2_fault = False: timestamp: 46425710
# Convert value for TEST_RUN to a (none): timestamp: 46425725
# generated script variable --> self.TEST_RUN = "r1": timestamp: 46425730
# Convert value for description to a (none): timestamp: 46425745
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 46425750
# Test Setup --> r1 Debug Level: 3: timestamp: 46425756
# Start Test --> : timestamp: 46425995
# Powerup Test Script: timestamp: 46425996
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46425996
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46425996
# Validation Timestamp: 46426028: timestamp: 46426028
# fan 1 should power on: timestamp: 46426028

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46426996: timestamp: 46426996
# fan 2 should not power on: timestamp: 46426996

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46426996: timestamp: 46426996
# Both fans are Available EICAS message: timestamp: 46426996

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 46426996
