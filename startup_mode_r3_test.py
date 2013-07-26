# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Test Run Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 11591334
# Start Test: : timestamp: 11591465
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 11591466
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 11591466
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 11591466
# 
# Validation Timestamp: 11591501: timestamp: 11591501
# fan 1 should power on: timestamp: 11591501

def r3_tc1_test():
    """
    r3_tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 11592466: timestamp: 11592466
# fan 2 should not power on: timestamp: 11592466

def r3_tc2_test():
    """
    r3_tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 11592466
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 11592466
# 
# Validation Timestamp: 11592480: timestamp: 11592480
# only fan 1 is available: timestamp: 11592480

def r3_tc3_test():
    """
    r3_tc3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 11592480: timestamp: 11592480
# low fan speed: timestamp: 11592480

def r3_tc4_test():
    """
    r3_tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 11592480
