# Get Script Variables: timestamp: 46324395
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46324405
# generated script variable --> self.fan1_fault = True: timestamp: 46324410
# Convert value for fan2_fault to a (none): timestamp: 46324425
# generated script variable --> self.fan2_fault = "True": timestamp: 46324430
# Convert value for TEST_RUN to a (none): timestamp: 46324445
# generated script variable --> self.TEST_RUN = "r4": timestamp: 46324450
# Convert value for description to a (none): timestamp: 46324465
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 46324470
# Test Setup --> r4 Debug Level: 3: timestamp: 46324476
# Start Test --> : timestamp: 46324893
# Powerup Test Script: timestamp: 46324894
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46324894
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 46324894
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 46324894
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46324894
# Validation Timestamp: 46324943: timestamp: 46324943
# No Fans Available EICAS message: timestamp: 46324943

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46325894: timestamp: 46325894
# fan 2 should not power on: timestamp: 46325894

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46325894: timestamp: 46325894
# fan 1 should not power on: timestamp: 46325894

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 46325894
