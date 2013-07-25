# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 77333065
# Get Test Data Variables: timestamp: 77333066
# test data variable --> self.fan1_fault = False: timestamp: 77333081
# test data variable --> self.fan2_fault = False: timestamp: 77333101
# test data variable --> self.TEST_RUN = "r1": timestamp: 77333121
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 77333141
# Test Setup --> r1 Debug Level: 3: timestamp: 77333147
# Start Test --> : timestamp: 77333485
# Powerup Test Script: timestamp: 77333486
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 77333486
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 77333486
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 77333486
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 77333486
# 
# Validation Timestamp: 77333524: timestamp: 77333524
# fan 1 should power on: timestamp: 77333524

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 77334486: timestamp: 77334486
# fan 2 should not power on: timestamp: 77334486

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 77334486
# 
# Validation Timestamp: 77334523: timestamp: 77334523
# both fans are available: timestamp: 77334523

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 77334523: timestamp: 77334523
# low fan speed: timestamp: 77334523

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 77334523
