# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81602141
# Get Test Data Variables: timestamp: 81602142
# test data variable --> self.fan1_fault = False: timestamp: 81602145
# test data variable --> self.fan2_fault = True: timestamp: 81602149
# test data variable --> self.TEST_RUN = "r3": timestamp: 81602153
# test data variable --> self.powerup = False: timestamp: 81602157
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 81602161
# Test Setup --> r3 Debug Level: 3: timestamp: 81602163
# Start Test --> : timestamp: 81602572
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 81602573
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 81602573
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81602573
# 
# Validation Timestamp: 81602610: timestamp: 81602610
# fan 1 should power on: timestamp: 81602610

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81603573: timestamp: 81603573
# fan 2 should not power on: timestamp: 81603573

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 81603573
# 
# Validation Timestamp: 81603600: timestamp: 81603600
# only fan 1 is available: timestamp: 81603600

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81603600: timestamp: 81603600
# low fan speed: timestamp: 81603600

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 81603600
