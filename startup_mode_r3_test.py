# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Description: Fan1 ok Fan2 faulted at startup mode
# #######################################################
# : timestamp: 8207536
# Start Test: : timestamp: 8207667
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 8207668
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 8207668
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 8207668
# 
# Validation Timestamp: 8207714: timestamp: 8207714
# fan 1 should power on: timestamp: 8207714

def r3_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8208668: timestamp: 8208668
# fan 2 should not power on: timestamp: 8208668

def r3_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 8208668
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 8208668
# 
# Validation Timestamp: 8208685: timestamp: 8208685
# only fan 1 is available: timestamp: 8208685

def r3_tc3_test():
    """
    Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8208685: timestamp: 8208685
# low fan speed: timestamp: 8208685

def r3_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 8208685
