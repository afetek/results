# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 82352771
# Get Test Data Variables: timestamp: 82352772
# test data variable --> self.fan1_fault = False: timestamp: 82352787
# test data variable --> self.fan2_fault = True: timestamp: 82352807
# test data variable --> self.TEST_RUN = "r3": timestamp: 82352827
# test data variable --> self.powerup = False: timestamp: 82352847
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 82352867
# Test Setup --> r3 Debug Level: 3: timestamp: 82352873
# Start Test --> : timestamp: 82353227
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 82353228
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 82353228
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 82353228
# 
# Validation Timestamp: 82353269: timestamp: 82353269
# fan 1 should power on: timestamp: 82353269

def test1_test_test():
    """
    Run r3 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 82354228: timestamp: 82354228
# fan 2 should not power on: timestamp: 82354228

def test2_test_test():
    """
    Run r3 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 82354228
# 
# Validation Timestamp: 82354248: timestamp: 82354248
# only fan 1 is available: timestamp: 82354248

def test3_test_test():
    """
    Run r3 Test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 82354248: timestamp: 82354248
# low fan speed: timestamp: 82354248

def test4_test_test():
    """
    Run r3 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r3: timestamp: 82354248
