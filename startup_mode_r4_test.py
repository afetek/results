# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82734792
# Get Test Data Variables: timestamp: 82734793
# test data variable --> self.fan1_fault = True: timestamp: 82734808
# test data variable --> self.fan2_fault = True: timestamp: 82734828
# test data variable --> self.TEST_RUN = "r4": timestamp: 82734848
# test data variable --> self.powerup = False: timestamp: 82734868
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 82734888
# Test Setup --> r4 Debug Level: 3: timestamp: 82734894
# Start Test --> : timestamp: 82735114
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 82735115
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 82735115
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 82735115
# 
# Validation Timestamp: 82736115: timestamp: 82736115
# fan 1 should not power on: timestamp: 82736115

def test1_test_test():
    """
    Run r4 Test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82736115: timestamp: 82736115
# fan 2 should not power on: timestamp: 82736115

def test2_test_test():
    """
    Run r4 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# 
# Validation Timestamp: 82736115: timestamp: 82736115
# no fans available: timestamp: 82736115

def test3_test_test():
    """
    Run r4 Test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# Test Done --> r4: timestamp: 82736115
