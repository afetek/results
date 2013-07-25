# Get Script Variables: timestamp: 9861609
# conversion: (enum): timestamp: 9861619
# generated script variable --> self.fan1_fault = False: timestamp: 9861624
# conversion: (none): timestamp: 9861639
# generated script variable --> self.fan2_fault = "True": timestamp: 9861644
# conversion: (none): timestamp: 9861659
# generated script variable --> self.TEST_RUN = "r3": timestamp: 9861664
# conversion: (none): timestamp: 9861679
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 9861684
# Test Setup --> r3 Debug Level: 3: timestamp: 9861690
# Start Test --> : timestamp: 9861928
# Powerup Test Script: timestamp: 9861929
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 9861929
# self.model.fan2FaultRead.Value == 1.0: timestamp: 9861929
# self.model.powerECU.Value == 1.0: timestamp: 9861929
# Validation Timestamp: 9861965: timestamp: 9861965
# fan 1 should power on: timestamp: 9861965

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is >= 1 and <= 1: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 9862929: timestamp: 9862929
# fan 2 should not power on: timestamp: 9862929

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 9862929: timestamp: 9862929
# Both fans are Available EICAS message: timestamp: 9862929

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is >= 1 and <= 1: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 9862929
