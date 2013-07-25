# Get Script Variables: timestamp: 57319065
# generated script variable --> self.fan1_fault = False: timestamp: 57319080
# generated script variable --> self.fan2_fault = True: timestamp: 57319100
# generated script variable --> self.TEST_RUN = "r3": timestamp: 57319120
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 57319140
# Test Setup --> r3 Debug Level: 3: timestamp: 57319146
# Start Test --> : timestamp: 57319484
# Powerup Test Script: timestamp: 57319485
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57319485
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 57319485
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 57319485
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57319485
# 
# Validation Timestamp: 57319527: timestamp: 57319527
# fan 1 should power on: timestamp: 57319527

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57320485: timestamp: 57320485
# fan 2 should not power on: timestamp: 57320485

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 57320485
# 
# Validation Timestamp: 57321485: timestamp: 57321485
# only fan 1 is available: timestamp: 57321485

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 1.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 57321485
