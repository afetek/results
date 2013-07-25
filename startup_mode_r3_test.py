# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 74470820
# Get Test Data Variables: timestamp: 74470821
# test data variable --> self.fan1_fault = False: timestamp: 74470836
# test data variable --> self.fan2_fault = True: timestamp: 74470856
# test data variable --> self.TEST_RUN = "r3": timestamp: 74470876
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 74470896
# Test Setup --> r3 Debug Level: 3: timestamp: 74470902
# Start Test --> : timestamp: 74471206
# Powerup Test Script: timestamp: 74471207
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 74471207
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 74471207
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 74471207
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 74471207
# 
# Validation Timestamp: 74471248: timestamp: 74471248
# fan 1 should power on: timestamp: 74471248

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 74472207: timestamp: 74472207
# fan 2 should not power on: timestamp: 74472207

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 74472207
# 
# Validation Timestamp: 74472227: timestamp: 74472227
# only fan 1 is available: timestamp: 74472227

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 74472227: timestamp: 74472227
# low fan speed: timestamp: 74472227

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 74472227
