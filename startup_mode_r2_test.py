# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 3977180
# Get Test Data Variables: timestamp: 3977181
# test data variable --> self.fan1_fault = True: timestamp: 3977196
# test data variable --> self.fan2_fault = False: timestamp: 3977216
# test data variable --> self.TEST_RUN = "r2": timestamp: 3977236
# test data variable --> self.powerup = False: timestamp: 3977256
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 3977276
# Test Setup --> r2 Debug Level: 3: timestamp: 3977282
# Start Test --> : timestamp: 3977513
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 3977514
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 3977514
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 3977514
# 
# Validation Timestamp: 3977547: timestamp: 3977547
# fan 2 should power on: timestamp: 3977547

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 3978514: timestamp: 3978514
# fan 1 should not power on: timestamp: 3978514

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 3978514
# 
# Validation Timestamp: 3978527: timestamp: 3978527
# only fan 2 is available: timestamp: 3978527

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 3978527: timestamp: 3978527
# low fan speed: timestamp: 3978527

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 3978527
