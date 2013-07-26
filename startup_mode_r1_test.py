# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82411662
# Get Test Data Variables: timestamp: 82411663
# test data variable --> self.fan1_fault = False: timestamp: 82411678
# test data variable --> self.fan2_fault = False: timestamp: 82411698
# test data variable --> self.TEST_RUN = "r1": timestamp: 82411718
# test data variable --> self.powerup = False: timestamp: 82411738
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 82411758
# Test Setup --> r1 Debug Level: 3: timestamp: 82411764
# Start Test --> : timestamp: 82412020
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 82412021
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 82412021
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 82412021
# 
# Validation Timestamp: 82412071: timestamp: 82412071
# fan 1 should power on: timestamp: 82412071

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82413021: timestamp: 82413021
# fan 2 should not power on: timestamp: 82413021

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 82413021
# 
# Validation Timestamp: 82413061: timestamp: 82413061
# both fans are available: timestamp: 82413061

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 82413061: timestamp: 82413061
# low fan speed: timestamp: 82413061

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 82413061
