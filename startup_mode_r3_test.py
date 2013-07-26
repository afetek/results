# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82165272
# Get Test Data Variables: timestamp: 82165273
# test data variable --> self.fan1_fault = False: timestamp: 82165288
# test data variable --> self.fan2_fault = True: timestamp: 82165308
# test data variable --> self.TEST_RUN = "r3": timestamp: 82165328
# test data variable --> self.powerup = False: timestamp: 82165348
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 82165368
# Test Setup --> r3 Debug Level: 3: timestamp: 82165374
# Start Test --> : timestamp: 82165592
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 82165593
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 82165593
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 82165593
# 
# Validation Timestamp: 82165625: timestamp: 82165625
# fan 1 should power on: timestamp: 82165625

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82166593: timestamp: 82166593
# fan 2 should not power on: timestamp: 82166593

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 82166593
# 
# Validation Timestamp: 82166616: timestamp: 82166616
# only fan 1 is available: timestamp: 82166616

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 82166616: timestamp: 82166616
# low fan speed: timestamp: 82166616

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 82166616
