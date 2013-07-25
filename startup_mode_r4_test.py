# Get Script Variables: timestamp: 6978402
# generated script variable --> self.TEST_RUN = "r4": timestamp: 6978417
# generated script variable --> self.fan1_fault = "True": timestamp: 6978437
# generated script variable --> self.fan2_fault = "True": timestamp: 6978457
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 6978477
# Test Setup --> r4 Debug Level: 3: timestamp: 6978483
# Start Test --> : timestamp: 6978812
# Powerup Test Script: timestamp: 6978813
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 6978813
# self.model.fan1FaultRead.Value == 1.0: timestamp: 6978813
# self.model.fan2FaultRead.Value == 1.0: timestamp: 6978813
# self.model.powerECU.Value == 1.0: timestamp: 6978813
# Validation Timestamp: 6978864: timestamp: 6978864
# No Fans Available EICAS message: timestamp: 6978864

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 6979813: timestamp: 6979813
# fan 2 should not power on: timestamp: 6979813

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 6979813: timestamp: 6979813
# fan 1 should not power on: timestamp: 6979813

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 6979813
