# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81180239
# Get Test Data Variables: timestamp: 81180240
# test data variable --> self.TEST_RUN = "r2": timestamp: 81180243
# test data variable --> self.fan1_fault = True: timestamp: 81180247
# test data variable --> self.powerup = "False": timestamp: 81180251
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 81180255
# test data variable --> self.fan2_fault = False: timestamp: 81180259
# Test Setup --> r2 Debug Level: 3: timestamp: 81180261
# Start Test --> : timestamp: 81180656
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 81180657
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 81180657
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81180657
# 
# Validation Timestamp: 81186988: timestamp: 81186988
# fan 2 should power on: timestamp: 81186988

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81187988: timestamp: 81187988
# fan 1 should not power on: timestamp: 81187988

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 81187988
# 
# Validation Timestamp: 81188002: timestamp: 81188002
# only fan 2 is available: timestamp: 81188002

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81188002: timestamp: 81188002
# low fan speed: timestamp: 81188002

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 81188002
