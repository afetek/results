# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81914750
# Get Test Data Variables: timestamp: 81914751
# test data variable --> self.fan1_fault = False: timestamp: 81914766
# test data variable --> self.fan2_fault = False: timestamp: 81914786
# test data variable --> self.TEST_RUN = "r5": timestamp: 81914806
# test data variable --> self.powerup = True: timestamp: 81914826
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 81914846
# Test Setup --> r5 Debug Level: 3: timestamp: 81914852
# Start Test --> : timestamp: 81915229
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 81915230
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 81915230
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81915230
# 
# Validation Timestamp: 81975316: timestamp: 81975316
# fan 1 should power on: timestamp: 81975316

def test1_test_test():
    """
    Run r5 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81976316: timestamp: 81976316
# fan 2 should not power on: timestamp: 81976316

def test2_test_test():
    """
    Run r5 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 81976316
# 
# Validation Timestamp: 81976364: timestamp: 81976364
# both fans are available: timestamp: 81976364

def test3_test_test():
    """
    Run r5 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81976364: timestamp: 81976364
# low fan speed: timestamp: 81976364

def test4_test_test():
    """
    Run r5 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r5: timestamp: 81976364
