# Kalman Filter
This filter was built as part of our ECE 4250 Digital Signal and Image Processing final project in Spring 2017.

# Authors
Brian Bigdelle bb586, Eric Johnson edj36

# Installation
In order to run the code, you will need the following:
- python 3.5
    - we use [Anaconda](https://www.continuum.io/downloads)
- matplotlib library
    - `pip install matplotlib`
- tkinter library
    - `pip install tkinter`
- pandas library
    - `pip install pandas`
- numpy libary
    - `pip install numpy`
- clone or download this repository

# Usage
Once those are installed and you have downloaded/cloned this repo, make sure gui.py and kalman.py are in the same directory. Then in a terminal, cd to that directory, and run the system with `python gui.py`

A GUI will appear. Select a stock and date range and then press "Process". The graph will update to show the actual stock price over that range of dates (in blue) and the output of the Kalman filter also over the selected range of dates (in orange).

## Notes
We did not implement robust date verification in the GUI, so if you try and filter a stock price on a day that does not exist (e.g. Feb 31st), you will get an error.

You can change the configuration of the Kalman filter in `kalman.py` to see how different parameters have an effect on the behavior of the filter.