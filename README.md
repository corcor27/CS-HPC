# CS-HPC

#git hub

To download and add this repositry to the server entre: "git clone https://github.com/corcor27/CS-HPC.git"
Note: if you want to edit your files on the system then to view you need to use nano. e.g. I want to view my file called test.py so I would enter "nano test.py". to save use control x and then s

# Anaconda
To start using the HPC cluster, you will likely have some required dependencies. Therefore its inportant that you set up your conda enviorment. 

1) intiate the shell: to do this type the following; "anaconda3-launch conda init" you will now need to close the shell and reconect to the server. You will know it work when you log back in and you see the following: (base) cot13@slurm etc. where you wont have the (base) before
2) You should never use your base enviroment going forward, as if theres a problem it will affect all your other enviroments. So now you need to create a new enviroment, to which you need to entre the following: "conda create --name AI_SUM python==3.9" please edit AI_SUM to the name of your enviroment.
3) activate this new enviroment with "conda activate AI_SUM" You should see that the (base) now changes to (AI_SUM)
4) You are ready to install your packages, to which you will want to use "conda install package" or "pip install package". Go through and install everything you believe you will need.

# Running a job

1) So start to submitting a job, you are going to need a batch file. Assuming that you cloned this repositry "run-aber.sh" is your batch file.
2) Now we need to find you a partition to run on, to see all nodes entre: "scontrol show nodes".
3) Once you have selected a partition you will want to change the line in your batch file which specifies what node you want: "#SBATCH -p cpusmall" change the cpusmall part.
4) Also change the email user name, such that you get notified whenever your job has finished. Also change the name of your conda enviorment. 
5) To submitted your job you want to entre the following: "sbatch run-ABER.sh" for example.

