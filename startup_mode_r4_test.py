# Get Script Variables: timestamp: 48435701
# generated script variable --> self.fan1_fault = True: timestamp: 48435716
# generated script variable --> self.fan2_fault = True: timestamp: 48435736
# generated script variable --> self.TEST_RUN = "r4": timestamp: 48435756
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 48435776
# Test Setup --> r4 Debug Level: 3: timestamp: 48435782
# Start Test --> : timestamp: 48436062
# Powerup Test Script: timestamp: 48436063
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 48436063
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 48436063
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 48436063
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 48436063
# Validation Timestamp: 48436131: timestamp: 48436131
# No Fans Available EICAS message: timestamp: 48436131

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 48437063: timestamp: 48437063
# fan 2 should not power on: timestamp: 48437063

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 48437063: timestamp: 48437063
# fan 1 should not power on: timestamp: 48437063

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 48437063
