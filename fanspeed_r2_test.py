# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 7443454
# Start Test: : timestamp: 7443825
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 7443826
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7443826
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7443826
# 
# Validation Timestamp: 7443864: timestamp: 7443864
# fan 2 should power on: timestamp: 7443864

def r2_tc1_test():
    """
    FANSPEED r2 tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7444826: timestamp: 7444826
# fan 1 should not power on: timestamp: 7444826

def r2_tc2_test():
    """
    FANSPEED r2 tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 7444826
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 7444826
# 
# Validation Timestamp: 7444835: timestamp: 7444835
# only fan 2 is available: timestamp: 7444835

def r2_tc3_test():
    """
    FANSPEED r2 tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7444835: timestamp: 7444835
# low fan speed: timestamp: 7444835

def r2_tc4_test():
    """
    FANSPEED r2 tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 7444835
