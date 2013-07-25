# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 77340142
# Get Test Data Variables: timestamp: 77340143
# test data variable --> self.fan1_fault = False: timestamp: 77340158
# test data variable --> self.fan2_fault = True: timestamp: 77340178
# test data variable --> self.TEST_RUN = "r3": timestamp: 77340198
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 77340218
# Test Setup --> r3 Debug Level: 3: timestamp: 77340224
# Start Test --> : timestamp: 77340602
# Powerup Test Script: timestamp: 77340603
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 77340603
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 77340603
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 77340603
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 77340603
# 
# Validation Timestamp: 77340644: timestamp: 77340644
# fan 1 should power on: timestamp: 77340644

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 77341603: timestamp: 77341603
# fan 2 should not power on: timestamp: 77341603

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 77341603
# 
# Validation Timestamp: 77341623: timestamp: 77341623
# only fan 1 is available: timestamp: 77341623

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 77341623: timestamp: 77341623
# low fan speed: timestamp: 77341623

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 77341623
