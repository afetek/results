# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Description: Fan1 Fault Fan2 ok at startup mode
# #######################################################
# : timestamp: 8204492
# Start Test: : timestamp: 8204624
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 8204625
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 8204625
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 8204625
# 
# Validation Timestamp: 8204654: timestamp: 8204654
# fan 2 should power on: timestamp: 8204654

def r2_tc1_test():
    """
    Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8205625: timestamp: 8205625
# fan 1 should not power on: timestamp: 8205625

def r2_tc2_test():
    """
    Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 8205625
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 8205625
# 
# Validation Timestamp: 8205645: timestamp: 8205645
# only fan 2 is available: timestamp: 8205645

def r2_tc3_test():
    """
    Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8205645: timestamp: 8205645
# low fan speed: timestamp: 8205645

def r2_tc4_test():
    """
    Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 8205645
