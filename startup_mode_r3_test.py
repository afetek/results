# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82730745
# Get Test Data Variables: timestamp: 82730746
# test data variable --> self.fan1_fault = False: timestamp: 82730761
# test data variable --> self.fan2_fault = True: timestamp: 82730781
# test data variable --> self.TEST_RUN = "r3": timestamp: 82730801
# test data variable --> self.powerup = False: timestamp: 82730821
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 82730841
# Test Setup --> r3 Debug Level: 3: timestamp: 82730847
# Start Test --> : timestamp: 82731348
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 82731349
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 82731349
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 82731349
# 
# Validation Timestamp: 82731389: timestamp: 82731389
# fan 1 should power on: timestamp: 82731389

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82732349: timestamp: 82732349
# fan 2 should not power on: timestamp: 82732349

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 82732349
# 
# Validation Timestamp: 82732369: timestamp: 82732369
# only fan 1 is available: timestamp: 82732369

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 82732369: timestamp: 82732369
# low fan speed: timestamp: 82732369

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 82732369
