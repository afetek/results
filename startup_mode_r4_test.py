# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r4
# Description: Fan1 and Fan2 faulted at startup
# #######################################################
# : timestamp: 8648166
# Start Test: : timestamp: 8648296
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 8648297
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 8648297
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 8648297
# 
# Validation Timestamp: 8649297: timestamp: 8649297
# fan 1 should not power on: timestamp: 8649297

def r4_tc1_test():
    """
    Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8649297: timestamp: 8649297
# fan 2 should not power on: timestamp: 8649297

def r4_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8649297: timestamp: 8649297
# no fans available: timestamp: 8649297

def r4_tc3_test():
    """
    Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 8649297
