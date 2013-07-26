# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 4156197
# Get Test Data Variables: timestamp: 4156198
# test data variable --> self.fan1_fault = False: timestamp: 4156213
# test data variable --> self.fan2_fault = True: timestamp: 4156233
# test data variable --> self.TEST_RUN = "r3": timestamp: 4156253
# test data variable --> self.powerup = False: timestamp: 4156273
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 4156293
# Test Setup --> r3 Debug Level: 3: timestamp: 4156299
# Start Test --> : timestamp: 4156531
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 4156532
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 4156532
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4156532
# 
# Validation Timestamp: 4156568: timestamp: 4156568
# fan 1 should power on: timestamp: 4156568

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 4157532: timestamp: 4157532
# fan 2 should not power on: timestamp: 4157532

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 4157532
# 
# Validation Timestamp: 4157559: timestamp: 4157559
# only fan 1 is available: timestamp: 4157559

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 4157559: timestamp: 4157559
# low fan speed: timestamp: 4157559

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 4157559
