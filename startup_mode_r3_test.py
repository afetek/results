# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 105751
# Get Test Data Variables: timestamp: 105752
# test data variable --> self.fan1_fault = False: timestamp: 105767
# test data variable --> self.fan2_fault = True: timestamp: 105787
# test data variable --> self.TEST_RUN = "r3": timestamp: 105807
# test data variable --> self.powerup = False: timestamp: 105827
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 105847
# Test Setup --> r3 Debug Level: 3: timestamp: 105853
# Start Test --> : timestamp: 105981
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 105982
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 105982
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 105982
# 
# Validation Timestamp: 106021: timestamp: 106021
# fan 1 should power on: timestamp: 106021

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 106982: timestamp: 106982
# fan 2 should not power on: timestamp: 106982

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 106982
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 106982
# 
# Validation Timestamp: 107012: timestamp: 107012
# only fan 1 is available: timestamp: 107012

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 107012: timestamp: 107012
# low fan speed: timestamp: 107012

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 107012
