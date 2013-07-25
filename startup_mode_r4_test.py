# Get Script Variables: timestamp: 51609392
# generated script variable --> self.fan1_fault = True: timestamp: 51609407
# generated script variable --> self.fan2_fault = True: timestamp: 51609427
# generated script variable --> self.TEST_RUN = "r4": timestamp: 51609447
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 51609467
# Test Setup --> r4 Debug Level: 3: timestamp: 51609473
# Start Test --> : timestamp: 51609704
# Powerup Test Script: timestamp: 51609705
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 51609705
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 51609705
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 51609705
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 51609705
# 
# Validation Timestamp: 51609775: timestamp: 51609775
# No Fans Available EICAS message: timestamp: 51609775

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 51610705: timestamp: 51610705
# fan 2 should not power on: timestamp: 51610705

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 51610705: timestamp: 51610705
# fan 1 should not power on: timestamp: 51610705

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 51610705
