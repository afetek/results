# Get Script Variables: timestamp: 46815484
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46815494
# generated script variable --> self.fan1_fault = True: timestamp: 46815499
# Convert value for fan2_fault (enum) to a (enum): timestamp: 46815514
# generated script variable --> self.fan2_fault = True: timestamp: 46815519
# Convert value for TEST_RUN to a (none): timestamp: 46815534
# generated script variable --> self.TEST_RUN = "r4": timestamp: 46815539
# Convert value for description to a (none): timestamp: 46815554
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 46815559
# Test Setup --> r4 Debug Level: 3: timestamp: 46815565
# Start Test --> : timestamp: 46815814
# Powerup Test Script: timestamp: 46815815
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46815815
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 46815815
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 46815815
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46815815
# Validation Timestamp: 46815861: timestamp: 46815861
# No Fans Available EICAS message: timestamp: 46815861

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46816815: timestamp: 46816815
# fan 2 should not power on: timestamp: 46816815

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46816815: timestamp: 46816815
# fan 1 should not power on: timestamp: 46816815

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 46816815
