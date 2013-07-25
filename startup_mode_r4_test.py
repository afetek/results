# Get Script Variables: timestamp: 9864662
# conversion: (enum): timestamp: 9864672
# generated script variable --> self.fan1_fault = True: timestamp: 9864677
# conversion: (none): timestamp: 9864692
# generated script variable --> self.fan2_fault = "True": timestamp: 9864697
# conversion: (none): timestamp: 9864712
# generated script variable --> self.TEST_RUN = "r4": timestamp: 9864717
# conversion: (none): timestamp: 9864732
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 9864737
# Test Setup --> r4 Debug Level: 3: timestamp: 9864743
# Start Test --> : timestamp: 9864981
# Powerup Test Script: timestamp: 9864982
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 9864982
# self.model.fan1FaultRead.Value == 1.0: timestamp: 9864982
# self.model.fan2FaultRead.Value == 1.0: timestamp: 9864982
# self.model.powerECU.Value == 1.0: timestamp: 9864982
# Validation Timestamp: 9865056: timestamp: 9865056
# No Fans Available EICAS message: timestamp: 9865056

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 9865982: timestamp: 9865982
# fan 2 should not power on: timestamp: 9865982

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 9865982: timestamp: 9865982
# fan 1 should not power on: timestamp: 9865982

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 9865982
