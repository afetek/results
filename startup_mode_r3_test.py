# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 9289091
# Start Test: : timestamp: 9289321
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 9289322
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 9289322
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 9289322
# 
# Validation Timestamp: 9289359: timestamp: 9289359
# fan 1 should power on: timestamp: 9289359

def r3_tc1_test():
    """
    r3_tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 9290322: timestamp: 9290322
# fan 2 should not power on: timestamp: 9290322

def r3_tc2_test():
    """
    r3_tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 9290322
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 9290322
# 
# Validation Timestamp: 9290339: timestamp: 9290339
# only fan 1 is available: timestamp: 9290339

def r3_tc3_test():
    """
    r3_tc3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 9290339: timestamp: 9290339
# low fan speed: timestamp: 9290339

def r3_tc4_test():
    """
    r3_tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 9290339
