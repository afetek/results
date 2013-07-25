# Get Script Variables: timestamp: 9647488
# conversion: (enum): timestamp: 9647498
# generated script variable --> self.fan1_fault = True: timestamp: 9647503
# conversion: (none): timestamp: 9647518
# generated script variable --> self.fan2_fault = "True": timestamp: 9647523
# conversion: (none): timestamp: 9647538
# generated script variable --> self.TEST_RUN = "r4": timestamp: 9647543
# conversion: (none): timestamp: 9647558
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 9647563
# Test Setup --> r4 Debug Level: 3: timestamp: 9647569
# Start Test --> : timestamp: 9647907
# Powerup Test Script: timestamp: 9647908
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 9647908
# self.model.fan1FaultRead.Value == 1.0: timestamp: 9647908
# self.model.fan2FaultRead.Value == 1.0: timestamp: 9647908
# self.model.powerECU.Value == 1.0: timestamp: 9647908
# Validation Timestamp: 9647966: timestamp: 9647966
# No Fans Available EICAS message: timestamp: 9647966

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 9648908: timestamp: 9648908
# fan 2 should not power on: timestamp: 9648908

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 9648908: timestamp: 9648908
# fan 1 should not power on: timestamp: 9648908

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 9648908
