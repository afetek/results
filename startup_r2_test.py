# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 7829438
# Start Test: : timestamp: 7829630
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 7829631
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7829631
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7829631
# 
# Validation Timestamp: 7829668: timestamp: 7829668
# fan 2 should power on: timestamp: 7829668

def r2_tc1_test():
    """
    STARTUP r2 tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7830631: timestamp: 7830631
# fan 1 should not power on: timestamp: 7830631

def r2_tc2_test():
    """
    STARTUP r2 tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 7830631
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 7830631
# 
# Validation Timestamp: 7830639: timestamp: 7830639
# only fan 2 is available: timestamp: 7830639

def r2_tc3_test():
    """
    STARTUP r2 tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7830639: timestamp: 7830639
# low fan speed: timestamp: 7830639

def r2_tc4_test():
    """
    STARTUP r2 tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 7830639
