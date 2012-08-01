

avrdude -p atmega328p -b 115200 -c stk500v2 \
-e -U flash:w:$1 -P usb \
-U lfuse:w:0xff:m -U hfuse:w:0xda:m -U efuse:w:0x05:m
