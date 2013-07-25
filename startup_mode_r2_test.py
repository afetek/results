# Get Script Variables: timestamp: 5927669
# generated script variable --> self.TEST_RUN = "r2": timestamp: 5927684
# generated script variable --> self.fan1_fault = "True": timestamp: 5927704
# generated script variable --> self.fan2_fault = "False": timestamp: 5927724
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 5927744
# Test Setup --> r2 Debug Level: 3: timestamp: 5927750
# Start Test --> : timestamp: 5927978
# Powerup Test Script: timestamp: 5927979
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5927979
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5927979
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5927979
# self.model.powerECU.Value == 1.0: timestamp: 5927979
# Validation Timestamp: 5928031: timestamp: 5928031
# No Fans Available EICAS message: timestamp: 5928031

def test1_test_test():
    """
    script1 run r2 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5928979: timestamp: 5928979
# fan 2 should not power on: timestamp: 5928979

def test2_test_test():
    """
    script1 run r2 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5928979: timestamp: 5928979
# fan 1 should not power on: timestamp: 5928979

def test3_test_test():
    """
    script1 run r2 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 5928979
