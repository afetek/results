# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r4
# Description: Fan1 and Fan2 faulted at startup
# #######################################################
# : timestamp: 4013873
# Start Test: : timestamp: 4014003
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 4014004
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 4014004
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 4014004
# 
# Validation Timestamp: 4015004: timestamp: 4015004
# fan 1 should not power on: timestamp: 4015004

def r4_tc1_test():
    """
    STARTUP r4 tc1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 4015004: timestamp: 4015004
# fan 2 should not power on: timestamp: 4015004

def r4_tc2_test():
    """
    STARTUP r4 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 4015004: timestamp: 4015004
# no fans available: timestamp: 4015004

def r4_tc3_test():
    """
    STARTUP r4 tc3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 4015004
