# Timer
I'm always between the course-works and the research. I felt I need a simple timer to keep track of the times that I'm working on my research, cause I want to spend at least 160 hours by the end of the summer. So, I created this simple timer. I hope it's helpful.

# Installation 
Just edit the bashrc.sh file and change my dir to where you have downloaded this bashrc. Then you should source this bashrc file in your actuall bashrc file. For instance, lets say that you download the code to "/home/timer". then you should change the bashrc.sh file here as : 
```
	function timer(){
		python "/home/timer/timer.py" "$1"
	}	
```

And then in your actuall bashrc file add:
```
	source /home/timer/bashrc.sh
```
