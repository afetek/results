# #######################################################
# Test Name: FANSPEED
# Requirements Under Test: 16, 17, 18, 19, 20
# Test Run: r2
# Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 6886344
# Start Test: : timestamp: 6886636
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 6886637
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 6886637
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 6886637
# 
# Validation Timestamp: 6886667: timestamp: 6886667
# fan 2 should power on: timestamp: 6886667

def r2_tc1_test():
    """
    FANSPEED r2 tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6887637: timestamp: 6887637
# fan 1 should not power on: timestamp: 6887637

def r2_tc2_test():
    """
    FANSPEED r2 tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 6887637
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 6887637
# 
# Validation Timestamp: 6887659: timestamp: 6887659
# only fan 2 is available: timestamp: 6887659

def r2_tc3_test():
    """
    FANSPEED r2 tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 6887659: timestamp: 6887659
# low fan speed: timestamp: 6887659

def r2_tc4_test():
    """
    FANSPEED r2 tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 6887659
