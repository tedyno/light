# light
Light control via raspberry pi
1. make launcher.sh executable with `sudo chmod 775 launcher.sh`
2. edit crontab with
`sudo crontab -e`
and add this line in the bottom of the file

`@reboot sh /home/pi/launcher.sh`
