#include<stdio.h>
#include<pthread.h>
#include<sys/types.h>
 
pthread_mutex_t work_mutex[5];
 
void *philosopher1()
{
	while(1)
	{
		pthread_mutex_lock(&work_mutex[4]);
		pthread_mutex_lock(&work_mutex[0]);
		printf("\nphilosopher 1 is eating");
		sleep(2);
		pthread_mutex_unlock(&work_mutex[4]);
		pthread_mutex_unlock(&work_mutex[0]);
		printf("\nphilosopher 1 is releasing the spoon");
		printf("\nphilosopher 1 is thinking");
		sleep(3);
	}
	pthread_exit(0);
}
 
void *philosopher2()
{
	while(1)
	{
		pthread_mutex_lock(&work_mutex[0]);
		pthread_mutex_lock(&work_mutex[1]);
		printf("\nphilosopher 2 is eating");
		sleep(3);
		pthread_mutex_unlock(&work_mutex[0]);
		pthread_mutex_unlock(&work_mutex[1]);
		printf("\nphilosopher 2 is releasing the spoon");
		printf("\nphilosopher 2 is thinking");
		sleep(2);
	}
	pthread_exit(0);
}
 
void *philosopher3()
{
	while(1)
	{
		pthread_mutex_lock(&work_mutex[1]);
		pthread_mutex_lock(&work_mutex[2]);
		printf("\nphilosopher 3 is eating");
		sleep(2);
		pthread_mutex_unlock(&work_mutex[1]);
		pthread_mutex_unlock(&work_mutex[2]);
		printf("\nphilosopher 3 is releasing the spoon");
		printf("\nphilosopher 3 is thinking");
		sleep(3);
	}
	pthread_exit(0);
}
 
void *philosopher4()
{
	while(1)
	{
		pthread_mutex_lock(&work_mutex[2]);
		pthread_mutex_lock(&work_mutex[3]);
		printf("\nphilosopher 4 is eating");
		sleep(3);
		pthread_mutex_unlock(&work_mutex[2]);
		pthread_mutex_unlock(&work_mutex[3]);
		printf("\nphilosopher 4 is releasing the spoon");
		printf("\nphilosopher 4 is thinking");
		sleep(2);
	}
	pthread_exit(0);
}
 
void *philosopher5()
{
	while(1)
	{
		pthread_mutex_lock(&work_mutex[3]);
		pthread_mutex_lock(&work_mutex[4]);
		printf("\nphilosopher 5 is eating");
		sleep(2);
		pthread_mutex_unlock(&work_mutex[3]);
		pthread_mutex_unlock(&work_mutex[4]);
		printf("\nphilosopher 5 is releasing the spoon");
		printf("\nphilosopher 5 is thinking");
		sleep(3);
	}
	pthread_exit(0);
}
 
main()
{
	int res,i;
	pthread_t ph1,ph2,ph3,ph4,ph5;
	 
	 
	 
	for(i=0;i<5;i++)
	{
		res=pthread_mutex_init(&work_mutex[i],NULL);
		//The pthread_mutex_init() function initialises the mutex referenced by mutex with attributes specified by attr. 
		//If attr is NULL, the default mutex attributes are used
		if(res!=0)
		printf("\nmutex not intilize");
	}
	 
	pthread_create(&ph1,NULL,philosopher1,NULL);
	pthread_create(&ph2,NULL,philosopher2,NULL);
	pthread_create(&ph3,NULL,philosopher3,NULL);
	pthread_create(&ph4,NULL,philosopher4,NULL);
	pthread_create(&ph5,NULL,philosopher5,NULL);
	 
	//The pthread_create() function starts a new thread in the calling
	// process.  The new thread starts execution by invoking
	// start_routine()
	 
	printf("\nthreads joing mutex");
	 
	pthread_join(ph1,NULL); //pthread_join - join with a terminated thread
	pthread_join(ph2,NULL);
	pthread_join(ph3,NULL);
	pthread_join(ph4,NULL);
	pthread_join(ph5,NULL);
 
}