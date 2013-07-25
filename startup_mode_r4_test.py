# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 77343235
# Get Test Data Variables: timestamp: 77343236
# test data variable --> self.fan1_fault = True: timestamp: 77343251
# test data variable --> self.fan2_fault = True: timestamp: 77343271
# test data variable --> self.TEST_RUN = "r4": timestamp: 77343291
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 77343311
# Test Setup --> r4 Debug Level: 3: timestamp: 77343317
# Start Test --> : timestamp: 77343776
# Powerup Test Script: timestamp: 77343777
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 77343777
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 77343777
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 77343777
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 77343777
# 
# Validation Timestamp: 77344777: timestamp: 77344777
# fan 1 should not power on: timestamp: 77344777

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 77344777: timestamp: 77344777
# fan 2 should not power on: timestamp: 77344777

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# 
# Validation Timestamp: 77344777: timestamp: 77344777
# no fans available: timestamp: 77344777

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# Test Done --> r4: timestamp: 77344777
