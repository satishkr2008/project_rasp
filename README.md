# project_rasp
Collection of sample modules written in order to understand the working of raspberry pi.

- Pi doesnt start if provided power is not 5V.

- Bus is used to connect Pi with the Cobbler. Red line at one side of the bus suggest the side which needs to be mapped with the pin-1. Simmilarly use red line to map pin-1 of the cobbler.

- There are two types of GPIO pin mapping. 
	a. BCM - Broadcom SOC channel
	b. BOARD - physical pin numbers
  Python recognizes both numbering style.

- Check the functionality of the breadboard.

- Planes in the breadboard have vertical connection. Two lines allong side these planes have horizontal connection. These two lines are generally used as ground and power lines.

- A pin in the GPIO can be either used as output to send signal or as input to receive signal from the device. But cant be used as both at the same time.

