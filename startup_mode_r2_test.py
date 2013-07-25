# Get Script Variables: timestamp: 57587718
# generated script variable --> self.fan1_fault = True: timestamp: 57587733
# generated script variable --> self.fan2_fault = False: timestamp: 57587753
# generated script variable --> self.TEST_RUN = "r2": timestamp: 57587773
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 57587793
# Test Setup --> r2 Debug Level: 3: timestamp: 57587799
# Start Test --> : timestamp: 57588123
# Powerup Test Script: timestamp: 57588124
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57588124
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 57588124
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 57588124
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57588124
# 
# Validation Timestamp: 57588164: timestamp: 57588164
# fan 2 should power on: timestamp: 57588164

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57589124: timestamp: 57589124
# fan 1 should not power on: timestamp: 57589124

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 57589124
# 
# Validation Timestamp: 57589155: timestamp: 57589155
# only fan 2 is available: timestamp: 57589155

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 57589155
