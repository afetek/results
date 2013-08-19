# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r3
# Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 5409307
# Start Test: : timestamp: 5409470
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 5409471
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 5409471
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 5409471
# 
# Validation Timestamp: 5409509: timestamp: 5409509
# fan 1 should power on: timestamp: 5409509

def r3_tc1_test():
    """
    STARTUP r3 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5410471: timestamp: 5410471
# fan 2 should not power on: timestamp: 5410471

def r3_tc2_test():
    """
    STARTUP r3 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 5410471
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 5410471
# 
# Validation Timestamp: 5410480: timestamp: 5410480
# only fan 1 is available: timestamp: 5410480

def r3_tc3_test():
    """
    STARTUP r3 tc3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5410480: timestamp: 5410480
# low fan speed: timestamp: 5410480

def r3_tc4_test():
    """
    STARTUP r3 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 5410480
