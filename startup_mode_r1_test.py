# Get Script Variables: timestamp: 44483039
# Conversion for fan1_fault (enum) is (enum): timestamp: 44483049
# generated script variable --> self.fan1_fault = False: timestamp: 44483054
# Conversion for fan2_fault is (none): timestamp: 44483069
# generated script variable --> self.fan2_fault = "False": timestamp: 44483074
# Conversion for TEST_RUN is (none): timestamp: 44483089
# generated script variable --> self.TEST_RUN = "r1": timestamp: 44483094
# Conversion for description is (none): timestamp: 44483109
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 44483114
# Test Setup --> r1 Debug Level: 3: timestamp: 44483120
# Start Test --> : timestamp: 44483356
# Powerup Test Script: timestamp: 44483357
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 44483357
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 44483357
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 44483357
# Validation Timestamp: 44483383: timestamp: 44483383
# fan 1 should power on: timestamp: 44483383

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 44484357: timestamp: 44484357
# fan 2 should not power on: timestamp: 44484357

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 44484357: timestamp: 44484357
# Both fans are Available EICAS message: timestamp: 44484357

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3 and 3: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 44484357
