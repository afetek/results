# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Test Run Description: Fan1 ok Fan2 faulted at startup mode
# #######################################################
# : timestamp: 7981604
# Test Setup --> r3 Debug Level: 3: timestamp: 7981605
# Start Test --> : timestamp: 7981834
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7981835
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 7981835
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7981835
# 
# Validation Timestamp: 7981875: timestamp: 7981875
# fan 1 should power on: timestamp: 7981875

def r3_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7982835: timestamp: 7982835
# fan 2 should not power on: timestamp: 7982835

def r3_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7982835
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7982835
# 
# Validation Timestamp: 7982855: timestamp: 7982855
# only fan 1 is available: timestamp: 7982855

def r3_tc3_test():
    """
    Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7982855: timestamp: 7982855
# low fan speed: timestamp: 7982855

def r3_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 7982855
