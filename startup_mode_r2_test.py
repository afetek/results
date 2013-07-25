# Get Script Variables: timestamp: 48429604
# generated script variable --> self.fan1_fault = True: timestamp: 48429619
# generated script variable --> self.fan2_fault = False: timestamp: 48429639
# generated script variable --> self.TEST_RUN = "r2": timestamp: 48429659
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 48429679
# Test Setup --> r2 Debug Level: 3: timestamp: 48429685
# Start Test --> : timestamp: 48430036
# Powerup Test Script: timestamp: 48430037
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 48430037
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 48430037
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 48430037
# Validation Timestamp: 48430061: timestamp: 48430061
# fan 2 should power on: timestamp: 48430061

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 48431037: timestamp: 48431037
# fan 1 should not power on: timestamp: 48431037

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 48431037: timestamp: 48431037
# Fan 2 is available EICAS message: timestamp: 48431037

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 48431037
