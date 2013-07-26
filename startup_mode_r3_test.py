# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3\Test Run Description: Fan1 ok Fan2 faulted at startup mode
# #######################################################
# : timestamp: 7150260
# Test Setup --> r3 Debug Level: 3: timestamp: 7150261
# Start Test --> : timestamp: 7150491
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7150492
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 7150492
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7150492
# 
# Validation Timestamp: 7150531: timestamp: 7150531
# fan 1 should power on: timestamp: 7150531

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7151492: timestamp: 7151492
# fan 2 should not power on: timestamp: 7151492

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7151492
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7151492
# 
# Validation Timestamp: 7151510: timestamp: 7151510
# only fan 1 is available: timestamp: 7151510

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7151510: timestamp: 7151510
# low fan speed: timestamp: 7151510

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 7151510
