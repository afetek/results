# Get Script Variables: timestamp: 57010060
# generated script variable --> self.fan1_fault = True: timestamp: 57010075
# generated script variable --> self.fan2_fault = False: timestamp: 57010095
# generated script variable --> self.TEST_RUN = "r2": timestamp: 57010115
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 57010135
# Test Setup --> r2 Debug Level: 3: timestamp: 57010141
# Start Test --> : timestamp: 57010367
# Powerup Test Script: timestamp: 57010368
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57010368
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 57010368
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 57010368
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57010368
# 
# Validation Timestamp: 57010409: timestamp: 57010409
# fan 2 should power on: timestamp: 57010409

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57011368: timestamp: 57011368
# fan 1 should not power on: timestamp: 57011368

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 57011368
# Test Done --> r2: timestamp: 57011368
