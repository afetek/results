# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 7452590
# Start Test: : timestamp: 7452873
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7452874
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7452874
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7452874
# 
# Validation Timestamp: 7452904: timestamp: 7452904
# fan 1 should power on: timestamp: 7452904

def r5_tc1_test():
    """
    FANSPEED r5 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7453874: timestamp: 7453874
# fan 2 should not power on: timestamp: 7453874

def r5_tc2_test():
    """
    FANSPEED r5 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7453874
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7453874
# 
# Validation Timestamp: 7453915: timestamp: 7453915
# both fans are available: timestamp: 7453915

def r5_tc3_test():
    """
    FANSPEED r5 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7453915: timestamp: 7453915
# low fan speed: timestamp: 7453915

def r5_tc4_test():
    """
    FANSPEED r5 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 7453915
