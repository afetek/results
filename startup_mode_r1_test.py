# Get Script Variables: timestamp: 43836768
# Conversion for fan1_fault (enum) is (enum): timestamp: 43836778
# generated script variable --> self.fan1_fault = False: timestamp: 43836783
# Conversion for fan2_fault is (none): timestamp: 43836798
# generated script variable --> self.fan2_fault = "False": timestamp: 43836803
# Conversion for TEST_RUN is (none): timestamp: 43836818
# generated script variable --> self.TEST_RUN = "r1": timestamp: 43836823
# Conversion for description is (none): timestamp: 43836838
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 43836843
# Test Setup --> r1 Debug Level: 3: timestamp: 43836849
# Start Test --> : timestamp: 43837147
# Powerup Test Script: timestamp: 43837148
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 43837148
# Assignment: self.model.fan2FaultRead.Value = 1.0: timestamp: 43837148
# Assignment: self.model.powerECU.Value = 1.0: timestamp: 43837148
# Validation Timestamp: 43837191: timestamp: 43837191
# fan 1 should power on: timestamp: 43837191

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 43838148: timestamp: 43838148
# fan 2 should not power on: timestamp: 43838148

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 43838148: timestamp: 43838148
# Both fans are Available EICAS message: timestamp: 43838148

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is >= 3 and <= 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 43838148
