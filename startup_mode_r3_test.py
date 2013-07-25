# Get Script Variables: timestamp: 9644460
# conversion: (enum): timestamp: 9644470
# generated script variable --> self.fan1_fault = False: timestamp: 9644475
# conversion: (none): timestamp: 9644490
# generated script variable --> self.fan2_fault = "True": timestamp: 9644495
# conversion: (none): timestamp: 9644510
# generated script variable --> self.TEST_RUN = "r3": timestamp: 9644515
# conversion: (none): timestamp: 9644530
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 9644535
# Test Setup --> r3 Debug Level: 3: timestamp: 9644541
# Start Test --> : timestamp: 9644882
# Powerup Test Script: timestamp: 9644883
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 9644883
# self.model.fan2FaultRead.Value == 1.0: timestamp: 9644883
# self.model.powerECU.Value == 1.0: timestamp: 9644883
# Validation Timestamp: 9644926: timestamp: 9644926
# fan 1 should power on: timestamp: 9644926

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 9645883: timestamp: 9645883
# fan 2 should not power on: timestamp: 9645883

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 9645883: timestamp: 9645883
# Both fans are Available EICAS message: timestamp: 9645883

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is >= 1 and <= 1: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 9645883
