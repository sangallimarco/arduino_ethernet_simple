Arduino Ethernet Board telnet protocol

A=pin0
B=pin1
C=...

Syntax:
"#[\<\>\~\|]{1}[A-Z]{1}\n"

Examples of Commands:
#>C1\n
set pin 2 to out mode and set it to high

#<E\n
set pin 4 as input and read digital value
		
#~A\n
read analog input 0 and return value 

#|mymessage\n
sends to serial TX message 

