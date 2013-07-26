# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r4
# Description: Fan1 and Fan2 faulted at startup
# #######################################################
# : timestamp: 12037848
# Start Test: : timestamp: 12038079
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 12038080
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 12038080
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 12038080
# 
# Validation Timestamp: 12039080: timestamp: 12039080
# fan 1 should not power on: timestamp: 12039080

def r4_tc1_test():
    """
    r4_tc1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 12039080: timestamp: 12039080
# fan 2 should not power on: timestamp: 12039080

def r4_tc2_test():
    """
    r4_tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 12039080: timestamp: 12039080
# no fans available: timestamp: 12039080

def r4_tc3_test():
    """
    r4_tc3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 12039080
