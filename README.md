# light
Light control via raspberry pi

edit crontab with

sudo crontab -e

and add this line in the bottom of the file

@reboot sh /home/pi/launcher.sh
