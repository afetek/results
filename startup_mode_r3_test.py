# Get Script Variables: timestamp: 57013094
# generated script variable --> self.fan1_fault = False: timestamp: 57013109
# generated script variable --> self.fan2_fault = True: timestamp: 57013129
# generated script variable --> self.TEST_RUN = "r3": timestamp: 57013149
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 57013169
# Test Setup --> r3 Debug Level: 3: timestamp: 57013175
# Start Test --> : timestamp: 57013404
# Powerup Test Script: timestamp: 57013405
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57013405
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 57013405
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 57013405
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57013405
# 
# Validation Timestamp: 57013449: timestamp: 57013449
# fan 1 should power on: timestamp: 57013449

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57014405: timestamp: 57014405
# fan 2 should not power on: timestamp: 57014405

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 57014405
# Test Done --> r3: timestamp: 57014405
