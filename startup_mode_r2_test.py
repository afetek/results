# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 102712
# Get Test Data Variables: timestamp: 102713
# test data variable --> self.fan1_fault = True: timestamp: 102728
# test data variable --> self.fan2_fault = False: timestamp: 102748
# test data variable --> self.TEST_RUN = "r2": timestamp: 102768
# test data variable --> self.powerup = False: timestamp: 102788
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 102808
# Test Setup --> r2 Debug Level: 3: timestamp: 102814
# Start Test --> : timestamp: 102942
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 102943
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 102943
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 102943
# 
# Validation Timestamp: 102981: timestamp: 102981
# fan 2 should power on: timestamp: 102981

def test1_test_test():
    """
    Run r2 Test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 103943: timestamp: 103943
# fan 1 should not power on: timestamp: 103943

def test2_test_test():
    """
    Run r2 Test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 103943
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 103943
# 
# Validation Timestamp: 103972: timestamp: 103972
# only fan 2 is available: timestamp: 103972

def test3_test_test():
    """
    Run r2 Test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 103972: timestamp: 103972
# low fan speed: timestamp: 103972

def test4_test_test():
    """
    Run r2 Test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r2: timestamp: 103972
