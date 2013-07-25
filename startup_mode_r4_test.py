# #######################################################
# Test Name: Powerup Mode Test
# Requirements Under Test: 5,6,7,8
# #######################################################
# : timestamp: 74333064
# Get Test Data Variables: timestamp: 74333065
# test data variable --> self.fan1_fault = True: timestamp: 74333080
# test data variable --> self.fan2_fault = True: timestamp: 74333100
# test data variable --> self.TEST_RUN = "r4": timestamp: 74333120
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 74333140
# Test Setup --> r4 Debug Level: 3: timestamp: 74333146
# Start Test --> : timestamp: 74333477
# Powerup Test Script: timestamp: 74333478
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 74333478
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 74333478
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 74333478
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 74333478
# 
# Validation Timestamp: 74334478: timestamp: 74334478
# fan 1 should not power on: timestamp: 74334478

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 74334478: timestamp: 74334478
# fan 2 should not power on: timestamp: 74334478

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# 
# Validation Timestamp: 74334478: timestamp: 74334478
# no fans available: timestamp: 74334478

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# Test Done --> r4: timestamp: 74334478
