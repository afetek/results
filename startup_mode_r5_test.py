# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Test Run Description: Fan1 faulted Fan2 faulted at startup mode
# #######################################################
# : timestamp: 7324562
# Test Setup --> r5 Debug Level: 3: timestamp: 7324563
# Start Test --> : timestamp: 7324793
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7324794
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7324794
# Assigned value 0.0 to variable self.model.enableCanTx: timestamp: 7324794
# 
# Validation Timestamp: 7336706: timestamp: 7336706
# fan 1 should power on: timestamp: 7336706

def test1_test_test():
    """
    Run r5 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7336706: timestamp: 7336706
# fan 2 should not power on: timestamp: 7336706

def test2_test_test():
    """
    Run r5 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7336706
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7336706
# 
# Validation Timestamp: 7337706: timestamp: 7337706
# both fans are available: timestamp: 7337706

def test3_test_test():
    """
    Run r5 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7337706: timestamp: 7337706
# low fan speed: timestamp: 7337706

def test4_test_test():
    """
    Run r5 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 7337706
