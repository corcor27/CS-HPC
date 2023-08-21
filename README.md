# CS-HPC



# Anaconda
To start using the HPC cluster, you will likely have some required dependencies. Therefore its inportant that you set up your conda enviorment. 

1) intiate the shell: to do this type the following; "anaconda3-launch conda init" you will now need to close the shell and reconect to the server. You will know it work when you log back in and you see the following: (base) cot13@slurm etc. where you wont have the (base)) before
2) You should never use your base enviroment going forward, as if theres a problem it will affect all your other enviroments. So now you need to create a new enviroment, to which you need to entre the following: "conda create --name AI_SUM python==3.9" please edit AI_SUM to the name of your enviroment.
3) activate this new enviroment with "conda activate AI_SUM"
4) 

