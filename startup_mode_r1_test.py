# Get Script Variables: timestamp: 5806305
# generated script variable --> self.TEST_RUN = "r1": timestamp: 5806320
# generated script variable --> self.fan1_fault = "False": timestamp: 5806340
# generated script variable --> self.fan2_fault = "False": timestamp: 5806360
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 5806380
# Test Setup --> r1 Debug Level: 3: timestamp: 5806386
# Start Test --> : timestamp: 5806715
# Powerup Test Script: timestamp: 5806716
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5806716
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5806716
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5806716
# self.model.powerECU.Value == 1.0: timestamp: 5806716

def test1_test_test():
    """
    script1 run r1 test 1: Exception in Validation: Model instance has no attribute 'fan1_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5806776: timestamp: 5806776
# No Fans Available EICAS message: timestamp: 5806776

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5807716: timestamp: 5807716
# fan 2 should not power on: timestamp: 5807716

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 5807716
