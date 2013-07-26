# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81203978
# Get Test Data Variables: timestamp: 81203979
# test data variable --> self.TEST_RUN = "r5": timestamp: 81203982
# test data variable --> self.fan1_fault = False: timestamp: 81203986
# test data variable --> self.powerup = "True": timestamp: 81203990
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 81203994
# test data variable --> self.fan2_fault = False: timestamp: 81203998
# Test Setup --> r5 Debug Level: 3: timestamp: 81204000
# Start Test --> : timestamp: 81204395
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 81204396
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 81204396
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81204396
# 
# Validation Timestamp: 81207133: timestamp: 81207133
# fan 1 should power on: timestamp: 81207133

def test1_test_test():
    """
    Run r5 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81208133: timestamp: 81208133
# fan 2 should not power on: timestamp: 81208133

def test2_test_test():
    """
    Run r5 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 81208133
# 
# Validation Timestamp: 81208181: timestamp: 81208181
# both fans are available: timestamp: 81208181

def test3_test_test():
    """
    Run r5 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81208181: timestamp: 81208181
# low fan speed: timestamp: 81208181

def test4_test_test():
    """
    Run r5 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r5: timestamp: 81208181
