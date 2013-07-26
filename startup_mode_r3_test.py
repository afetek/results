# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81880513
# Get Test Data Variables: timestamp: 81880514
# test data variable --> self.fan1_fault = False: timestamp: 81880529
# test data variable --> self.fan2_fault = True: timestamp: 81880549
# test data variable --> self.TEST_RUN = "r3": timestamp: 81880569
# test data variable --> self.powerup = False: timestamp: 81880589
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 81880609
# Test Setup --> r3 Debug Level: 3: timestamp: 81880615
# Start Test --> : timestamp: 81880905
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 81880906
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 81880906
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81880906
# 
# Validation Timestamp: 81880949: timestamp: 81880949
# fan 1 should power on: timestamp: 81880949

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81881906: timestamp: 81881906
# fan 2 should not power on: timestamp: 81881906

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 81881906
# 
# Validation Timestamp: 81881928: timestamp: 81881928
# only fan 1 is available: timestamp: 81881928

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81881928: timestamp: 81881928
# low fan speed: timestamp: 81881928

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 81881928
