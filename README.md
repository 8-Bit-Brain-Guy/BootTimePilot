# BootTimePilot

Shows Windows 10 boot time and time to shutdown.
These times can be loacated manually via ... -> ... -> ...
This scrpt uses exported Event xml files to grab the appropriate informations: 
For startup times: ID100 -> MainPathBootTime and BootPostBootTime in milli seconds. The sum of both values can be read from BootTime
For shutdown times: ID200 -> ShutdownTime in milli seconds.
