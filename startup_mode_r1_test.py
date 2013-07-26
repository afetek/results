# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1
# Test Run Description: Fan1 ok, Fan2 ok at startup mode test
# #######################################################
# : timestamp: 7975522
# Test Setup --> r1 Debug Level: 3: timestamp: 7975523
# Start Test --> : timestamp: 7975753
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 7975754
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7975754
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7975754
# 
# Validation Timestamp: 7975795: timestamp: 7975795
# fan 1 should power on: timestamp: 7975795

def r1_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7976754: timestamp: 7976754
# fan 2 should not power on: timestamp: 7976754

def r1_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 7976754
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 7976754
# 
# Validation Timestamp: 7976795: timestamp: 7976795
# both fans are available: timestamp: 7976795

def r1_tc3_test():
    """
    Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7976795: timestamp: 7976795
# low fan speed: timestamp: 7976795

def r1_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 7976795
