# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r4
# Description: Fan1 and Fan2 faulted at startup
# #######################################################
# : timestamp: 5782273
# Start Test: : timestamp: 5782466
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 5782467
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 5782467
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 5782467
# 
# Validation Timestamp: 5783467: timestamp: 5783467
# fan 1 should not power on: timestamp: 5783467

def r4_tc1_test():
    """
    STARTUP r4 tc1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5783467: timestamp: 5783467
# fan 2 should not power on: timestamp: 5783467

def r4_tc2_test():
    """
    STARTUP r4 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5783467: timestamp: 5783467
# no fans available: timestamp: 5783467

def r4_tc3_test():
    """
    STARTUP r4 tc3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 5783467
