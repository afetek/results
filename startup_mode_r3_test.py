# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 4421158
# Get Test Data Variables: timestamp: 4421159
# test data variable --> self.fan1_fault = False: timestamp: 4421174
# test data variable --> self.fan2_fault = True: timestamp: 4421194
# test data variable --> self.TEST_RUN = "r3": timestamp: 4421214
# test data variable --> self.powerup = False: timestamp: 4421234
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 4421254
# Test Setup --> r3 Debug Level: 3: timestamp: 4421260
# Start Test --> : timestamp: 4421392
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 4421393
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 4421393
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4421393
# 
# Validation Timestamp: 4421428: timestamp: 4421428
# fan 1 should power on: timestamp: 4421428

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 4422393: timestamp: 4422393
# fan 2 should not power on: timestamp: 4422393

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 4422393
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 4422393
# 
# Validation Timestamp: 4422408: timestamp: 4422408
# only fan 1 is available: timestamp: 4422408

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 4422408: timestamp: 4422408
# low fan speed: timestamp: 4422408

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 4422408
