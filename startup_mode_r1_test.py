# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 99674
# Get Test Data Variables: timestamp: 99675
# test data variable --> self.fan1_fault = False: timestamp: 99690
# test data variable --> self.fan2_fault = False: timestamp: 99710
# test data variable --> self.TEST_RUN = "r1": timestamp: 99730
# test data variable --> self.powerup = False: timestamp: 99750
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 99770
# Test Setup --> r1 Debug Level: 3: timestamp: 99776
# Start Test --> : timestamp: 100005
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 100006
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 100006
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 100006
# 
# Validation Timestamp: 100041: timestamp: 100041
# fan 1 should power on: timestamp: 100041

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 101006: timestamp: 101006
# fan 2 should not power on: timestamp: 101006

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 101006
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 101006
# 
# Validation Timestamp: 101052: timestamp: 101052
# both fans are available: timestamp: 101052

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 101052: timestamp: 101052
# low fan speed: timestamp: 101052

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 101052
