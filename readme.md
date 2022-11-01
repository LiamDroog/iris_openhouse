Hi! This is the repo for a basic live-view image demo of the Iris Payload.

---

# How To Use:
## Gather Requisite Materials
You'll need x things:
1. Functional Iris board with Camera Modules
2. Iris Breakout Board + associated hardware
3. Power Supply [^1]
[^1]: Needs to have dual channel output for 3V3 and 5V0, but can be single channel if you have the buck'd breakout board (Ask Liam if it's not around)
4. Linux machine
5. USB-UART adapter
6. ST-LINK Programmer [^2]
[^2]: Only required if board has not been already programmed, or if you desire to change the parameters.
7. PCB holder
8. Multimeter
## Assembly:
Place Iris on the PCB holder. Plug in power supply to the breakout board (not Iris, yet.), and turn power on. Ensure you have 5V0 and 3V3 on the requisite pads.
Once power is confirmed, plug in Iris to the breakout board. Make sure the orientation of the harness is correct (red line corresponds to pin 1).
Attach USB-UART adapter to laptop and breakout board. Recall - Iris Tx -> Adapter Rx; Iris Rx -> Adapter Tx

## Running:
- Navigate to the liveview executable. Execute `sudo ./liveview` and enter your password.
- Open VSCode. Or use CLI python. Run `imgshow.py`. You will see the error screen. This is normal.
- Power on Iris. You should see initialization messages, and once it finishes, it will start continually taking images and transferring them. Images are not persistent as they are overwritten by each consecutive picture.
- Once the first image is captured, you should see the pygame screen change to match, with an ABsat logo and UofA logo at the bottom. One can focus the image by screwing the lens in or out.

That's it! It will run by itself and shouldn't encounter any issues. Highest image count was at the open house where it captured just shy of 6000 consecutive images with no interrupts. Try and break that record!

# Flashing Iris:
Download STM32CubeIDE and open the `ex2_iris_mcu_software` project. Plug in the ST-Link to both the debug header on Iris and a usb port on your computer. Hit play at the top of the screen to flash Iris with the software.
 
