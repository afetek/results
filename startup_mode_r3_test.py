# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 8645122
# Start Test: : timestamp: 8645354
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 8645355
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 8645355
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 8645355
# 
# Validation Timestamp: 8645395: timestamp: 8645395
# fan 1 should power on: timestamp: 8645395

def r3_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8646355: timestamp: 8646355
# fan 2 should not power on: timestamp: 8646355

def r3_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 8646355
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 8646355
# 
# Validation Timestamp: 8646386: timestamp: 8646386
# only fan 1 is available: timestamp: 8646386

def r3_tc3_test():
    """
    Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8646386: timestamp: 8646386
# low fan speed: timestamp: 8646386

def r3_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 8646386
