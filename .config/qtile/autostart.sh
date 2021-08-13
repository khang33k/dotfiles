#!/bin/sh

# systray battery icon
#cbatticon -u 5 &
# systray volume
volumeicon &
picom &
nitrogen --restore &
nm-applet &
xfce4-power-manager & 
light-locker &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

