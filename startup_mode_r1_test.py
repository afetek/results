# Get Script Variables: timestamp: 48426560
# generated script variable --> self.fan1_fault = False: timestamp: 48426575
# generated script variable --> self.fan2_fault = False: timestamp: 48426595
# generated script variable --> self.TEST_RUN = "r1": timestamp: 48426615
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 48426635
# Test Setup --> r1 Debug Level: 3: timestamp: 48426641
# Start Test --> : timestamp: 48426904
# Powerup Test Script: timestamp: 48426905
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 48426905
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 48426905
# Validation Timestamp: 48426941: timestamp: 48426941
# fan 1 should power on: timestamp: 48426941

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 48427905: timestamp: 48427905
# fan 2 should not power on: timestamp: 48427905

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 48427905: timestamp: 48427905
# Both fans are Available EICAS message: timestamp: 48427905

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 48427905
