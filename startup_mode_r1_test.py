# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 4415072
# Get Test Data Variables: timestamp: 4415073
# test data variable --> self.fan1_fault = False: timestamp: 4415088
# test data variable --> self.fan2_fault = False: timestamp: 4415108
# test data variable --> self.TEST_RUN = "r1": timestamp: 4415128
# test data variable --> self.powerup = False: timestamp: 4415148
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 4415168
# Test Setup --> r1 Debug Level: 3: timestamp: 4415174
# Start Test --> : timestamp: 4415305
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 4415306
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 4415306
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4415306
# 
# Validation Timestamp: 4415349: timestamp: 4415349
# fan 1 should power on: timestamp: 4415349

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 4416306: timestamp: 4416306
# fan 2 should not power on: timestamp: 4416306

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 4416306
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 4416306
# 
# Validation Timestamp: 4416348: timestamp: 4416348
# both fans are available: timestamp: 4416348

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 4416348: timestamp: 4416348
# low fan speed: timestamp: 4416348

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 4416348
