# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r1
# Description: Fans OK at startup
# #######################################################
# : timestamp: 7440415
# Start Test: : timestamp: 7440670
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7440671
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7440671
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7440671
# 
# Validation Timestamp: 7440704: timestamp: 7440704
# fan 1 should power on: timestamp: 7440704

def r1_tc1_test():
    """
    FANSPEED r1 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7441671: timestamp: 7441671
# fan 2 should not power on: timestamp: 7441671

def r1_tc2_test():
    """
    FANSPEED r1 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7441671
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7441671
# 
# Validation Timestamp: 7441696: timestamp: 7441696
# both fans are available: timestamp: 7441696

def r1_tc3_test():
    """
    FANSPEED r1 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7441696: timestamp: 7441696
# low fan speed: timestamp: 7441696

def r1_tc4_test():
    """
    FANSPEED r1 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 7441696
