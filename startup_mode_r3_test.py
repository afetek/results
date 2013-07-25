# Get Script Variables: timestamp: 69168101
# test data variable --> self.fan1_fault = False: timestamp: 69168116
# test data variable --> self.fan2_fault = True: timestamp: 69168136
# test data variable --> self.TEST_RUN = "r3": timestamp: 69168156
# test data variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 69168176
# Test Setup --> r3 Debug Level: 3: timestamp: 69168182
# Start Test --> : timestamp: 69168524
# Powerup Test Script: timestamp: 69168525
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 69168525
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 69168525
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 69168525
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 69168525
# 
# Validation Timestamp: 69168565: timestamp: 69168565
# fan 1 should power on: timestamp: 69168565

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 69169525: timestamp: 69169525
# fan 2 should not power on: timestamp: 69169525

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 69169525
# 
# Validation Timestamp: 69169556: timestamp: 69169556
# only fan 1 is available: timestamp: 69169556

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 69169556: timestamp: 69169556
# low fan speed: timestamp: 69169556

def test4_test_test():
    """
     run r3 test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r3: timestamp: 69169556
