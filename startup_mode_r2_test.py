# Get Script Variables: timestamp: 48184083
# generated script variable --> self.fan1_fault = True: timestamp: 48184098
# generated script variable --> self.fan2_fault = False: timestamp: 48184118
# generated script variable --> self.TEST_RUN = "r2": timestamp: 48184138
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 48184158
# Test Setup --> r2 Debug Level: 3: timestamp: 48184164
# Start Test --> : timestamp: 48184450
# Powerup Test Script: timestamp: 48184451
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 48184451
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 48184451
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 48184451
# Validation Timestamp: 48184483: timestamp: 48184483
# fan 2 should power on: timestamp: 48184483

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 48185451: timestamp: 48185451
# fan 1 should not power on: timestamp: 48185451

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 48185451: timestamp: 48185451
# Fan 2 is available EICAS message: timestamp: 48185451

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 48185451
