# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 4162285
# Get Test Data Variables: timestamp: 4162286
# test data variable --> self.fan1_fault = False: timestamp: 4162301
# test data variable --> self.fan2_fault = False: timestamp: 4162321
# test data variable --> self.TEST_RUN = "r5": timestamp: 4162341
# test data variable --> self.powerup = True: timestamp: 4162361
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 4162381
# Test Setup --> r5 Debug Level: 3: timestamp: 4162387
# Start Test --> : timestamp: 4162517
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 4162518
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 4162518
# 
# Validation Timestamp: 4183837: timestamp: 4183837
# fan 1 should power on: timestamp: 4183837

def test1_test_test():
    """
    Run r5 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 4183837: timestamp: 4183837
# fan 2 should not power on: timestamp: 4183837

def test2_test_test():
    """
    Run r5 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 4183837
# 
# Validation Timestamp: 4184837: timestamp: 4184837
# both fans are available: timestamp: 4184837

def test3_test_test():
    """
    Run r5 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 4184837: timestamp: 4184837
# low fan speed: timestamp: 4184837

def test4_test_test():
    """
    Run r5 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r5: timestamp: 4184837
