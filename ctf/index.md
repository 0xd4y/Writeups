---
layout: post
title: "CTF Writeups"
---

###### CTF Writeups

Here are a collection of CTF writeups from various tournaments that I have participated in.

# RedPwn

## Ret2The-Unknown 

This challenge was about exploiting a binary via a return-to-libc attack (due to the enabled NX bit). The address of printf was provided to faciliate exploitation, however it was only given after passing in user input. This address could not be used for future execution of the binary due to the presence of ASLR. Nevertheless, despite the presence of the enabled NX bit and ASLR, the binary was vulnerable.

<a href="https://0xd4y.github.io/Writeups/ctf/Ret2The-Unknown%20Writeup.pdf" class="class2">Ret2The-Unknown Writeup</a>
