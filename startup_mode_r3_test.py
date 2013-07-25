# Get Script Variables: timestamp: 57145801
# generated script variable --> self.fan1_fault = False: timestamp: 57145816
# generated script variable --> self.fan2_fault = True: timestamp: 57145836
# generated script variable --> self.TEST_RUN = "r3": timestamp: 57145856
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 57145876
# Test Setup --> r3 Debug Level: 3: timestamp: 57145882
# Start Test --> : timestamp: 57146209
# Powerup Test Script: timestamp: 57146210
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57146210
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 57146210
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 57146210
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57146210
# 
# Validation Timestamp: 57146244: timestamp: 57146244
# fan 1 should power on: timestamp: 57146244

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57147210: timestamp: 57147210
# fan 2 should not power on: timestamp: 57147210

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 57147210
# Test Done --> r3: timestamp: 57147210
