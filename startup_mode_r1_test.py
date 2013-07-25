# Get Script Variables: timestamp: 57584674
# generated script variable --> self.fan1_fault = False: timestamp: 57584689
# generated script variable --> self.fan2_fault = False: timestamp: 57584709
# generated script variable --> self.TEST_RUN = "r1": timestamp: 57584729
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 57584749
# Test Setup --> r1 Debug Level: 3: timestamp: 57584755
# Start Test --> : timestamp: 57584995
# Powerup Test Script: timestamp: 57584996
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 57584996
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 57584996
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 57584996
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 57584996
# 
# Validation Timestamp: 57585024: timestamp: 57585024
# fan 1 should power on: timestamp: 57585024

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 57585996: timestamp: 57585996
# fan 2 should not power on: timestamp: 57585996

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 57585996
# 
# Validation Timestamp: 57586035: timestamp: 57586035
# both fans are available: timestamp: 57586035

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 57586035
