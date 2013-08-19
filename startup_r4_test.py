# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r4
# Description: Fan1 and Fan2 faulted at startup
# #######################################################
# : timestamp: 6374820
# Start Test: : timestamp: 6375010
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 6375011
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 6375011
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 6375011
# 
# Validation Timestamp: 6376011: timestamp: 6376011
# fan 1 should not power on: timestamp: 6376011

def r4_tc1_test():
    """
    STARTUP r4 tc1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6376011: timestamp: 6376011
# fan 2 should not power on: timestamp: 6376011

def r4_tc2_test():
    """
    STARTUP r4 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6376011: timestamp: 6376011
# no fans available: timestamp: 6376011

def r4_tc3_test():
    """
    STARTUP r4 tc3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 6376011
