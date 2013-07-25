# Get Script Variables: timestamp: 47961647
# generated script variable --> self.fan1_fault = False: timestamp: 47961662
# generated script variable --> self.fan2_fault = True: timestamp: 47961682
# generated script variable --> self.TEST_RUN = "r3": timestamp: 47961702
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 47961722
# Test Setup --> r3 Debug Level: 3: timestamp: 47961728
# Start Test --> : timestamp: 47961955
# Powerup Test Script: timestamp: 47961956
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47961956
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 47961956
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47961956
# Validation Timestamp: 47961981: timestamp: 47961981
# fan 1 should power on: timestamp: 47961981

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47962956: timestamp: 47962956
# fan 2 should not power on: timestamp: 47962956

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47962956: timestamp: 47962956
# Both fans are Available EICAS message: timestamp: 47962956

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1 and 1: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 47962956
