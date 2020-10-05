<h1>IDS on Wireless Sensor Network</h1>
<p>This IDS detects Blackhole Attack on a sensor network.The developed IDS anomaly based IDS that uses ML Algorithm to detect black hole attack.An anomaly based IDS detects attack based on anomalies in data from the sensor nodes</p>
<p>Network is setup on Cooja Simulator in Contiki OS a lightweight operating system for IOT which can be downloaded from <a href="https://sourceforge.net/projects/contiki/files/Instant%20Contiki/" target="_blank">Contiki</a></p>
<h3>File Structure</h3>
<ol>
<li><b><u>Data-Generator<u></b>: This folder consist of program that generate csv data file which is given as input to ML Program.The program ping's the network 200 times every 5 seconds.</li> <br> 
<li><b><u>Data</u></b>:It consist of data collected through Data-Generator program</li> <br> 
<li><b><u>Simulations:</u></b>It consists of cooja simulation files</li> <br> 
<li><b><u>Firmware:</u></b>Firmware files of sky mote sensor</li> <br> 
</ol>
<h4>For running data generator program python 3.7 is required which can be only installed from the source</h4>
<h5>It should be installed in the contiki os vm</h5>  
<h5><a href="https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/">Python installation instructions</a></h5>  
