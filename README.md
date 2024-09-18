# BootTimePilot

Shows Windows 10 boot time and time to shutdown.<br>
These times can be loacated manually via ... -> ... -> ...<br>
This scrpt uses exported Event xml files to grab the appropriate informations:<br>
For startup times: ID100 -> MainPathBootTime and BootPostBootTime in milli seconds. The sum of both values can be read from BootTime<br>
For shutdown times: ID200 -> ShutdownTime in milli seconds.
