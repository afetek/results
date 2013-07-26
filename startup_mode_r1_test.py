# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1
# Test Run Description: Fans OK at startup
# #######################################################
# : timestamp: 11585249
# Start Test: : timestamp: 11585380
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 11585381
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 11585381
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 11585381
# 
# Validation Timestamp: 11585421: timestamp: 11585421
# fan 1 should power on: timestamp: 11585421

def r1_tc1_test():
    """
    r1_tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 11586381: timestamp: 11586381
# fan 2 should not power on: timestamp: 11586381

def r1_tc2_test():
    """
    r1_tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 11586381
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 11586381
# 
# Validation Timestamp: 11586420: timestamp: 11586420
# both fans are available: timestamp: 11586420

def r1_tc3_test():
    """
    r1_tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 11586420: timestamp: 11586420
# low fan speed: timestamp: 11586420

def r1_tc4_test():
    """
    r1_tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 11586420
