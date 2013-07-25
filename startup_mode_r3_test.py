# Get Script Variables: timestamp: 8806919
# generated script variable --> self.TEST_RUN = "r3": timestamp: 8806934
# generated script variable --> self.fan1_fault = "False": timestamp: 8806954
# generated script variable --> self.fan2_fault = "True": timestamp: 8806974
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 8806994
# Test Setup --> r3 Debug Level: 3: timestamp: 8807000
# Start Test --> : timestamp: 8807230
# Powerup Test Script: timestamp: 8807231
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 8807231
# self.model.fan1FaultRead.Value == 1.0: timestamp: 8807231
# self.model.fan2FaultRead.Value == 1.0: timestamp: 8807231
# self.model.powerECU.Value == 1.0: timestamp: 8807231
# Validation Timestamp: 8808231: timestamp: 8808231
# fan 1 should power on: timestamp: 8808231

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 8808231: timestamp: 8808231
# fan 2 should not power on: timestamp: 8808231

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 8808231: timestamp: 8808231
# Both fans are Available EICAS message: timestamp: 8808231

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is >= 1 and <= 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 8808231
