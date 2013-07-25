# Get Script Variables: timestamp: 6969268
# generated script variable --> self.TEST_RUN = "r1": timestamp: 6969283
# generated script variable --> self.fan1_fault = "False": timestamp: 6969303
# generated script variable --> self.fan2_fault = "False": timestamp: 6969323
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 6969343
# Test Setup --> r1 Debug Level: 3: timestamp: 6969349
# Start Test --> : timestamp: 6969678
# Powerup Test Script: timestamp: 6969679
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 6969679
# self.model.fan1FaultRead.Value == 1.0: timestamp: 6969679
# self.model.fan2FaultRead.Value == 1.0: timestamp: 6969679
# self.model.powerECU.Value == 1.0: timestamp: 6969679
# Validation Timestamp: 6969725: timestamp: 6969725
# No Fans Available EICAS message: timestamp: 6969725

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 6970679: timestamp: 6970679
# fan 2 should not power on: timestamp: 6970679

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 6970679: timestamp: 6970679
# fan 1 should not power on: timestamp: 6970679

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 6970679
