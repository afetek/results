# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 5785308
# Start Test: : timestamp: 5785496
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 5785497
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 5785497
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 5785497
# 
# Validation Timestamp: 5785523: timestamp: 5785523
# fan 1 should power on: timestamp: 5785523

def r5_tc1_test():
    """
    STARTUP r5 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5786497: timestamp: 5786497
# fan 2 should not power on: timestamp: 5786497

def r5_tc2_test():
    """
    STARTUP r5 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 5786497
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 5786497
# 
# Validation Timestamp: 5786525: timestamp: 5786525
# both fans are available: timestamp: 5786525

def r5_tc3_test():
    """
    STARTUP r5 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5786525: timestamp: 5786525
# low fan speed: timestamp: 5786525

def r5_tc4_test():
    """
    STARTUP r5 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 5786525