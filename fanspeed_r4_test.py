# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r4
# Description: Fan1 and Fan2 faulted at startup
# #######################################################
# : timestamp: 7449543
# Start Test: : timestamp: 7449737
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 7449738
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 7449738
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7449738
# 
# Validation Timestamp: 7450738: timestamp: 7450738
# fan 1 should not power on: timestamp: 7450738

def r4_tc1_test():
    """
    FANSPEED r4 tc1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7450738: timestamp: 7450738
# fan 2 should not power on: timestamp: 7450738

def r4_tc2_test():
    """
    FANSPEED r4 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7450738: timestamp: 7450738
# no fans available: timestamp: 7450738

def r4_tc3_test():
    """
    FANSPEED r4 tc3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 7450738
