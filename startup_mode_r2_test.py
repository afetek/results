# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Test Run Description: Fan1 Fault Fan2 ok at startup mode
# #######################################################
# : timestamp: 7315417
# Test Setup --> r2 Debug Level: 3: timestamp: 7315418
# Start Test --> : timestamp: 7315648
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 7315649
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7315649
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7315649
# 
# Validation Timestamp: 7315672: timestamp: 7315672
# fan 2 should power on: timestamp: 7315672

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7316649: timestamp: 7316649
# fan 1 should not power on: timestamp: 7316649

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 7316649
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 7316649
# 
# Validation Timestamp: 7316663: timestamp: 7316663
# only fan 2 is available: timestamp: 7316663

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7316663: timestamp: 7316663
# low fan speed: timestamp: 7316663

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 7316663
