# Get Script Variables: timestamp: 6891122
# generated script variable --> self.TEST_RUN = "r3": timestamp: 6891137
# generated script variable --> self.fan1_fault = "False": timestamp: 6891157
# generated script variable --> self.fan2_fault = "True": timestamp: 6891177
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 6891197
# Test Setup --> r3 Debug Level: 3: timestamp: 6891203
# Start Test --> : timestamp: 6891534
# Powerup Test Script: timestamp: 6891535
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 6891535
# self.model.fan1FaultRead.Value == 1.0: timestamp: 6891535
# self.model.fan2FaultRead.Value == 1.0: timestamp: 6891535
# self.model.powerECU.Value == 1.0: timestamp: 6891535
# Validation Timestamp: 6891588: timestamp: 6891588
# No Fans Available EICAS message: timestamp: 6891588

def test1_test_test():
    """
    rtt_script_00048 run r3 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 6892535: timestamp: 6892535
# fan 2 should not power on: timestamp: 6892535

def test2_test_test():
    """
    rtt_script_00048 run r3 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 6892535: timestamp: 6892535
# fan 1 should not power on: timestamp: 6892535

def test3_test_test():
    """
    rtt_script_00048 run r3 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 6892535
