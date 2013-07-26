# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 9342931
# Start Test: : timestamp: 9343062
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 9343063
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 9343063
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 9343063
# 
# Validation Timestamp: 9343097: timestamp: 9343097
# fan 2 should power on: timestamp: 9343097

def r2_tc1_test():
    """
    r2_tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 9344063: timestamp: 9344063
# fan 1 should not power on: timestamp: 9344063

def r2_tc2_test():
    """
    r2_tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 9344063
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 9344063
# 
# Validation Timestamp: 9344076: timestamp: 9344076
# only fan 2 is available: timestamp: 9344076

def r2_tc3_test():
    """
    r2_tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 9344076: timestamp: 9344076
# low fan speed: timestamp: 9344076

def r2_tc4_test():
    """
    r2_tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 9344076
