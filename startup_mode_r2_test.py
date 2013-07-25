# Get Script Variables: timestamp: 43839846
# Conversion for fan1_fault (enum) is (enum): timestamp: 43839856
# generated script variable --> self.fan1_fault = True: timestamp: 43839861
# Conversion for fan2_fault is (none): timestamp: 43839876
# generated script variable --> self.fan2_fault = "False": timestamp: 43839881
# Conversion for TEST_RUN is (none): timestamp: 43839896
# generated script variable --> self.TEST_RUN = "r2": timestamp: 43839901
# Conversion for description is (none): timestamp: 43839916
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 43839921
# Test Setup --> r2 Debug Level: 3: timestamp: 43839927
# Start Test --> : timestamp: 43840283
# Powerup Test Script: timestamp: 43840284
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 43840284
# Assignment: self.model.fan1FaultRead.Value = 1.0: timestamp: 43840284
# Assignment: self.model.fan2FaultRead.Value = 1.0: timestamp: 43840284
# Assignment: self.model.powerECU.Value = 1.0: timestamp: 43840284
# Validation Timestamp: 43841284: timestamp: 43841284
# fan 2 should power on: timestamp: 43841284

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is >= 1 and <= 1: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 43841284: timestamp: 43841284
# fan 1 should not power on: timestamp: 43841284

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is < 1 or > 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 43841284: timestamp: 43841284
# Fan 2 is available EICAS message: timestamp: 43841284

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is >= 2 and <= 2: actual value is 0.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 43841284
