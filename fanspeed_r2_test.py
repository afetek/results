# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 6353160
# Start Test: : timestamp: 6353471
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 6353472
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 6353472
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 6353472
# 
# Validation Timestamp: 6353510: timestamp: 6353510
# fan 2 should power on: timestamp: 6353510

def r2_tc1_test():
    """
    FANSPEED r2 tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6354472: timestamp: 6354472
# fan 1 should not power on: timestamp: 6354472

def r2_tc2_test():
    """
    FANSPEED r2 tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 6354472
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 6354472
# 
# Validation Timestamp: 6354481: timestamp: 6354481
# only fan 2 is available: timestamp: 6354481

def r2_tc3_test():
    """
    FANSPEED r2 tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6354481: timestamp: 6354481
# low fan speed: timestamp: 6354481

def r2_tc4_test():
    """
    FANSPEED r2 tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 6354481
