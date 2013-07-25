# Get Script Variables: timestamp: 57142767
# generated script variable --> self.fan1_fault = True: timestamp: 57142782
# generated script variable --> self.fan2_fault = False: timestamp: 57142802
# generated script variable --> self.TEST_RUN = "r2": timestamp: 57142822
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 57142842
# Test Setup --> r2 Debug Level: 3: timestamp: 57142848
# Start Test --> : timestamp: 57143076
# Powerup Test Script: timestamp: 57143077
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57143077
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 57143077
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 57143077
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57143077
# 
# Validation Timestamp: 57143104: timestamp: 57143104
# fan 2 should power on: timestamp: 57143104

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57144077: timestamp: 57144077
# fan 1 should not power on: timestamp: 57144077

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 57144077
# Test Done --> r2: timestamp: 57144077
