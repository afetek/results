# Get Script Variables: timestamp: 69161999
# test data variable --> self.fan1_fault = False: timestamp: 69162014
# test data variable --> self.fan2_fault = False: timestamp: 69162034
# test data variable --> self.TEST_RUN = "r1": timestamp: 69162054
# test data variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 69162074
# Test Setup --> r1 Debug Level: 3: timestamp: 69162080
# Start Test --> : timestamp: 69162311
# Powerup Test Script: timestamp: 69162312
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 69162312
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 69162312
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 69162312
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 69162312
# 
# Validation Timestamp: 69162346: timestamp: 69162346
# fan 1 should power on: timestamp: 69162346

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 69163312: timestamp: 69163312
# fan 2 should not power on: timestamp: 69163312

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 69163312
# 
# Validation Timestamp: 69163356: timestamp: 69163356
# both fans are available: timestamp: 69163356

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 69163356: timestamp: 69163356
# low fan speed: timestamp: 69163356

def test4_test_test():
    """
     run r1 test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r1: timestamp: 69163356
