# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 5493048
# Start Test: : timestamp: 5493278
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 5493279
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 5493279
# Assigned value 0.0 to variable self.model.enableCanTx: timestamp: 5493279
# 
# Validation Timestamp: 5572790: timestamp: 5572790
# fan 1 should power on: timestamp: 5572790

def r5_tc1_test():
    """
    r5_tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5572790: timestamp: 5572790
# fan 2 should not power on: timestamp: 5572790

def r5_tc2_test():
    """
    r5_tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 5572790
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 5572790
# 
# Validation Timestamp: 5573790: timestamp: 5573790
# both fans are available: timestamp: 5573790

def r5_tc3_test():
    """
    r5_tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    ##########################
    TEST_STATUS = '''FAILED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5573790: timestamp: 5573790
# low fan speed: timestamp: 5573790

def r5_tc4_test():
    """
    r5_tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 5573790
