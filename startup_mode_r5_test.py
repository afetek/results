# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 8651209
# Start Test: : timestamp: 8651439
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 8651440
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 8651440
# Assigned value 0.0 to variable self.model.enableCanTx: timestamp: 8651440
# 
# Validation Timestamp: 8663194: timestamp: 8663194
# fan 1 should power on: timestamp: 8663194

def r5_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8663194: timestamp: 8663194
# fan 2 should not power on: timestamp: 8663194

def r5_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 8663194
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 8663194
# 
# Validation Timestamp: 8664194: timestamp: 8664194
# both fans are available: timestamp: 8664194

def r5_tc3_test():
    """
    Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8664194: timestamp: 8664194
# low fan speed: timestamp: 8664194

def r5_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 8664194
