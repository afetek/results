# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 3790396
# Get Test Data Variables: timestamp: 3790397
# test data variable --> self.fan1_fault = False: timestamp: 3790412
# test data variable --> self.fan2_fault = True: timestamp: 3790432
# test data variable --> self.TEST_RUN = "r3": timestamp: 3790452
# test data variable --> self.powerup = False: timestamp: 3790472
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 3790492
# Test Setup --> r3 Debug Level: 3: timestamp: 3790498
# Start Test --> : timestamp: 3790631
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 3790632
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 3790632
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 3790632
# 
# Validation Timestamp: 3790676: timestamp: 3790676
# fan 1 should power on: timestamp: 3790676

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 3791632: timestamp: 3791632
# fan 2 should not power on: timestamp: 3791632

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 3791632
# 
# Validation Timestamp: 3791655: timestamp: 3791655
# only fan 1 is available: timestamp: 3791655

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 3791655: timestamp: 3791655
# low fan speed: timestamp: 3791655

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 3791655
