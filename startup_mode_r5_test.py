# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81608223
# Get Test Data Variables: timestamp: 81608224
# test data variable --> self.fan1_fault = False: timestamp: 81608227
# test data variable --> self.fan2_fault = False: timestamp: 81608231
# test data variable --> self.TEST_RUN = "r5": timestamp: 81608235
# test data variable --> self.powerup = True: timestamp: 81608239
# test data variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 81608243
# Test Setup --> r5 Debug Level: 3: timestamp: 81608245
# Start Test --> : timestamp: 81608643
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 81608644
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 81608644
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81608644
# 
# Validation Timestamp: 81662353: timestamp: 81662353
# fan 1 should power on: timestamp: 81662353

def test1_test_test():
    """
    Run r5 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81663353: timestamp: 81663353
# fan 2 should not power on: timestamp: 81663353

def test2_test_test():
    """
    Run r5 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 81663353
# 
# Validation Timestamp: 81663398: timestamp: 81663398
# both fans are available: timestamp: 81663398

def test3_test_test():
    """
    Run r5 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81663398: timestamp: 81663398
# low fan speed: timestamp: 81663398

def test4_test_test():
    """
    Run r5 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r5: timestamp: 81663398
