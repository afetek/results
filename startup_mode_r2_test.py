# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 74326955
# Get Test Data Variables: timestamp: 74326956
# test data variable --> self.fan1_fault = True: timestamp: 74326971
# test data variable --> self.fan2_fault = False: timestamp: 74326991
# test data variable --> self.TEST_RUN = "r2": timestamp: 74327011
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 74327031
# Test Setup --> r2 Debug Level: 3: timestamp: 74327037
# Start Test --> : timestamp: 74327345
# Powerup Test Script: timestamp: 74327346
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 74327346
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 74327346
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 74327346
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 74327346
# 
# Validation Timestamp: 74327383: timestamp: 74327383
# fan 2 should power on: timestamp: 74327383

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 74328346: timestamp: 74328346
# fan 1 should not power on: timestamp: 74328346

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 74328346
# 
# Validation Timestamp: 74328374: timestamp: 74328374
# only fan 2 is available: timestamp: 74328374

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 74328374: timestamp: 74328374
# low fan speed: timestamp: 74328374

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 74328374
