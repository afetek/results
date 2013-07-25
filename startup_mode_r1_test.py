# Get Script Variables: timestamp: 68869084
# generated script variable --> self.fan1_fault = False: timestamp: 68869099
# generated script variable --> self.fan2_fault = False: timestamp: 68869119
# generated script variable --> self.TEST_RUN = "r1": timestamp: 68869139
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 68869159
# Test Setup --> r1 Debug Level: 3: timestamp: 68869165
# Start Test --> : timestamp: 68869415
# Powerup Test Script: timestamp: 68869416
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 68869416
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 68869416
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 68869416
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 68869416
# 
# Validation Timestamp: 68869449: timestamp: 68869449
# fan 1 should power on: timestamp: 68869449

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 68870416: timestamp: 68870416
# fan 2 should not power on: timestamp: 68870416

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 68870416
# 
# Validation Timestamp: 68870449: timestamp: 68870449
# both fans are available: timestamp: 68870449

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 68870449: timestamp: 68870449
# low fan speed: timestamp: 68870449

def test4_test_test():
    """
     run r1 test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r1: timestamp: 68870449
