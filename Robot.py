from gpiozero import Motor, AngularServo
from time import sleep


class Robot:
    """
    Initial robot class for a 4 motored robot.

    Parameters
    ----------
    lf_motor: gpiozero.Motor
        The motor class for the left front motor.
    rf_motor: gpiozero.Motor
        The motor class for the right front motor.
    lb_motor: gpiozero.Motor
        The motor class for the left back motor.
    rb_motor: gpiozero.Motor
        The motor class for the right back motor.
    """
    def __init__(self, lf_motor: Motor, rf_motor: Motor, lb_motor: Motor, rb_motor: Motor):
        # TODO: Add angular servo motor inputs
        # TODO: Add vectorized motor control
        self.lf_motor = lf_motor
        self.rf_motor = rf_motor
        self.lb_motor = lb_motor
        self.rb_motor = rb_motor

    def stop_all_motors(self):
        self.lf_motor.stop()
        self.rf_motor.stop()
        self.lb_motor.stop()
        self.rb_motor.stop()

    def forward(self, speed: float = 1.0, time: float = 1.0):
        """Moves robot forwards by setting all motors forwards for allotted time."""
        self.lf_motor.forward(speed)
        self.rf_motor.forward(speed)
        self.lb_motor.forward(speed)
        self.rb_motor.forward(speed)
        sleep(time)
        self.stop_all_motors()

    def backward(self, speed: float = 1.0, time: float = 1.0):
        """Moves robot backwards by setting all motors backwards for allotted time."""
        self.lf_motor.backward(speed)
        self.rf_motor.backward(speed)
        self.lb_motor.backward(speed)
        self.rb_motor.backward(speed)
        sleep(time)
        self.stop_all_motors()

    def turn_left(self, speed: float = 1.0, time: float = 1.0):
        """Turns robot left by setting right motors forwards and left motors backwards for allotted time."""
        self.lf_motor.backward(speed)
        self.rf_motor.forward(speed)
        self.lb_motor.backward(speed)
        self.rb_motor.forward(speed)
        sleep(time)
        self.stop_all_motors()

    def turn_right(self, speed: float = 1.0, time: float = 1.0):
        """Turns robot right by setting right motors backwards and left motors forwards for allotted time."""
        self.lf_motor.forward(speed)
        self.rf_motor.backward(speed)
        self.lb_motor.forward(speed)
        self.rb_motor.backward(speed)
        sleep(time)
        self.stop_all_motors()
