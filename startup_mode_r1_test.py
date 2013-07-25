# Get Script Variables: timestamp: 48181047
# generated script variable --> self.fan1_fault = False: timestamp: 48181062
# generated script variable --> self.fan2_fault = False: timestamp: 48181082
# generated script variable --> self.TEST_RUN = "r1": timestamp: 48181102
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 48181122
# Test Setup --> r1 Debug Level: 3: timestamp: 48181128
# Start Test --> : timestamp: 48181392
# Powerup Test Script: timestamp: 48181393
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 48181393
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 48181393
# Validation Timestamp: 48181423: timestamp: 48181423
# fan 1 should power on: timestamp: 48181423

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 48182393: timestamp: 48182393
# fan 2 should not power on: timestamp: 48182393

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 48182393: timestamp: 48182393
# Both fans are Available EICAS message: timestamp: 48182393

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 48182393
