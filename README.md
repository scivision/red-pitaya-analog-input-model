# red-pitaya-analog-input-model
Red Pitaya analog input SPICE model (GNUcap/ngSPICE compatible)

DC coupling can become a problem when intending to use Red Pitaya for RF with non-DC-shorted antennas.
Here is a model for the analog input filtering of the Red Pitaya for LV and HV positions.

* f > 100 kHz, HV has 26 dB less gain than LV.
* f < 1 kHz, HF has 15 dB less gain than LV.

![Red Pitaya Analog Input transfer function](https://cdn.rawgit.com/scivision/red-pitaya-analog-input-model/master/transfer_fcn.svg)
*Red Pitaya Analog Input transfer function*

## Run Simulation

    gnucap -b LV.net

## Plot Simulation output

    ./PlotTransfer.py

## References

* [Red Pitaya Analog Input schematic](https://wiki.redpitaya.com/tmp/Fast_analog_inputs_sch.png)
* [measured Red Pitaya LV transfer function](https://forum.redpitaya.com/viewtopic.php?f=9&t=468)
