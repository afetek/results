# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Description: Fan1 faulted Fan2 faulted at startup mode
# #######################################################
# : timestamp: 8213633
# Start Test: : timestamp: 8213764
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 8213765
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 8213765
# Assigned value 0.0 to variable self.model.enableCanTx: timestamp: 8213765
# 
# Validation Timestamp: 8270930: timestamp: 8270930
# fan 1 should power on: timestamp: 8270930

def r5_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8270930: timestamp: 8270930
# fan 2 should not power on: timestamp: 8270930

def r5_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 8270930
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 8270930
# 
# Validation Timestamp: 8271930: timestamp: 8271930
# both fans are available: timestamp: 8271930

def r5_tc3_test():
    """
    Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8271930: timestamp: 8271930
# low fan speed: timestamp: 8271930

def r5_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 8271930
