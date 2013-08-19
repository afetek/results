# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r3
# Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 7446503
# Start Test: : timestamp: 7446697
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7446698
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 7446698
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7446698
# 
# Validation Timestamp: 7446724: timestamp: 7446724
# fan 1 should power on: timestamp: 7446724

def r3_tc1_test():
    """
    FANSPEED r3 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7447698: timestamp: 7447698
# fan 2 should not power on: timestamp: 7447698

def r3_tc2_test():
    """
    FANSPEED r3 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7447698
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7447698
# 
# Validation Timestamp: 7447715: timestamp: 7447715
# only fan 1 is available: timestamp: 7447715

def r3_tc3_test():
    """
    FANSPEED r3 tc3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7447715: timestamp: 7447715
# low fan speed: timestamp: 7447715

def r3_tc4_test():
    """
    FANSPEED r3 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 7447715
