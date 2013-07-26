# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r4\Test Run Description: Fan1 faulted Fan2 faulted at startup mode
# #######################################################
# : timestamp: 7153300
# Test Setup --> r4 Debug Level: 3: timestamp: 7153301
# Start Test --> : timestamp: 7153530
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 7153531
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 7153531
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7153531
# 
# Validation Timestamp: 7154531: timestamp: 7154531
# fan 1 should not power on: timestamp: 7154531

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7154531: timestamp: 7154531
# fan 2 should not power on: timestamp: 7154531

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7154531: timestamp: 7154531
# no fans available: timestamp: 7154531

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 7154531
