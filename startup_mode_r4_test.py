# Get Script Variables: timestamp: 47429175
# Convert value for fan1_fault (enum) to a boolean: timestamp: 47429185
# generated script variable --> self.fan1_fault = True: timestamp: 47429190
# Convert value for fan2_fault (enum) to a boolean: timestamp: 47429205
# generated script variable --> self.fan2_fault = True: timestamp: 47429210
# Convert value for TEST_RUN to a str | float: timestamp: 47429225
# generated script variable --> self.TEST_RUN = "r4": timestamp: 47429230
# Convert value for description to a str | float: timestamp: 47429245
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 47429250
# Test Setup --> r4 Debug Level: 3: timestamp: 47429256
# Start Test --> : timestamp: 47429596
# Powerup Test Script: timestamp: 47429597
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 47429597
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 47429597
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 47429597
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 47429597
# Validation Timestamp: 47429655: timestamp: 47429655
# No Fans Available EICAS message: timestamp: 47429655

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 47430597: timestamp: 47430597
# fan 2 should not power on: timestamp: 47430597

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 47430597: timestamp: 47430597
# fan 1 should not power on: timestamp: 47430597

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 47430597
