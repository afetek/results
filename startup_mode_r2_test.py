# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 74467779
# Get Test Data Variables: timestamp: 74467780
# test data variable --> self.fan1_fault = True: timestamp: 74467795
# test data variable --> self.fan2_fault = False: timestamp: 74467815
# test data variable --> self.TEST_RUN = "r2": timestamp: 74467835
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 74467855
# Test Setup --> r2 Debug Level: 3: timestamp: 74467861
# Start Test --> : timestamp: 74468103
# Powerup Test Script: timestamp: 74468104
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 74468104
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 74468104
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 74468104
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 74468104
# 
# Validation Timestamp: 74468148: timestamp: 74468148
# fan 2 should power on: timestamp: 74468148

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 74469104: timestamp: 74469104
# fan 1 should not power on: timestamp: 74469104

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 74469104
# 
# Validation Timestamp: 74469128: timestamp: 74469128
# only fan 2 is available: timestamp: 74469128

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 74469128: timestamp: 74469128
# low fan speed: timestamp: 74469128

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 74469128
