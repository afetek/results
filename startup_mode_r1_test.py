# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 74323876
# Get Test Data Variables: timestamp: 74323877
# test data variable --> self.fan1_fault = False: timestamp: 74323892
# test data variable --> self.fan2_fault = False: timestamp: 74323912
# test data variable --> self.TEST_RUN = "r1": timestamp: 74323932
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 74323952
# Test Setup --> r1 Debug Level: 3: timestamp: 74323958
# Start Test --> : timestamp: 74324202
# Powerup Test Script: timestamp: 74324203
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 74324203
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 74324203
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 74324203
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 74324203
# 
# Validation Timestamp: 74324243: timestamp: 74324243
# fan 1 should power on: timestamp: 74324243

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 74325203: timestamp: 74325203
# fan 2 should not power on: timestamp: 74325203

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 74325203
# 
# Validation Timestamp: 74325254: timestamp: 74325254
# both fans are available: timestamp: 74325254

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 74325254: timestamp: 74325254
# low fan speed: timestamp: 74325254

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 74325254
