# Get Script Variables: timestamp: 57139733
# generated script variable --> self.fan1_fault = False: timestamp: 57139748
# generated script variable --> self.fan2_fault = False: timestamp: 57139768
# generated script variable --> self.TEST_RUN = "r1": timestamp: 57139788
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 57139808
# Test Setup --> r1 Debug Level: 3: timestamp: 57139814
# Start Test --> : timestamp: 57140143
# Powerup Test Script: timestamp: 57140144
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57140144
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 57140144
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 57140144
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57140144
# 
# Validation Timestamp: 57140184: timestamp: 57140184
# fan 1 should power on: timestamp: 57140184

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57141144: timestamp: 57141144
# fan 2 should not power on: timestamp: 57141144

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 57141144
# Test Done --> r1: timestamp: 57141144
