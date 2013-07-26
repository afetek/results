# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82737831
# Get Test Data Variables: timestamp: 82737832
# test data variable --> self.fan1_fault = False: timestamp: 82737847
# test data variable --> self.fan2_fault = False: timestamp: 82737867
# test data variable --> self.TEST_RUN = "r5": timestamp: 82737887
# test data variable --> self.powerup = True: timestamp: 82737907
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 82737927
# Test Setup --> r5 Debug Level: 3: timestamp: 82737933
# Start Test --> : timestamp: 82738284
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 82738285
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 82738285
# 
# Validation Timestamp: 82757013: timestamp: 82757013
# fan 1 should power on: timestamp: 82757013

def test1_test_test():
    """
    Run r5 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82757013: timestamp: 82757013
# fan 2 should not power on: timestamp: 82757013

def test2_test_test():
    """
    Run r5 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 82757013
# 
# Validation Timestamp: 82758013: timestamp: 82758013
# both fans are available: timestamp: 82758013

def test3_test_test():
    """
    Run r5 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 82758013: timestamp: 82758013
# low fan speed: timestamp: 82758013

def test4_test_test():
    """
    Run r5 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r5: timestamp: 82758013
