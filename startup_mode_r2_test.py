# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 8642081
# Start Test: : timestamp: 8642211
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 8642212
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 8642212
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 8642212
# 
# Validation Timestamp: 8642256: timestamp: 8642256
# fan 2 should power on: timestamp: 8642256

def r2_tc1_test():
    """
    Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8643212: timestamp: 8643212
# fan 1 should not power on: timestamp: 8643212

def r2_tc2_test():
    """
    Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 8643212
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 8643212
# 
# Validation Timestamp: 8643226: timestamp: 8643226
# only fan 2 is available: timestamp: 8643226

def r2_tc3_test():
    """
    Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8643226: timestamp: 8643226
# low fan speed: timestamp: 8643226

def r2_tc4_test():
    """
    Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 8643226
