# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r5
# Description: Fans OK, powerup to startup
# #######################################################
# : timestamp: 12040898
# Start Test: : timestamp: 12041029
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 12041030
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 12041030
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 12041030
# 
# Validation Timestamp: 12041061: timestamp: 12041061
# fan 1 should power on: timestamp: 12041061

def r5_tc1_test():
    """
    r5_tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 12042030: timestamp: 12042030
# fan 2 should not power on: timestamp: 12042030

def r5_tc2_test():
    """
    r5_tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 12042030
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 12042030
# 
# Validation Timestamp: 12042081: timestamp: 12042081
# both fans are available: timestamp: 12042081

def r5_tc3_test():
    """
    r5_tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 12042081: timestamp: 12042081
# low fan speed: timestamp: 12042081

def r5_tc4_test():
    """
    r5_tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r5: timestamp: 12042081
