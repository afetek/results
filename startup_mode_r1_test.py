# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81138768
# Get Test Data Variables: timestamp: 81138769
# test data variable --> self.TEST_RUN = "r1": timestamp: 81138772
# test data variable --> self.fan1_fault = False: timestamp: 81138776
# test data variable --> self.powerup = "False": timestamp: 81138780
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 81138784
# test data variable --> self.fan2_fault = False: timestamp: 81138788
# Test Setup --> r1 Debug Level: 3: timestamp: 81138790
# Start Test --> : timestamp: 81139192
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 81139193
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 81139193
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81139193
# 
# Validation Timestamp: 81177317: timestamp: 81177317
# fan 1 should power on: timestamp: 81177317

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81178317: timestamp: 81178317
# fan 2 should not power on: timestamp: 81178317

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 81178317
# 
# Validation Timestamp: 81178362: timestamp: 81178362
# both fans are available: timestamp: 81178362

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81178362: timestamp: 81178362
# low fan speed: timestamp: 81178362

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 81178362
