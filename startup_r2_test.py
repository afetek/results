# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 4007798
# Start Test: : timestamp: 4008027
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 4008028
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 4008028
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4008028
# 
# Validation Timestamp: 4008068: timestamp: 4008068
# fan 2 should power on: timestamp: 4008068

def r2_tc1_test():
    """
    STARTUP r2 tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 4009028: timestamp: 4009028
# fan 1 should not power on: timestamp: 4009028

def r2_tc2_test():
    """
    STARTUP r2 tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 4009028
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 4009028
# 
# Validation Timestamp: 4009039: timestamp: 4009039
# only fan 2 is available: timestamp: 4009039

def r2_tc3_test():
    """
    STARTUP r2 tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 4009039: timestamp: 4009039
# low fan speed: timestamp: 4009039

def r2_tc4_test():
    """
    STARTUP r2 tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 4009039
