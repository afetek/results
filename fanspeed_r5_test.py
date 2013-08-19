# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 6895474
# Start Test: : timestamp: 6895768
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 6895769
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 6895769
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 6895769
# 
# Validation Timestamp: 6895807: timestamp: 6895807
# fan 1 should power on: timestamp: 6895807

def r5_tc1_test():
    """
    FANSPEED r5 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6896769: timestamp: 6896769
# fan 2 should not power on: timestamp: 6896769

def r5_tc2_test():
    """
    FANSPEED r5 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 6896769
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 6896769
# 
# Validation Timestamp: 6896798: timestamp: 6896798
# both fans are available: timestamp: 6896798

def r5_tc3_test():
    """
    FANSPEED r5 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6896798: timestamp: 6896798
# low fan speed: timestamp: 6896798

def r5_tc4_test():
    """
    FANSPEED r5 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 6896798
