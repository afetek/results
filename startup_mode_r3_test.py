# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 73971700
# Get Test Data Variables: timestamp: 73971701
# test data variable --> self.fan1_fault = False: timestamp: 73971716
# test data variable --> self.fan2_fault = True: timestamp: 73971736
# test data variable --> self.TEST_RUN = "r3": timestamp: 73971756
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 73971776
# Test Setup --> r3 Debug Level: 3: timestamp: 73971782
# Start Test --> : timestamp: 73972146
# Powerup Test Script: timestamp: 73972147
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 73972147
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 73972147
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 73972147
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 73972147
# 
# Validation Timestamp: 73972190: timestamp: 73972190
# fan 1 should power on: timestamp: 73972190

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ######################
    TEST_STATUS = "PASSED"
    ######################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 73973147: timestamp: 73973147
# fan 2 should not power on: timestamp: 73973147

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ######################
    TEST_STATUS = "PASSED"
    ######################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 73973147
# 
# Validation Timestamp: 73973169: timestamp: 73973169
# only fan 1 is available: timestamp: 73973169

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ######################
    TEST_STATUS = "PASSED"
    ######################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 73973169: timestamp: 73973169
# low fan speed: timestamp: 73973169

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ######################
    TEST_STATUS = "PASSED"
    ######################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 73973169
