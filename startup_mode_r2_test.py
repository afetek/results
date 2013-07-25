# Get Script Variables: timestamp: 5809340
# generated script variable --> self.TEST_RUN = "r2": timestamp: 5809355
# generated script variable --> self.fan1_fault = "True": timestamp: 5809375
# generated script variable --> self.fan2_fault = "False": timestamp: 5809395
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 5809415
# Test Setup --> r2 Debug Level: 3: timestamp: 5809421
# Start Test --> : timestamp: 5809649
# Powerup Test Script: timestamp: 5809650
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 5809650
# self.model.fan1FaultRead.Value == 1.0: timestamp: 5809650
# self.model.fan2FaultRead.Value == 1.0: timestamp: 5809650
# self.model.powerECU.Value == 1.0: timestamp: 5809650

def test1_test_test():
    """
    script1 run r2 test 1: Exception in Validation: Model instance has no attribute 'fan1_power_enbale'
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 5809716: timestamp: 5809716
# No Fans Available EICAS message: timestamp: 5809716

def test2_test_test():
    """
    script1 run r2 test 2: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 5810650: timestamp: 5810650
# fan 2 should not power on: timestamp: 5810650

def test3_test_test():
    """
    script1 run r2 test 3: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 5810650
