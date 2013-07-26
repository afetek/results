# #######################################################
# Test Name: Powerup Mode
# Requirements Under Test: 1,5,6,7,8
# #######################################################
# : timestamp: 81431842
# Get Test Data Variables: timestamp: 81431843
# test data variable --> self.fan1_fault = False: timestamp: 81431846
# test data variable --> self.fan2_fault = False: timestamp: 81431850
# test data variable --> self.TEST_RUN = "r1": timestamp: 81431854
# test data variable --> self.powerup = False: timestamp: 81431858
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 81431862
# Test Setup --> r1 Debug Level: 3: timestamp: 81431864
# Start Test --> : timestamp: 81432254
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 81432255
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 81432255
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 81432255
# 
# Validation Timestamp: 81432292: timestamp: 81432292
# fan 1 should power on: timestamp: 81432292

def test1_test_test():
    """
    Run r1 Test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test1_test"


# 
# Validation Timestamp: 81433255: timestamp: 81433255
# fan 2 should not power on: timestamp: 81433255

def test2_test_test():
    """
    Run r1 Test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 81433255
# 
# Validation Timestamp: 81433291: timestamp: 81433291
# both fans are available: timestamp: 81433291

def test3_test_test():
    """
    Run r1 Test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test3_test"


# 
# Validation Timestamp: 81433291: timestamp: 81433291
# low fan speed: timestamp: 81433291

def test4_test_test():
    """
    Run r1 Test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "Failed test4_test"


# Test Done --> r1: timestamp: 81433291
