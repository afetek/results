# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 7462060
# Start Test: : timestamp: 7462294
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7462295
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 7462295
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7462295
# 
# Validation Timestamp: 7462323: timestamp: 7462323
# fan 1 should power on: timestamp: 7462323

def r3_tc1_test():
    """
    STARTUP r3 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7463295: timestamp: 7463295
# fan 2 should not power on: timestamp: 7463295

def r3_tc2_test():
    """
    STARTUP r3 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7463295
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7463295
# 
# Validation Timestamp: 7463315: timestamp: 7463315
# only fan 1 is available: timestamp: 7463315

def r3_tc3_test():
    """
    STARTUP r3 tc3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7463315: timestamp: 7463315
# low fan speed: timestamp: 7463315

def r3_tc4_test():
    """
    STARTUP r3 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 7463315
