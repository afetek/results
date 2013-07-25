# Get Script Variables: timestamp: 51606359
# generated script variable --> self.fan1_fault = False: timestamp: 51606374
# generated script variable --> self.fan2_fault = True: timestamp: 51606394
# generated script variable --> self.TEST_RUN = "r3": timestamp: 51606414
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 51606434
# Test Setup --> r3 Debug Level: 3: timestamp: 51606440
# Start Test --> : timestamp: 51606768
# Powerup Test Script: timestamp: 51606769
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 51606769
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 51606769
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 51606769
# 
# Validation Timestamp: 51606804: timestamp: 51606804
# fan 1 should power on: timestamp: 51606804

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 51607769: timestamp: 51607769
# fan 2 should not power on: timestamp: 51607769

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 51607769: timestamp: 51607769
# Both fans are Available EICAS message: timestamp: 51607769

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 51607769
