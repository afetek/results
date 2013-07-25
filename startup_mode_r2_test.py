# Get Script Variables: timestamp: 8803879
# generated script variable --> self.TEST_RUN = "r2": timestamp: 8803894
# generated script variable --> self.fan1_fault = "True": timestamp: 8803914
# generated script variable --> self.fan2_fault = "False": timestamp: 8803934
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 8803954
# Test Setup --> r2 Debug Level: 3: timestamp: 8803960
# Start Test --> : timestamp: 8804186
# Powerup Test Script: timestamp: 8804187
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 8804187
# self.model.fan1FaultRead.Value == 1.0: timestamp: 8804187
# self.model.fan2FaultRead.Value == 1.0: timestamp: 8804187
# self.model.powerECU.Value == 1.0: timestamp: 8804187
# Validation Timestamp: 8805187: timestamp: 8805187
# fan 2 should power on: timestamp: 8805187

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is >= 1 and <= 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 8805187: timestamp: 8805187
# fan 1 should not power on: timestamp: 8805187

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 8805187: timestamp: 8805187
# Fan 2 is available EICAS message: timestamp: 8805187

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is >= 2 and <= 2: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 8805187
