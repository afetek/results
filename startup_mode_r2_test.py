# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 3787352
# Get Test Data Variables: timestamp: 3787353
# test data variable --> self.fan1_fault = True: timestamp: 3787368
# test data variable --> self.fan2_fault = False: timestamp: 3787388
# test data variable --> self.TEST_RUN = "r2": timestamp: 3787408
# test data variable --> self.powerup = False: timestamp: 3787428
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 3787448
# Test Setup --> r2 Debug Level: 3: timestamp: 3787454
# Start Test --> : timestamp: 3787586
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 3787587
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 3787587
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 3787587
# 
# Validation Timestamp: 3787636: timestamp: 3787636
# fan 2 should power on: timestamp: 3787636

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 3788587: timestamp: 3788587
# fan 1 should not power on: timestamp: 3788587

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 3788587
# 
# Validation Timestamp: 3788615: timestamp: 3788615
# only fan 2 is available: timestamp: 3788615

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 3788615: timestamp: 3788615
# low fan speed: timestamp: 3788615

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 3788615
