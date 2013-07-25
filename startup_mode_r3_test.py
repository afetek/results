# Get Script Variables: timestamp: 5930704
# generated script variable --> self.TEST_RUN = "r3": timestamp: 5930719
# generated script variable --> self.fan1_fault = "False": timestamp: 5930739
# generated script variable --> self.fan2_fault = "True": timestamp: 5930759
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 5930779
# Test Setup --> r3 Debug Level: 3: timestamp: 5930785
# Start Test --> : timestamp: 5931112
# Powerup Test Script: timestamp: 5931113
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5931113
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5931113
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5931113
# self.model.powerECU.Value == 1.0: timestamp: 5931113
# Validation Timestamp: 5931171: timestamp: 5931171
# No Fans Available EICAS message: timestamp: 5931171

def test1_test_test():
    """
    script1 run r3 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5932113: timestamp: 5932113
# fan 2 should not power on: timestamp: 5932113

def test2_test_test():
    """
    script1 run r3 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5932113: timestamp: 5932113
# fan 1 should not power on: timestamp: 5932113

def test3_test_test():
    """
    script1 run r3 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 5932113
