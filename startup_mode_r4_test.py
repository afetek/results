# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r4
# Test Run Description: Fan1 faulted Fan2 faulted at startup mode
# #######################################################
# : timestamp: 7984648
# Test Setup --> r4 Debug Level: 3: timestamp: 7984649
# Start Test --> : timestamp: 7984879
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 7984880
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 7984880
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7984880
# 
# Validation Timestamp: 7985880: timestamp: 7985880
# fan 1 should not power on: timestamp: 7985880

def r4_tc1_test():
    """
    Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7985880: timestamp: 7985880
# fan 2 should not power on: timestamp: 7985880

def r4_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7985880: timestamp: 7985880
# no fans available: timestamp: 7985880

def r4_tc3_test():
    """
    Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r4: timestamp: 7985880
