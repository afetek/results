# Get Script Variables: timestamp: 57323113
# generated script variable --> self.fan1_fault = True: timestamp: 57323128
# generated script variable --> self.fan2_fault = True: timestamp: 57323148
# generated script variable --> self.TEST_RUN = "r4": timestamp: 57323168
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 57323188
# Test Setup --> r4 Debug Level: 3: timestamp: 57323194
# Start Test --> : timestamp: 57323523
# Powerup Test Script: timestamp: 57323524
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57323524
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 57323524
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 57323524
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57323524
# 
# Validation Timestamp: 57324524: timestamp: 57324524
# fan 1 should not power on: timestamp: 57324524

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57324524: timestamp: 57324524
# fan 2 should not power on: timestamp: 57324524

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 57325524: timestamp: 57325524
# no fans available: timestamp: 57325524

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 57325524
