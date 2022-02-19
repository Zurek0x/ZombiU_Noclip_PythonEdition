alloc(newmem,2048)
label(returnhere)
label(originalcode)
label(exit)

newmem:
// NONE: Do not write external addresses

originalcode:
//mov [ecx+38],eax
mov eax,[edx+3C]

exit:
jmp returnhere

"ZOMBI.exe"+B5B23:
jmp newmem
nop
returnhere: