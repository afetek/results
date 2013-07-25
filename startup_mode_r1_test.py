# Get Script Variables: timestamp: 8800839
# generated script variable --> self.TEST_RUN = "r1": timestamp: 8800854
# generated script variable --> self.fan1_fault = "False": timestamp: 8800874
# generated script variable --> self.fan2_fault = "False": timestamp: 8800894
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 8800914
# Test Setup --> r1 Debug Level: 3: timestamp: 8800920
# Start Test --> : timestamp: 8801146
# Powerup Test Script: timestamp: 8801147
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 8801147
# self.model.fan1FaultRead.Value == 1.0: timestamp: 8801147
# self.model.fan2FaultRead.Value == 1.0: timestamp: 8801147
# self.model.powerECU.Value == 1.0: timestamp: 8801147
# Validation Timestamp: 8802147: timestamp: 8802147
# fan 1 should power on: timestamp: 8802147

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 8802147: timestamp: 8802147
# fan 2 should not power on: timestamp: 8802147

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 8802147: timestamp: 8802147
# Both fans are Available EICAS message: timestamp: 8802147

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is >= 3 and <= 3: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 8802147
