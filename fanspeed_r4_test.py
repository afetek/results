# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r4
# Description: Fan1 and Fan2 faulted at startup
# #######################################################
# : timestamp: 6892424
# Start Test: : timestamp: 6892857
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 6892858
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 6892858
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 6892858
# 
# Validation Timestamp: 6893858: timestamp: 6893858
# fan 1 should not power on: timestamp: 6893858

def r4_tc1_test():
    """
    FANSPEED r4 tc1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6893858: timestamp: 6893858
# fan 2 should not power on: timestamp: 6893858

def r4_tc2_test():
    """
    FANSPEED r4 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6893858: timestamp: 6893858
# no fans available: timestamp: 6893858

def r4_tc3_test():
    """
    FANSPEED r4 tc3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 6893858
