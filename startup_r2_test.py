# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 3301703
# Start Test: : timestamp: 3301932
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 3301933
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 3301933
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 3301933
# 
# Validation Timestamp: 3301967: timestamp: 3301967
# fan 2 should power on: timestamp: 3301967

def r2_tc1_test():
    """
    STARTUP r2 tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 3302933: timestamp: 3302933
# fan 1 should not power on: timestamp: 3302933

def r2_tc2_test():
    """
    STARTUP r2 tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 3302933
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 3302933
# 
# Validation Timestamp: 3302949: timestamp: 3302949
# only fan 2 is available: timestamp: 3302949

def r2_tc3_test():
    """
    STARTUP r2 tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 3302949: timestamp: 3302949
# low fan speed: timestamp: 3302949

def r2_tc4_test():
    """
    STARTUP r2 tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 3302949
