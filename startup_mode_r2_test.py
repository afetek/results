# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 77337108
# Get Test Data Variables: timestamp: 77337109
# test data variable --> self.fan1_fault = True: timestamp: 77337124
# test data variable --> self.fan2_fault = False: timestamp: 77337144
# test data variable --> self.TEST_RUN = "r2": timestamp: 77337164
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 77337184
# Test Setup --> r2 Debug Level: 3: timestamp: 77337190
# Start Test --> : timestamp: 77337528
# Powerup Test Script: timestamp: 77337529
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 77337529
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 77337529
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 77337529
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 77337529
# 
# Validation Timestamp: 77337564: timestamp: 77337564
# fan 2 should power on: timestamp: 77337564

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 77338529: timestamp: 77338529
# fan 1 should not power on: timestamp: 77338529

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 77338529
# 
# Validation Timestamp: 77338543: timestamp: 77338543
# only fan 2 is available: timestamp: 77338543

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 77338543: timestamp: 77338543
# low fan speed: timestamp: 77338543

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 77338543
