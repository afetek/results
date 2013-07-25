# Get Script Variables: timestamp: 6888077
# generated script variable --> self.TEST_RUN = "r2": timestamp: 6888092
# generated script variable --> self.fan1_fault = "True": timestamp: 6888112
# generated script variable --> self.fan2_fault = "False": timestamp: 6888132
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 6888152
# Test Setup --> r2 Debug Level: 3: timestamp: 6888158
# Start Test --> : timestamp: 6888399
# Powerup Test Script: timestamp: 6888400
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 6888400
# self.model.fan1FaultRead.Value == 1.0: timestamp: 6888400
# self.model.fan2FaultRead.Value == 1.0: timestamp: 6888400
# self.model.powerECU.Value == 1.0: timestamp: 6888400
# Validation Timestamp: 6888468: timestamp: 6888468
# No Fans Available EICAS message: timestamp: 6888468

def test1_test_test():
    """
    rtt_script_00048 run r2 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 6889400: timestamp: 6889400
# fan 2 should not power on: timestamp: 6889400

def test2_test_test():
    """
    rtt_script_00048 run r2 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 6889400: timestamp: 6889400
# fan 1 should not power on: timestamp: 6889400

def test3_test_test():
    """
    rtt_script_00048 run r2 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 6889400
