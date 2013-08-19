# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 19563561
# Start Test: : timestamp: 19563857
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 19563858
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 19563858
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 19563858
# 
# Validation Timestamp: 19563887: timestamp: 19563887
# fan 1 should power on: timestamp: 19563887

def r5_tc1_test():
    """
    STARTUP r5 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 19564858: timestamp: 19564858
# fan 2 should not power on: timestamp: 19564858

def r5_tc2_test():
    """
    STARTUP r5 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 19564858
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 19564858
# 
# Validation Timestamp: 19564889: timestamp: 19564889
# both fans are available: timestamp: 19564889

def r5_tc3_test():
    """
    STARTUP r5 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 19564889: timestamp: 19564889
# low fan speed: timestamp: 19564889

def r5_tc4_test():
    """
    STARTUP r5 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 19564889
