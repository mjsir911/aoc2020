.set READ, 0
.set STDIN, 0
.set SYS_EXIT, 60

.section .text

.globl _start

_start:
	# https://www.officedaytime.com/simd512e/ is a very useful resource if the
	# instructions apply to me
	# not many byte level instructions 
	# perhaps interleave the two ids in each word would work

	vpcmpeqd        %ymm15, %ymm15, %ymm15 # a bunch o' ones

	mov $STDIN, %edi
	mov $33, %edx
	mov %rsp, %rsi # rsp is scratchpad / stack
loop:
	mov $READ, %eax
	syscall

	cmp $0, %rax
	je exit

	vpxor (%rsi), %ymm15, %ymm0 # this is a mov with a negation built in
	# add $33, %rsp
	# vmovdqa (%rsp), %ymm0

	# XOR the stack with FBLRMask repeated over and over again
	# these next two are unneccessary but make debugging easier
	# vpbroadcastb FBLRMask, %ymm1 
	# vpand %ymm0, %ymm1, %ymm0

	# bit shift the xord bits over a few times to sthat bit is highest of the byte
	# https://www.officedaytime.com/simd512e/simdimg/shift.php?f=psllw
	vpsllw $5, %ymm0, %ymm0
	# vpsrlw $2, %ymm0, %ymm0

	# PMOVMSKB is wrong endian which is why we do this stuff

	# byte shift over PSHUFB middle boundary
	vperm2i128 $0b00100001, %ymm0, %ymm0, %ymm1
	vpalignr $16-5, %ymm1, %ymm0, %ymm0

	# %ymm0 now has line 1 & 2 in the correct qwords
	# %xmm1 also has line 3 on the (needs to be shifted by 1 for newline)

	# use PSHUFB for endian correcting
	# also remove newlines and pad out correctly
	vpshufb endianShuf, %ymm0, %ymm0


	# PMOVMSKB to extract 32 bytes to register
	vpmovmskb %ymm0, %r9
	mov %r9, (%rsi)

	# also deal with line 3 on lower qword of %ymm0
	# do the same for the third line in %xmm0
	psrldq $1, %xmm1
	pshufb endianShuf, %xmm1
	pmovmskb %xmm1, %r10
	mov %r10, 4(%rsi)

	add $6, %rsi

	jmp loop

exit:
	mov $SYS_EXIT, %eax
	mov $-1, %rdi
	syscall

.section .data
	.balign 32
	endianShuf: 
		.byte 0xE, 0xD, 0xC, 0xB, 0xA, 0x9, 0x8, 0x7, 0x6, 0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF
		.byte 0x9, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2, 0x1, 0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF 
