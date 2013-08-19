# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 3310788
# Start Test: : timestamp: 3310917
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 3310918
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 3310918
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 3310918
# 
# Validation Timestamp: 3310947: timestamp: 3310947
# fan 1 should power on: timestamp: 3310947

def r5_tc1_test():
    """
    STARTUP r5 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 3311918: timestamp: 3311918
# fan 2 should not power on: timestamp: 3311918

def r5_tc2_test():
    """
    STARTUP r5 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 3311918
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 3311918
# 
# Validation Timestamp: 3311948: timestamp: 3311948
# both fans are available: timestamp: 3311948

def r5_tc3_test():
    """
    STARTUP r5 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 3311948: timestamp: 3311948
# low fan speed: timestamp: 3311948

def r5_tc4_test():
    """
    STARTUP r5 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 3311948
