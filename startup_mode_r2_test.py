# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 12031759
# Start Test: : timestamp: 12031889
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 12031890
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 12031890
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 12031890
# 
# Validation Timestamp: 12031922: timestamp: 12031922
# fan 2 should power on: timestamp: 12031922

def r2_tc1_test():
    """
    r2_tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 12032890: timestamp: 12032890
# fan 1 should not power on: timestamp: 12032890

def r2_tc2_test():
    """
    r2_tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 12032890
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 12032890
# 
# Validation Timestamp: 12032921: timestamp: 12032921
# only fan 2 is available: timestamp: 12032921

def r2_tc3_test():
    """
    r2_tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 12032921: timestamp: 12032921
# low fan speed: timestamp: 12032921

def r2_tc4_test():
    """
    r2_tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 12032921
