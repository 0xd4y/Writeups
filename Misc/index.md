---
layout: post
title: "Miscellaneous Writeups"
---

###### Misc

All writeups not related to TryHackMe or HackTheBox are posted on this page. 

# OverTheWire

<a href="https://overthewire.org/wargames/">OverTheWire</a> is a website that contains many different wargames ranging from learning Unix, binary exploitation, scripting, along with many other fun and instructional challenges.

## Narnia

This challenge was about binary exploitation. There were a total of nine binaries which increased in difficulty after each exploit. Common binary exploitation techniques are discussed in this report including ret2libc, shellcode injection, format string exploitation, among others. 

<a href="https://0xd4y.github.io/Writeups/Misc/Narnia%20Writeup.pdf">Narnia Writeup</a>

## Behemoth

Behemoth is the sequel to Narnia and is rated to be slightly harder. In comparison to Narnia, it involved more reverse engineering exercises and required more knowledge of C. Each binary contained a different vulnerability ranging from PATH environment variable privilege escalation to buffer overflows, format string exploits, and bypassing shellcode filtering.

<a href="https://0xd4y.github.io/Writeups/Misc/Behemoth%20Writeup.pdf">Behemoth Writeup</a>

# Pwnable.kr

<a href="http://pwnable.kr/">Pwnable.kr</a> is a website dedicated to providing reverse engineering and binary exploitation challenges at varying difficulties.

## Passcode

scanf() is a function that is widely used in C programs. This binary, which is seemingly secure, made subtle but dangerous programming mistakes that resulted in a security hole in which a user can manipulate memory. Since this binary was dynamically linked, overwriting the GOT entry subsequently forces the program to jump to memory of the attacker's choice.

<a href="https://0xd4y.github.io/Writeups/Misc/Passcode%20Writeup.pdf">Passcode Writeup</a>
