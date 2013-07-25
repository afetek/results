# Get Script Variables: timestamp: 48432655
# generated script variable --> self.fan1_fault = False: timestamp: 48432670
# generated script variable --> self.fan2_fault = True: timestamp: 48432690
# generated script variable --> self.TEST_RUN = "r3": timestamp: 48432710
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 48432730
# Test Setup --> r3 Debug Level: 3: timestamp: 48432736
# Start Test --> : timestamp: 48433040
# Powerup Test Script: timestamp: 48433041
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 48433041
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 48433041
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 48433041
# Validation Timestamp: 48433081: timestamp: 48433081
# fan 1 should power on: timestamp: 48433081

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 48434041: timestamp: 48434041
# fan 2 should not power on: timestamp: 48434041

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 48434041: timestamp: 48434041
# Both fans are Available EICAS message: timestamp: 48434041

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 48434041
