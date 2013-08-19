# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 6371792
# Start Test: : timestamp: 6371982
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 6371983
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 6371983
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 6371983
# 
# Validation Timestamp: 6372029: timestamp: 6372029
# fan 1 should power on: timestamp: 6372029

def r3_tc1_test():
    """
    STARTUP r3 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6372983: timestamp: 6372983
# fan 2 should not power on: timestamp: 6372983

def r3_tc2_test():
    """
    STARTUP r3 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 6372983
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 6372983
# 
# Validation Timestamp: 6373000: timestamp: 6373000
# only fan 1 is available: timestamp: 6373000

def r3_tc3_test():
    """
    STARTUP r3 tc3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6373000: timestamp: 6373000
# low fan speed: timestamp: 6373000

def r3_tc4_test():
    """
    STARTUP r3 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 6373000
