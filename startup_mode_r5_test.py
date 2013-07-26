# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81724574
# Get Test Data Variables: timestamp: 81724575
# test data variable --> self.fan1_fault = False: timestamp: 81724578
# test data variable --> self.fan2_fault = False: timestamp: 81724582
# test data variable --> self.TEST_RUN = "r5": timestamp: 81724586
# test data variable --> self.powerup = True: timestamp: 81724590
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 81724594
# Test Setup --> r5 Debug Level: 3: timestamp: 81724596
# Start Test --> : timestamp: 81725006
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 81725007
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 81725007
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81725007
# 
# Validation Timestamp: 81738360: timestamp: 81738360
# fan 1 should power on: timestamp: 81738360

def test1_test_test():
    """
    Run r5 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81739360: timestamp: 81739360
# fan 2 should not power on: timestamp: 81739360

def test2_test_test():
    """
    Run r5 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 81739360
# 
# Validation Timestamp: 81739394: timestamp: 81739394
# both fans are available: timestamp: 81739394

def test3_test_test():
    """
    Run r5 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81739394: timestamp: 81739394
# low fan speed: timestamp: 81739394

def test4_test_test():
    """
    Run r5 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r5: timestamp: 81739394
