# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82414708
# Get Test Data Variables: timestamp: 82414709
# test data variable --> self.fan1_fault = True: timestamp: 82414724
# test data variable --> self.fan2_fault = False: timestamp: 82414744
# test data variable --> self.TEST_RUN = "r2": timestamp: 82414764
# test data variable --> self.powerup = False: timestamp: 82414784
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 82414804
# Test Setup --> r2 Debug Level: 3: timestamp: 82414810
# Start Test --> : timestamp: 82415107
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 82415108
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 82415108
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 82415108
# 
# Validation Timestamp: 82415150: timestamp: 82415150
# fan 2 should power on: timestamp: 82415150

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82416108: timestamp: 82416108
# fan 1 should not power on: timestamp: 82416108

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 82416108
# 
# Validation Timestamp: 82416121: timestamp: 82416121
# only fan 2 is available: timestamp: 82416121

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 82416121: timestamp: 82416121
# low fan speed: timestamp: 82416121

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 82416121
