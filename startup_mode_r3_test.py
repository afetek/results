# Get Script Variables: timestamp: 5812402
# generated script variable --> self.TEST_RUN = "r3": timestamp: 5812417
# generated script variable --> self.fan1_fault = "False": timestamp: 5812437
# generated script variable --> self.fan2_fault = "True": timestamp: 5812457
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 5812477
# Test Setup --> r3 Debug Level: 3: timestamp: 5812483
# Start Test --> : timestamp: 5812814
# Powerup Test Script: timestamp: 5812815
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5812815
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5812815
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5812815
# self.model.powerECU.Value == 1.0: timestamp: 5812815

def test1_test_test():
    """
    script1 run r3 test 1: Exception in Validation: Model instance has no attribute 'fan1_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5812876: timestamp: 5812876
# No Fans Available EICAS message: timestamp: 5812876

def test2_test_test():
    """
    script1 run r3 test 2: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5813815: timestamp: 5813815
# fan 2 should not power on: timestamp: 5813815

def test3_test_test():
    """
    script1 run r3 test 3: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 5813815
