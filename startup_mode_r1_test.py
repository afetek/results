# Get Script Variables: timestamp: 47955561
# generated script variable --> self.fan1_fault = False: timestamp: 47955576
# generated script variable --> self.fan2_fault = False: timestamp: 47955596
# generated script variable --> self.TEST_RUN = "r1": timestamp: 47955616
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 47955636
# Test Setup --> r1 Debug Level: 3: timestamp: 47955642
# Start Test --> : timestamp: 47955868
# Powerup Test Script: timestamp: 47955869
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47955869
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47955869
# Validation Timestamp: 47955901: timestamp: 47955901
# fan 1 should power on: timestamp: 47955901

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47956869: timestamp: 47956869
# fan 2 should not power on: timestamp: 47956869

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47956869: timestamp: 47956869
# Both fans are Available EICAS message: timestamp: 47956869

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 47956869
