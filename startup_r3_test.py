# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 19557497
# Start Test: : timestamp: 19557689
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 19557690
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 19557690
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 19557690
# 
# Validation Timestamp: 19557728: timestamp: 19557728
# fan 1 should power on: timestamp: 19557728

def r3_tc1_test():
    """
    STARTUP r3 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 19558690: timestamp: 19558690
# fan 2 should not power on: timestamp: 19558690

def r3_tc2_test():
    """
    STARTUP r3 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 19558690
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 19558690
# 
# Validation Timestamp: 19558709: timestamp: 19558709
# only fan 1 is available: timestamp: 19558709

def r3_tc3_test():
    """
    STARTUP r3 tc3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 19558709: timestamp: 19558709
# low fan speed: timestamp: 19558709

def r3_tc4_test():
    """
    STARTUP r3 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 19558709
