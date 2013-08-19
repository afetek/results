# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1
# Description: Fans OK at startup
# #######################################################
# : timestamp: 4004763
# Start Test: : timestamp: 4004891
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 4004892
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 4004892
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4004892
# 
# Validation Timestamp: 4004928: timestamp: 4004928
# fan 1 should power on: timestamp: 4004928

def r1_tc1_test():
    """
    STARTUP r1 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 4005892: timestamp: 4005892
# fan 2 should not power on: timestamp: 4005892

def r1_tc2_test():
    """
    STARTUP r1 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 4005892
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 4005892
# 
# Validation Timestamp: 4005919: timestamp: 4005919
# both fans are available: timestamp: 4005919

def r1_tc3_test():
    """
    STARTUP r1 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 4005919: timestamp: 4005919
# low fan speed: timestamp: 4005919

def r1_tc4_test():
    """
    STARTUP r1 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 4005919
