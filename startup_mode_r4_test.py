# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81441002
# Get Test Data Variables: timestamp: 81441003
# test data variable --> self.fan1_fault = True: timestamp: 81441006
# test data variable --> self.fan2_fault = True: timestamp: 81441010
# test data variable --> self.TEST_RUN = "r4": timestamp: 81441014
# test data variable --> self.powerup = False: timestamp: 81441018
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 81441022
# Test Setup --> r4 Debug Level: 3: timestamp: 81441024
# Start Test --> : timestamp: 81441601
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 81441602
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 81441602
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81441602
# 
# Validation Timestamp: 81442602: timestamp: 81442602
# fan 1 should not power on: timestamp: 81442602

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81442602: timestamp: 81442602
# fan 2 should not power on: timestamp: 81442602

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# 
# Validation Timestamp: 81442602: timestamp: 81442602
# no fans available: timestamp: 81442602

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# Test Done --> r4: timestamp: 81442602
