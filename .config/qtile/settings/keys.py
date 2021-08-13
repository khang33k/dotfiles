# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
   # ([mod], "j", lazy.layout.down()),
    #([mod], "k", lazy.layout.up()),
    #([mod], "h", lazy.layout.left()),
    #([mod], "l", lazy.layout.right()),
    
   ([mod], "Down", lazy.layout.down()),
   ([mod], "Up", lazy.layout.up()),
   ([mod], "Left", lazy.layout.left()),
   ([mod], "Right", lazy.layout.right()),


    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),
([mod], "f", lazy.window.toggle_fullscreen()),
    # Move windows up or down in current stack
    ([mod, "shift"], "Left", lazy.layout.shuffle_down()),
    ([mod, "shift"], "Right", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "c", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "shift"], "r", lazy.restart()),

    ([mod, "shift"], "e", lazy.spawn("dm-logout")),
    ([mod, "control"], "q", lazy.shutdown()),
   # ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "d", lazy.spawn("rofi -modi drun -show drun -display-drun 'Apps : ' -line-padding 4 -columns 2 -padding 50 -hide-scrollbar -show-icons -drun-icon-theme 'Paper-Mono-Dark' -font 'UbuntuMono Nerd Font Regular 14'")),
     ([mod, "shift"], "d", lazy.spawn("dmenu_run")),
    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),
    ([mod, "shift"], "b", lazy.spawn("firefox --private-window")),

    # File Explorer
    ([mod], "n", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),
    ([mod], "h", lazy.spawn("alacritty -e 'htop'")),


    # Redshift
    #([mod], "r", lazy.spawn("redshift -O 2400")),
    #([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    #([mod, "shift"], "s", lazy.spawn("scrot")),
([mod, "control"], "l", lazy.spawn("light-locker-command -l")),

([mod, "control"], "w", lazy.spawn("dm-record")),
([mod, "control", "shift"], "p", lazy.spawn("passmenu")),

    # ------------ Hardware Configs ------------

    # Volume
   # ([], "XF86AudioLowerVolume", lazy.spawn(
    #    "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    #)),
    #([], "XF86AudioRaiseVolume", lazy.spawn(
     #   "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    #)),
    #([], "XF86AudioMute", lazy.spawn(
     #   "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    #)),
    ([mod, "control"], "p", lazy.spawn("alacritty -e 'alsamixer'")),
    ([mod, "shift"], "p", lazy.spawn("pavucontrol")),
   # Brightness
    #([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    #([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
]]
