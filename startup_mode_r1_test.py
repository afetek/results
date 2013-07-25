# Get Script Variables: timestamp: 9638386
# conversion: (enum): timestamp: 9638396
# generated script variable --> self.fan1_fault = False: timestamp: 9638401
# conversion: (none): timestamp: 9638416
# generated script variable --> self.fan2_fault = "False": timestamp: 9638421
# conversion: (none): timestamp: 9638436
# generated script variable --> self.TEST_RUN = "r1": timestamp: 9638441
# conversion: (none): timestamp: 9638456
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 9638461
# Test Setup --> r1 Debug Level: 3: timestamp: 9638467
# Start Test --> : timestamp: 9638704
# Powerup Test Script: timestamp: 9638705
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 9638705
# self.model.fan2FaultRead.Value == 1.0: timestamp: 9638705
# self.model.powerECU.Value == 1.0: timestamp: 9638705
# Validation Timestamp: 9638747: timestamp: 9638747
# fan 1 should power on: timestamp: 9638747

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 9639705: timestamp: 9639705
# fan 2 should not power on: timestamp: 9639705

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 9639705: timestamp: 9639705
# Both fans are Available EICAS message: timestamp: 9639705

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is >= 3 and <= 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 9639705
