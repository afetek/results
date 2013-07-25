# Get Script Variables: timestamp: 46157356
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46157366
# generated script variable --> self.fan1_fault = True: timestamp: 46157371
# Convert value for fan2_fault to a (none): timestamp: 46157386
# generated script variable --> self.fan2_fault = "False": timestamp: 46157391
# Convert value for TEST_RUN to a (none): timestamp: 46157406
# generated script variable --> self.TEST_RUN = "r2": timestamp: 46157411
# Convert value for description to a (none): timestamp: 46157426
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 46157431
# Test Setup --> r2 Debug Level: 3: timestamp: 46157437
# Start Test --> : timestamp: 46157749
# Powerup Test Script: timestamp: 46157750
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46157750
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 46157750
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 46157750
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46157750
# Validation Timestamp: 46158750: timestamp: 46158750
# fan 2 should power on: timestamp: 46158750

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46158750: timestamp: 46158750
# fan 1 should not power on: timestamp: 46158750

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46158750: timestamp: 46158750
# Fan 2 is available EICAS message: timestamp: 46158750

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 46158750
