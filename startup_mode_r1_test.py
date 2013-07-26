# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 3973134
# Get Test Data Variables: timestamp: 3973135
# test data variable --> self.fan1_fault = False: timestamp: 3973150
# test data variable --> self.fan2_fault = False: timestamp: 3973170
# test data variable --> self.TEST_RUN = "r1": timestamp: 3973190
# test data variable --> self.powerup = False: timestamp: 3973210
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 3973230
# Test Setup --> r1 Debug Level: 3: timestamp: 3973236
# Start Test --> : timestamp: 3973366
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 3973367
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 3973367
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 3973367
# 
# Validation Timestamp: 3973408: timestamp: 3973408
# fan 1 should power on: timestamp: 3973408

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 3974367: timestamp: 3974367
# fan 2 should not power on: timestamp: 3974367

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 3974367
# 
# Validation Timestamp: 3975367: timestamp: 3975367
# both fans are available: timestamp: 3975367

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 3975367: timestamp: 3975367
# low fan speed: timestamp: 3975367

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 3975367
