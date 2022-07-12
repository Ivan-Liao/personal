#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^Esc::ExitApp
return


::eap:: ivanhliao@gmail.com
::eaw:: ivan.liao@xselltechnologies.com
::paw:: <YOUR_PWD>


#X::
FormatTime, xx,, yyyy-MM-dd
SendInput, %xx%
return


^!+1::
MouseGetPos, xpos, ypos
clipboard := ypos
Sleep, 250
clipboard := xpos
MsgBox, The cursor is at X: %xpos% Y: %ypos%
return


