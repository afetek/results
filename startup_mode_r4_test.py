# Get Script Variables: timestamp: 5815450
# generated script variable --> self.TEST_RUN = "r4": timestamp: 5815465
# generated script variable --> self.fan1_fault = "True": timestamp: 5815485
# generated script variable --> self.fan2_fault = "True": timestamp: 5815505
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 5815525
# Test Setup --> r4 Debug Level: 3: timestamp: 5815531
# Start Test --> : timestamp: 5815913
# Powerup Test Script: timestamp: 5815914
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5815914
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5815914
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5815914
# self.model.powerECU.Value == 1.0: timestamp: 5815914

def test1_test_test():
    """
    script1 run r4 test 1: Exception in Validation: Model instance has no attribute 'fan1_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5815976: timestamp: 5815976
# No Fans Available EICAS message: timestamp: 5815976

def test2_test_test():
    """
    script1 run r4 test 2: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5816914: timestamp: 5816914
# fan 2 should not power on: timestamp: 5816914

def test3_test_test():
    """
    script1 run r4 test 3: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 5816914
