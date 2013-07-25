# Get Script Variables: timestamp: 46318327
# Convert value for fan1_fault (enum) to a (enum): timestamp: 46318337
# generated script variable --> self.fan1_fault = True: timestamp: 46318342
# Convert value for fan2_fault to a (none): timestamp: 46318357
# generated script variable --> self.fan2_fault = "False": timestamp: 46318362
# Convert value for TEST_RUN to a (none): timestamp: 46318377
# generated script variable --> self.TEST_RUN = "r2": timestamp: 46318382
# Convert value for description to a (none): timestamp: 46318397
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 46318402
# Test Setup --> r2 Debug Level: 3: timestamp: 46318408
# Start Test --> : timestamp: 46318743
# Powerup Test Script: timestamp: 46318744
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 46318744
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 46318744
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 46318744
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 46318744
# Validation Timestamp: 46319744: timestamp: 46319744
# fan 2 should power on: timestamp: 46319744

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1 and 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 46319744: timestamp: 46319744
# fan 1 should not power on: timestamp: 46319744

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 46319744: timestamp: 46319744
# Fan 2 is available EICAS message: timestamp: 46319744

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2 and 2: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 46319744
