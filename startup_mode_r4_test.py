# Get Script Variables: timestamp: 43845922
# Conversion for fan1_fault (enum) is (enum): timestamp: 43845932
# generated script variable --> self.fan1_fault = True: timestamp: 43845937
# Conversion for fan2_fault is (none): timestamp: 43845952
# generated script variable --> self.fan2_fault = "True": timestamp: 43845957
# Conversion for TEST_RUN is (none): timestamp: 43845972
# generated script variable --> self.TEST_RUN = "r4": timestamp: 43845977
# Conversion for description is (none): timestamp: 43845992
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 43845997
# Test Setup --> r4 Debug Level: 3: timestamp: 43846003
# Start Test --> : timestamp: 43846291
# Powerup Test Script: timestamp: 43846292
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 43846292
# Assignment: self.model.fan1FaultRead.Value = 1.0: timestamp: 43846292
# Assignment: self.model.fan2FaultRead.Value = 1.0: timestamp: 43846292
# Assignment: self.model.powerECU.Value = 1.0: timestamp: 43846292
# Validation Timestamp: 43846350: timestamp: 43846350
# No Fans Available EICAS message: timestamp: 43846350

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is >= 0 and <= 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 43847292: timestamp: 43847292
# fan 2 should not power on: timestamp: 43847292

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 43847292: timestamp: 43847292
# fan 1 should not power on: timestamp: 43847292

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 43847292
