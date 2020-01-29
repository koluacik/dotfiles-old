output_dir="$HOME/dotfiles/scripts/.screenshot_command.txt"
#TODO: tidy up this part
rofi="rofi -dmenu -location 2 -width 100 -line-margin 1 -line-padding 1 -yoffset 27"
area=("both screens" "left screen" "right screen" "select area" "active window")
action=(save clipboard)

s_area=$(for i in ${!area[*]}; do echo ${area[$i]}; done | $rofi -lines ${#area[*]})

s_action=$(for j in ${!action[*]}; do echo ${action[$j]}; done| $rofi -lines ${#action[*]})
case $s_area in
	"both screens")
		mycommand="maim"
		;;
	"left screen")
		mycommand="maim -g 1920x1080+0+0"
		;;
	"right screen")
		mycommand="maim -g 1920x1080+1920+0"
		;;
	"select area")
		mycommand="maim -s"
		;;
	"active window")
		mycommand='maim -i $(xdotool getactivewindow)'
		;;
	esac

case $s_action in
	save)
		save='~/Documents/Pictures/screenshots/$(date +%Y%m%d-%H%M%S).png'
		#save="~/Documents/Pictures/screenshots/ff.png"
		;;
	clipboard)
		save="| xclip -selection clipboard -t image/png"
		;;
	esac

final="$mycommand $save"

#avoid overriding the existing command with an empty one if you press ESC.
if [[ $mycommand == ""  ||  $save == "" ]]
then
	exit
else
	echo $final > $output_dir
fi

