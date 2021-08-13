-- http://projects.haskell.org/xmobar/

Config { 
    font = "xft:UbuntuMono Nerd Font:weight=bold:pixelsize=18:antialias=true:hinting=true",
    bgColor = "#292d3e",
    fgColor = "#10b356",
    lowerOnStart = True,
    hideOnStart = False,
    allDesktops = True,
    persistent = True,
    commands = [ 
        Run Date "  %d %b %Y %H:%M " "date" 600,
        Run Memory ["-t", "  <used>M (<usedratio>%)"] 150,
        Run Com "volume" [] "volume" 10,
        Run Com "battery" [] "battery" 600,
        Run Com "brightness" [] "brightness" 10,
        Run Com "bash" ["-c", "checkupdates | wc -l"] "updates" 3000,
        Run Com "/home/v3n0m/.config/xmobar/trayer-padding-icon.sh" [] "trayerpad" 600,
        Run UnsafeStdinReader
    ],
    alignSep = "}{",
    template = "<fc=#d9e62e>  </fc>%UnsafeStdinReader% }{ \
        \<fc=#0bbf29> %updates% </fc>\
        \<fc=#1667f2> %brightness%</fc>\
        \<fc=#0bbf29> %memory% </fc>\
        \<fc=#1667f2> %battery%</fc>\
        \<fc=#0bbf29> %volume%</fc>\
        \<fc=#1667f2> %date% </fc>\
        \%trayerpad%"
}
