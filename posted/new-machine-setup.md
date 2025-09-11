I got a new PC!
Well, it's not new. In fact, it's nine years old. 
But it still runs well. Lenovo/IBM knew a thing about building PCs back then.

It came with no operating system, so I naturally installed Fedora onto it. 
This is a very slick process now, certainly for older machines. 

Then it came to set up the machine. Because I have so many PCs, I need to synchronise data between them.
For my money, the synchronisation tool _par excellence_ is git. Cloud drives, constantly synchronising to local disks,
have their place, but even now we sometimes want to use a PC without the potential for interruption. 
Git handles this sort of asynchronous updating wonderfully.
I cannot pretend that the learning curve is gentle, but it really isn't too bad, 
especially with an AI agent to give you a few hints.

The basic operation I use is as follows: 

1. I do git init in an existing directory to create the repo,

1. I create an empty repo on bitbucket or github to allow remote synchronisation,

1. I sync my local changes to the remote with `git remote add` (github has instructions on how to do this).

1. I can use git to record my changes locally by doing `git add .`, `git commit`. 

1. When I want to send my changes to the remote repo, I do a `git push`,

1. When I want to start working on the same project on a new machine, I do a `git clone` (following the guidance on github etc.),

1. When I want to update a local project directory I haven't touched for a bit, I do a `git pull`. Sometimes, I have to merge the changes, but git usually (sort of) guides me through this. I don't bother with the complicated protocol of merging other people's work with mine, 
since I have nobody to collaborate with (sob).

The above is not meant to be a tutorial on how to use git. It's just a vague outline of how git can be used to synchronise files between machines. This is being written in my 'blog ideas' project, and once I've finished this draft, I'll `add` it, `commit` it and `push` it.
The point of writing it is to communicate the idea that git is not some arcane piece of software which takes years to learn and is only of use to Linux kernel developers with brains the size of several planets. Mere mortals like me can use it for mundane text management purposes. Yes, it is over the top for this purpose. No, it's not unusably excessive, and it works well with LaTex (a good substitute for Word), and with any text-based files. And it's free (FOSS) and pre-installed on any flavour of Linux you can imagine.

I very rarely need to resolve conflicts in one file, because I tend to keep my projects in directories with lots of smallish files that don't need to get edited (but not committed) over multiple machines.

I will make some further posts discussing how else I have set up my new old PC to be useful for practical, non-programming, tasks using Fedora Linux.

