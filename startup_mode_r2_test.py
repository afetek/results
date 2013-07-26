# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 4418116
# Get Test Data Variables: timestamp: 4418117
# test data variable --> self.fan1_fault = True: timestamp: 4418132
# test data variable --> self.fan2_fault = False: timestamp: 4418152
# test data variable --> self.TEST_RUN = "r2": timestamp: 4418172
# test data variable --> self.powerup = False: timestamp: 4418192
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 4418212
# Test Setup --> r2 Debug Level: 3: timestamp: 4418218
# Start Test --> : timestamp: 4418347
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 4418348
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 4418348
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4418348
# 
# Validation Timestamp: 4418388: timestamp: 4418388
# fan 2 should power on: timestamp: 4418388

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 4419348: timestamp: 4419348
# fan 1 should not power on: timestamp: 4419348

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 4419348
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 4419348
# 
# Validation Timestamp: 4419368: timestamp: 4419368
# only fan 2 is available: timestamp: 4419368

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 4419368: timestamp: 4419368
# low fan speed: timestamp: 4419368

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 4419368
