# Get Script Variables: timestamp: 47958597
# generated script variable --> self.fan1_fault = True: timestamp: 47958612
# generated script variable --> self.fan2_fault = False: timestamp: 47958632
# generated script variable --> self.TEST_RUN = "r2": timestamp: 47958652
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 47958672
# Test Setup --> r2 Debug Level: 3: timestamp: 47958678
# Start Test --> : timestamp: 47959068
# Powerup Test Script: timestamp: 47959069
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47959069
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 47959069
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47959069
# Validation Timestamp: 47959101: timestamp: 47959101
# fan 2 should power on: timestamp: 47959101

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47960069: timestamp: 47960069
# fan 1 should not power on: timestamp: 47960069

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47960069: timestamp: 47960069
# Fan 2 is available EICAS message: timestamp: 47960069

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 47960069
