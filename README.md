Raspbery Pi Pico W setup
========================

https://www.raspberrypi.com/documentation/microcontrollers/micropython.html

1. Download [MicroPython for Pi Pico W](https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2) (as `RPI_PICO_W-20240222-v1.22.2.uf2`)
2. Install onto the board
    1. Hold down bootsel button and plug in over USB (with micro USB cable supporting power+data)
    2. Drag and drop `.uf2` file onto drive that appears
    3. (Board automatically reboots into micropython waiting for REPL over USB)
3. Test via REPL
    1. Find device: `ls /dev/tty.usb*`
    2. Connect to REPL over serial: `minicom -b 11520 -o -D /dev/tty.usbmodem1421401`
    3. Test some code:

    ```python
    print("Hello world")
    # Prints text
    from machine import Pin
    led = Pin("LED", Pin.OUT)
    led.value(1)
    # LED turns on
    led.value(0)
    # LED turns off
    ```
    4. Disconnect from REPL: `<Meta-Z> Q` (opens menu, then quits)
4. Install main program to run non-interactively
    ```bash
    python3 -m venv rshell-venv
    source rshell-venv/bin/activate
    pip3 install rshell
    rshell --buffer-size=512 -p /dev/tty.usbmodem1421401
    ```
