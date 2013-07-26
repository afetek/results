# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81434908
# Get Test Data Variables: timestamp: 81434909
# test data variable --> self.fan1_fault = True: timestamp: 81434912
# test data variable --> self.fan2_fault = False: timestamp: 81434916
# test data variable --> self.TEST_RUN = "r2": timestamp: 81434920
# test data variable --> self.powerup = False: timestamp: 81434924
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 81434928
# Test Setup --> r2 Debug Level: 3: timestamp: 81434930
# Start Test --> : timestamp: 81435333
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 81435334
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 81435334
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81435334
# 
# Validation Timestamp: 81435372: timestamp: 81435372
# fan 2 should power on: timestamp: 81435372

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81436334: timestamp: 81436334
# fan 1 should not power on: timestamp: 81436334

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 81436334
# 
# Validation Timestamp: 81436351: timestamp: 81436351
# only fan 2 is available: timestamp: 81436351

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81436351: timestamp: 81436351
# low fan speed: timestamp: 81436351

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 81436351
