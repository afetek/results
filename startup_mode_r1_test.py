# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1\Test Run Description: Fan1 ok, Fan2 ok at startup mode test
# #######################################################
# : timestamp: 7144184
# Test Setup --> r1 Debug Level: 3: timestamp: 7144185
# Start Test --> : timestamp: 7144314
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7144315
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7144315
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7144315
# 
# Validation Timestamp: 7144351: timestamp: 7144351
# fan 1 should power on: timestamp: 7144351

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7145315: timestamp: 7145315
# fan 2 should not power on: timestamp: 7145315

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7145315
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7145315
# 
# Validation Timestamp: 7145350: timestamp: 7145350
# both fans are available: timestamp: 7145350

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7145350: timestamp: 7145350
# low fan speed: timestamp: 7145350

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 7145350
