# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 3980217
# Get Test Data Variables: timestamp: 3980218
# test data variable --> self.fan1_fault = False: timestamp: 3980233
# test data variable --> self.fan2_fault = True: timestamp: 3980253
# test data variable --> self.TEST_RUN = "r3": timestamp: 3980273
# test data variable --> self.powerup = False: timestamp: 3980293
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 3980313
# Test Setup --> r3 Debug Level: 3: timestamp: 3980319
# Start Test --> : timestamp: 3980451
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 3980452
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 3980452
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 3980452
# 
# Validation Timestamp: 3980487: timestamp: 3980487
# fan 1 should power on: timestamp: 3980487

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 3981452: timestamp: 3981452
# fan 2 should not power on: timestamp: 3981452

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 3981452
# 
# Validation Timestamp: 3981467: timestamp: 3981467
# only fan 1 is available: timestamp: 3981467

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 3981467: timestamp: 3981467
# low fan speed: timestamp: 3981467

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 3981467
