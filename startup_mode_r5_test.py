# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Test Run Description: Fan1 faulted Fan2 faulted at startup mode
# #######################################################
# : timestamp: 7987691
# Test Setup --> r5 Debug Level: 3: timestamp: 7987692
# Start Test --> : timestamp: 7987921
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7987922
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7987922
# Assigned value 0.0 to variable self.model.enableCanTx: timestamp: 7987922
# 
# Validation Timestamp: 7998853: timestamp: 7998853
# fan 1 should power on: timestamp: 7998853

def r5_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7998853: timestamp: 7998853
# fan 2 should not power on: timestamp: 7998853

def r5_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7998853
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7998853
# 
# Validation Timestamp: 7999853: timestamp: 7999853
# both fans are available: timestamp: 7999853

def r5_tc3_test():
    """
    Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7999853: timestamp: 7999853
# low fan speed: timestamp: 7999853

def r5_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 7999853
