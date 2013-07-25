# Get Script Variables: timestamp: 47426139
# Convert value for fan1_fault (enum) to a boolean: timestamp: 47426149
# generated script variable --> self.fan1_fault = False: timestamp: 47426154
# Convert value for fan2_fault (enum) to a boolean: timestamp: 47426169
# generated script variable --> self.fan2_fault = True: timestamp: 47426174
# Convert value for TEST_RUN to a str | float: timestamp: 47426189
# generated script variable --> self.TEST_RUN = "r3": timestamp: 47426194
# Convert value for description to a str | float: timestamp: 47426209
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 47426214
# Test Setup --> r3 Debug Level: 3: timestamp: 47426220
# Start Test --> : timestamp: 47426539
# Powerup Test Script: timestamp: 47426540
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47426540
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 47426540
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47426540
# Validation Timestamp: 47426584: timestamp: 47426584
# fan 1 should power on: timestamp: 47426584

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1 and 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47427540: timestamp: 47427540
# fan 2 should not power on: timestamp: 47427540

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47427540: timestamp: 47427540
# Both fans are Available EICAS message: timestamp: 47427540

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1 and 1: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 47427540
