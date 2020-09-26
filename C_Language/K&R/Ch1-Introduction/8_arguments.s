	.file	"8_arguments.c"
	.text
	.section	.rodata
.LC0:
	.string	"%s"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$2032, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movl	$0, -2024(%rbp)
	jmp	.L2
.L4:
	movl	-2020(%rbp), %eax
	cmpl	-2024(%rbp), %eax
	jle	.L3
	movl	-2020(%rbp), %eax
	movl	%eax, -2024(%rbp)
	leaq	-2016(%rbp), %rdx
	leaq	-1008(%rbp), %rax
	movq	%rdx, %rsi
	movq	%rax, %rdi
	call	copy
.L3:
	cmpl	$0, -2024(%rbp)
	jle	.L2
	leaq	-1008(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
.L2:
	leaq	-2016(%rbp), %rax
	movl	$1000, %esi
	movq	%rax, %rdi
	call	get_line
	movl	%eax, -2020(%rbp)
	cmpl	$0, -2020(%rbp)
	jg	.L4
	movl	$0, %eax
	movq	-8(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L6
	call	__stack_chk_fail@PLT
.L6:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.globl	get_line
	.type	get_line, @function
get_line:
.LFB1:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%rdi, -24(%rbp)
	movl	%esi, -28(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L8
.L10:
	movl	-4(%rbp), %eax
	movslq	%eax, %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movl	-8(%rbp), %edx
	movb	%dl, (%rax)
	addl	$1, -4(%rbp)
.L8:
	movl	-28(%rbp), %eax
	subl	$1, %eax
	cmpl	%eax, -4(%rbp)
	jge	.L9
	call	getchar@PLT
	movl	%eax, -8(%rbp)
	cmpl	$-1, -8(%rbp)
	je	.L9
	cmpl	$110, -8(%rbp)
	jne	.L10
.L9:
	cmpl	$10, -8(%rbp)
	jne	.L11
	movl	-4(%rbp), %eax
	movslq	%eax, %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movl	-8(%rbp), %edx
	movb	%dl, (%rax)
	addl	$1, -4(%rbp)
.L11:
	movl	-4(%rbp), %eax
	movslq	%eax, %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movb	$0, (%rax)
	movl	-4(%rbp), %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	get_line, .-get_line
	.globl	copy
	.type	copy, @function
copy:
.LFB2:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movq	%rsi, -32(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L14
.L15:
	addl	$1, -4(%rbp)
.L14:
	movl	-4(%rbp), %eax
	movslq	%eax, %rdx
	movq	-32(%rbp), %rax
	addq	%rax, %rdx
	movl	-4(%rbp), %eax
	movslq	%eax, %rcx
	movq	-24(%rbp), %rax
	addq	%rcx, %rax
	movzbl	(%rdx), %edx
	movb	%dl, (%rax)
	movzbl	(%rax), %eax
	testb	%al, %al
	jne	.L15
	nop
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	copy, .-copy
	.ident	"GCC: (Ubuntu 9.3.0-10ubuntu2) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
