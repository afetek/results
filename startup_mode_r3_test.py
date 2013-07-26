# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Test Run Description: Fan1 ok Fan2 faulted at startup mode
# #######################################################
# : timestamp: 7318460
# Test Setup --> r3 Debug Level: 3: timestamp: 7318461
# Start Test --> : timestamp: 7318692
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7318693
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 7318693
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7318693
# 
# Validation Timestamp: 7318732: timestamp: 7318732
# fan 1 should power on: timestamp: 7318732

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7319693: timestamp: 7319693
# fan 2 should not power on: timestamp: 7319693

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7319693
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7319693
# 
# Validation Timestamp: 7319723: timestamp: 7319723
# only fan 1 is available: timestamp: 7319723

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7319723: timestamp: 7319723
# low fan speed: timestamp: 7319723

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 7319723
