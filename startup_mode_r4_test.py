# Get Script Variables: timestamp: 47964682
# generated script variable --> self.fan1_fault = True: timestamp: 47964697
# generated script variable --> self.fan2_fault = True: timestamp: 47964717
# generated script variable --> self.TEST_RUN = "r4": timestamp: 47964737
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 47964757
# Test Setup --> r4 Debug Level: 3: timestamp: 47964763
# Start Test --> : timestamp: 47964993
# Powerup Test Script: timestamp: 47964994
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47964994
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 47964994
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 47964994
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47964994
# Validation Timestamp: 47965052: timestamp: 47965052
# No Fans Available EICAS message: timestamp: 47965052

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47965994: timestamp: 47965994
# fan 2 should not power on: timestamp: 47965994

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47965994: timestamp: 47965994
# fan 1 should not power on: timestamp: 47965994

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 47965994
