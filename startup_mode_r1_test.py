# Get Script Variables: timestamp: 9855529
# conversion: (enum): timestamp: 9855539
# generated script variable --> self.fan1_fault = False: timestamp: 9855544
# conversion: (none): timestamp: 9855559
# generated script variable --> self.fan2_fault = "False": timestamp: 9855564
# conversion: (none): timestamp: 9855579
# generated script variable --> self.TEST_RUN = "r1": timestamp: 9855584
# conversion: (none): timestamp: 9855599
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 9855604
# Test Setup --> r1 Debug Level: 3: timestamp: 9855610
# Start Test --> : timestamp: 9855948
# Powerup Test Script: timestamp: 9855949
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 9855949
# self.model.fan2FaultRead.Value == 1.0: timestamp: 9855949
# self.model.powerECU.Value == 1.0: timestamp: 9855949
# Validation Timestamp: 9855986: timestamp: 9855986
# fan 1 should power on: timestamp: 9855986

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 9856949: timestamp: 9856949
# fan 2 should not power on: timestamp: 9856949

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 9856949: timestamp: 9856949
# Both fans are Available EICAS message: timestamp: 9856949

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is >= 3 and <= 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 9856949
