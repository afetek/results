# Get Script Variables: timestamp: 5924624
# generated script variable --> self.TEST_RUN = "r1": timestamp: 5924639
# generated script variable --> self.fan1_fault = "False": timestamp: 5924659
# generated script variable --> self.fan2_fault = "False": timestamp: 5924679
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 5924699
# Test Setup --> r1 Debug Level: 3: timestamp: 5924705
# Start Test --> : timestamp: 5924933
# Powerup Test Script: timestamp: 5924934
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5924934
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5924934
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5924934
# self.model.powerECU.Value == 1.0: timestamp: 5924934
# Validation Timestamp: 5924991: timestamp: 5924991
# No Fans Available EICAS message: timestamp: 5924991

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5925934: timestamp: 5925934
# fan 2 should not power on: timestamp: 5925934

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5925934: timestamp: 5925934
# fan 1 should not power on: timestamp: 5925934

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 5925934
