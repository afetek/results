# Get Script Variables: timestamp: 8471515
# generated script variable --> self.TEST_RUN = "r1": timestamp: 8471530
# generated script variable --> self.fan1_fault = "False": timestamp: 8471550
# generated script variable --> self.fan2_fault = "False": timestamp: 8471570
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 8471590
# Test Setup --> r1 Debug Level: 3: timestamp: 8471596
# Start Test --> : timestamp: 8471811
# Powerup Test Script: timestamp: 8471812
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 8471812
# self.model.fan1FaultRead.Value == 1.0: timestamp: 8471812
# self.model.fan2FaultRead.Value == 1.0: timestamp: 8471812
# self.model.powerECU.Value == 1.0: timestamp: 8471812
# Validation Timestamp: 8472812: timestamp: 8472812
# fan 1 should power on: timestamp: 8472812

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 8472812: timestamp: 8472812
# fan 2 should not power on: timestamp: 8472812

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 8472812: timestamp: 8472812
# Both fans are Available EICAS message: timestamp: 8472812

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is >= 3 and <= 3: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 8472812
