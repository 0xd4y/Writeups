---
layout: post
title: "HackTheBox Writeups"
---

###### HackTheBox Writeups

### Easy


## Bank

This is a really cool box that has a couple of interesting twists. I go through the unintended solution (the way I went about the machine) and the intended solution. There is a lot to learn here about web security and networking, and I highly encourage you to read this writeup.

<a href="https://0xd4y.github.io/Writeups/HackTheBox/Bank%20Writeup.pdf" class="class2">Bank Writeup</a>


## Bastion

A very realistic box with many things to learn. Misconfigurations can be a dealbreaker when it comes to a certain attack vector. There has always been a conflict between security and convenience, and this box highlights it. I go very in-depth about multiple aspects in this box relating to bastion hosts and credential databases. I hope you learn as much from this writeup as I did from this challenge!

<a href="https://0xd4y.github.io/Writeups/HackTheBox/Bastion%20Writeup.pdf" class="class2">Bastion Writeup</a>

## Love 

This Windows box dealt with exploiting an SSRF vulnerability which allowed for the viewing of a sensitive webpage hosted internally on the target. After exploting a vulnerable version of "voting system" software, a shell as a low-privileged user was returned. Finally, by taking advantage of an HKLM misconfiguration, a shell as the SYSTEM user could be obtained (namely by installing a malicious MSI package).

<a href="https://0xd4y.github.io/Writeups/HackTheBox/Love%20Writeup.pdf" class="class2">Love Writeup</a>

## Writeup

Yes, this box is called Writeup. This box did not have many open ports and even included a DoS protection script to prevent gobusters. The problem is we had to discover certain directories in order to extract essential information about the web server. Come check out my writeup for Writeup, as you will learn a lot about hashes and enumeration.

<a href="https://0xd4y.github.io/Writeups/HackTheBox/Writeup%20Writeup.pdf" class="class2">Writeup Writeup</a>

#### Medium


## Active

This was a fantastic box about the Windows Active Directory service. It showed the importance of managing your passwords in a secure way, as well as having strong passwords that are hard to crack. Something that really makes this box stand out is not so much the vulnerabilities themselves, but rather the reason why they are easily exploitable in the first place. Microsoft essentially made themselves vulnerable, as they spoke a little bit too much on THEIR OWN website! Come check out the writeup to see what I mean.

<a href="https://0xd4y.github.io/Writeups/HackTheBox/Active%20Writeup.pdf" class="class3">Active Writeup</a>
