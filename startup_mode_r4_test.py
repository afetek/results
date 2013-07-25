# Get Script Variables: timestamp: 57016128
# generated script variable --> self.fan1_fault = True: timestamp: 57016143
# generated script variable --> self.fan2_fault = True: timestamp: 57016163
# generated script variable --> self.TEST_RUN = "r4": timestamp: 57016183
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 57016203
# Test Setup --> r4 Debug Level: 3: timestamp: 57016209
# Start Test --> : timestamp: 57016436
# Powerup Test Script: timestamp: 57016437
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57016437
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 57016437
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 57016437
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57016437
# 
# Validation Timestamp: 57017437: timestamp: 57017437
# fan 1 should not power on: timestamp: 57017437

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57017437: timestamp: 57017437
# fan 2 should not power on: timestamp: 57017437

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Test Done --> r4: timestamp: 57017437
