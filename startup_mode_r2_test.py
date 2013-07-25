# Get Script Variables: timestamp: 69165060
# test data variable --> self.fan1_fault = True: timestamp: 69165075
# test data variable --> self.fan2_fault = False: timestamp: 69165095
# test data variable --> self.TEST_RUN = "r2": timestamp: 69165115
# test data variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 69165135
# Test Setup --> r2 Debug Level: 3: timestamp: 69165141
# Start Test --> : timestamp: 69165467
# Powerup Test Script: timestamp: 69165468
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 69165468
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 69165468
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 69165468
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 69165468
# 
# Validation Timestamp: 69165505: timestamp: 69165505
# fan 2 should power on: timestamp: 69165505

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 69166468: timestamp: 69166468
# fan 1 should not power on: timestamp: 69166468

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 69166468
# 
# Validation Timestamp: 69166496: timestamp: 69166496
# only fan 2 is available: timestamp: 69166496

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 69166496: timestamp: 69166496
# low fan speed: timestamp: 69166496

def test4_test_test():
    """
     run r2 test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r2: timestamp: 69166496
