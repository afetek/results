# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 4149101
# Get Test Data Variables: timestamp: 4149102
# test data variable --> self.fan1_fault = False: timestamp: 4149117
# test data variable --> self.fan2_fault = False: timestamp: 4149137
# test data variable --> self.TEST_RUN = "r1": timestamp: 4149157
# test data variable --> self.powerup = False: timestamp: 4149177
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 4149197
# Test Setup --> r1 Debug Level: 3: timestamp: 4149203
# Start Test --> : timestamp: 4149335
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 4149336
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 4149336
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4149336
# 
# Validation Timestamp: 4149369: timestamp: 4149369
# fan 1 should power on: timestamp: 4149369

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 4150336: timestamp: 4150336
# fan 2 should not power on: timestamp: 4150336

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 4150336
# 
# Validation Timestamp: 4151336: timestamp: 4151336
# both fans are available: timestamp: 4151336

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 4151336: timestamp: 4151336
# low fan speed: timestamp: 4151336

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 4151336
