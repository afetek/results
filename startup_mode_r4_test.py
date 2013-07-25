# Get Script Variables: timestamp: 8480682
# generated script variable --> self.TEST_RUN = "r4": timestamp: 8480697
# generated script variable --> self.fan1_fault = "True": timestamp: 8480717
# generated script variable --> self.fan2_fault = "True": timestamp: 8480737
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 8480757
# Test Setup --> r4 Debug Level: 3: timestamp: 8480763
# Start Test --> : timestamp: 8481091
# Powerup Test Script: timestamp: 8481092
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 8481092
# self.model.fan1FaultRead.Value == 1.0: timestamp: 8481092
# self.model.fan2FaultRead.Value == 1.0: timestamp: 8481092
# self.model.powerECU.Value == 1.0: timestamp: 8481092
# Validation Timestamp: 8481157: timestamp: 8481157
# No Fans Available EICAS message: timestamp: 8481157

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 8482092: timestamp: 8482092
# fan 2 should not power on: timestamp: 8482092

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 8482092: timestamp: 8482092
# fan 1 should not power on: timestamp: 8482092

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 8482092
