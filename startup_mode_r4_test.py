# Get Script Variables: timestamp: 6894171
# generated script variable --> self.TEST_RUN = "r4": timestamp: 6894186
# generated script variable --> self.fan1_fault = "True": timestamp: 6894206
# generated script variable --> self.fan2_fault = "True": timestamp: 6894226
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 6894246
# Test Setup --> r4 Debug Level: 3: timestamp: 6894252
# Start Test --> : timestamp: 6894478
# Powerup Test Script: timestamp: 6894479
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 6894479
# self.model.fan1FaultRead.Value == 1.0: timestamp: 6894479
# self.model.fan2FaultRead.Value == 1.0: timestamp: 6894479
# self.model.powerECU.Value == 1.0: timestamp: 6894479
# Validation Timestamp: 6894528: timestamp: 6894528
# No Fans Available EICAS message: timestamp: 6894528

def test1_test_test():
    """
    rtt_script_00048 run r4 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 6895479: timestamp: 6895479
# fan 2 should not power on: timestamp: 6895479

def test2_test_test():
    """
    rtt_script_00048 run r4 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 6895479: timestamp: 6895479
# fan 1 should not power on: timestamp: 6895479

def test3_test_test():
    """
    rtt_script_00048 run r4 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 6895479
