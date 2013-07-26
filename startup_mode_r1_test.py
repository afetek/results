# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1
# Description: Fan1 ok, Fan2 ok at startup mode test
# #######################################################
# : timestamp: 8201448
# Start Test: : timestamp: 8201580
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 8201581
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 8201581
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 8201581
# 
# Validation Timestamp: 8201614: timestamp: 8201614
# fan 1 should power on: timestamp: 8201614

def r1_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8202581: timestamp: 8202581
# fan 2 should not power on: timestamp: 8202581

def r1_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 8202581
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 8202581
# 
# Validation Timestamp: 8202625: timestamp: 8202625
# both fans are available: timestamp: 8202625

def r1_tc3_test():
    """
    Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8202625: timestamp: 8202625
# low fan speed: timestamp: 8202625

def r1_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 8202625
