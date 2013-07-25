# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 74463726
# Get Test Data Variables: timestamp: 74463727
# test data variable --> self.fan1_fault = False: timestamp: 74463742
# test data variable --> self.fan2_fault = False: timestamp: 74463762
# test data variable --> self.TEST_RUN = "r1": timestamp: 74463782
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 74463802
# Test Setup --> r1 Debug Level: 3: timestamp: 74463808
# Start Test --> : timestamp: 74464148
# Powerup Test Script: timestamp: 74464149
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 74464149
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 74464149
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 74464149
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 74464149
# 
# Validation Timestamp: 74464188: timestamp: 74464188
# fan 1 should power on: timestamp: 74464188

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 74465149: timestamp: 74465149
# fan 2 should not power on: timestamp: 74465149

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 74465149
# 
# Validation Timestamp: 74465188: timestamp: 74465188
# both fans are available: timestamp: 74465188

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 74465188: timestamp: 74465188
# low fan speed: timestamp: 74465188

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 74465188
