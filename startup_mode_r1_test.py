# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82644018
# Get Test Data Variables: timestamp: 82644019
# test data variable --> self.fan1_fault = False: timestamp: 82644034
# test data variable --> self.fan2_fault = False: timestamp: 82644054
# test data variable --> self.TEST_RUN = "r1": timestamp: 82644074
# test data variable --> self.powerup = False: timestamp: 82644094
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 82644114
# Test Setup --> r1 Debug Level: 3: timestamp: 82644120
# Start Test --> : timestamp: 82644341
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 82644342
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 82644342
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 82644342
# 
# Validation Timestamp: 82644389: timestamp: 82644389
# fan 1 should power on: timestamp: 82644389

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82645342: timestamp: 82645342
# fan 2 should not power on: timestamp: 82645342

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 82645342
# 
# Validation Timestamp: 82645389: timestamp: 82645389
# both fans are available: timestamp: 82645389

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 82645389: timestamp: 82645389
# low fan speed: timestamp: 82645389

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 82645389
