# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82162239
# Get Test Data Variables: timestamp: 82162240
# test data variable --> self.fan1_fault = True: timestamp: 82162255
# test data variable --> self.fan2_fault = False: timestamp: 82162275
# test data variable --> self.TEST_RUN = "r2": timestamp: 82162295
# test data variable --> self.powerup = False: timestamp: 82162315
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 82162335
# Test Setup --> r2 Debug Level: 3: timestamp: 82162341
# Start Test --> : timestamp: 82162702
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 82162703
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 82162703
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 82162703
# 
# Validation Timestamp: 82162746: timestamp: 82162746
# fan 2 should power on: timestamp: 82162746

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82163703: timestamp: 82163703
# fan 1 should not power on: timestamp: 82163703

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 82163703
# 
# Validation Timestamp: 82163716: timestamp: 82163716
# only fan 2 is available: timestamp: 82163716

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 82163716: timestamp: 82163716
# low fan speed: timestamp: 82163716

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 82163716
