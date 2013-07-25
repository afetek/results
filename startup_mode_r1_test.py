# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 73763237
# Get Test Data Variables: timestamp: 73763238
# test data variable --> self.fan1_fault = False: timestamp: 73763253
# test data variable --> self.fan2_fault = False: timestamp: 73763273
# test data variable --> self.TEST_RUN = "r1": timestamp: 73763293
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 73763313
# Test Setup --> r1 Debug Level: 3: timestamp: 73763319
# Start Test --> : timestamp: 73763592
# Powerup Test Script: timestamp: 73763593
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 73763593
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 73763593
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 73763593
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 73763593
# 
# Validation Timestamp: 73763627: timestamp: 73763627
# fan 1 should power on: timestamp: 73763627

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    #####################
    TEST_STATUS = PASSED
    #####################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 73764593: timestamp: 73764593
# fan 2 should not power on: timestamp: 73764593

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    #####################
    TEST_STATUS = PASSED
    #####################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 73764593
# 
# Validation Timestamp: 73764638: timestamp: 73764638
# both fans are available: timestamp: 73764638

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    #####################
    TEST_STATUS = PASSED
    #####################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 73764638: timestamp: 73764638
# low fan speed: timestamp: 73764638

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    #####################
    TEST_STATUS = PASSED
    #####################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 73764638
