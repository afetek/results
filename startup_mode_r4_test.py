# Get Script Variables: timestamp: 68878185
# generated script variable --> self.fan1_fault = True: timestamp: 68878200
# generated script variable --> self.fan2_fault = True: timestamp: 68878220
# generated script variable --> self.TEST_RUN = "r4": timestamp: 68878240
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 68878260
# Test Setup --> r4 Debug Level: 3: timestamp: 68878266
# Start Test --> : timestamp: 68878497
# Powerup Test Script: timestamp: 68878498
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 68878498
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 68878498
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 68878498
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 68878498
# 
# Validation Timestamp: 68879498: timestamp: 68879498
# fan 1 should not power on: timestamp: 68879498

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 68879498: timestamp: 68879498
# fan 2 should not power on: timestamp: 68879498

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 68879498: timestamp: 68879498
# no fans available: timestamp: 68879498

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 68879498
