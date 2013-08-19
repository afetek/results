# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r3
# Description: Fan2 faulted at startup
# #######################################################
# : timestamp: 6889385
# Start Test: : timestamp: 6889675
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 6889676
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 6889676
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 6889676
# 
# Validation Timestamp: 6889707: timestamp: 6889707
# fan 1 should power on: timestamp: 6889707

def r3_tc1_test():
    """
    FANSPEED r3 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6890676: timestamp: 6890676
# fan 2 should not power on: timestamp: 6890676

def r3_tc2_test():
    """
    FANSPEED r3 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 6890676
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 6890676
# 
# Validation Timestamp: 6890679: timestamp: 6890679
# only fan 1 is available: timestamp: 6890679

def r3_tc3_test():
    """
    FANSPEED r3 tc3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6890679: timestamp: 6890679
# low fan speed: timestamp: 6890679

def r3_tc4_test():
    """
    FANSPEED r3 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r3: timestamp: 6890679
