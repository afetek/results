# Get Script Variables: timestamp: 47420064
# Convert value for fan1_fault (enum) to a boolean: timestamp: 47420074
# generated script variable --> self.fan1_fault = False: timestamp: 47420079
# Convert value for fan2_fault (enum) to a boolean: timestamp: 47420094
# generated script variable --> self.fan2_fault = False: timestamp: 47420099
# Convert value for TEST_RUN to a str | float: timestamp: 47420114
# generated script variable --> self.TEST_RUN = "r1": timestamp: 47420119
# Convert value for description to a str | float: timestamp: 47420134
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 47420139
# Test Setup --> r1 Debug Level: 3: timestamp: 47420145
# Start Test --> : timestamp: 47420487
# Powerup Test Script: timestamp: 47420488
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47420488
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47420488
# Validation Timestamp: 47420524: timestamp: 47420524
# fan 1 should power on: timestamp: 47420524

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47421488: timestamp: 47421488
# fan 2 should not power on: timestamp: 47421488

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47421488: timestamp: 47421488
# Both fans are Available EICAS message: timestamp: 47421488

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 47421488
