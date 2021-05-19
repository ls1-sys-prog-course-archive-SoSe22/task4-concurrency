#include <pthread.h>
#include <unistd.h>
#include <assert.h>
#include <stdio.h>
#include "cspinlock.h"

volatile int counter;
cspinlock_t* slock;

void* work1(){
	cspin_lock(slock);
	counter++;
	sleep(1);
	assert(counter==1);
	cspin_unlock(slock);
	return NULL;
}

void* work2(){
	while(counter == 0);
	cspin_lock(slock);
	counter++;
	cspin_unlock(slock);
	return NULL;
}

int main() {
	counter = 0;
	
	slock = cspin_alloc();
	cspin_init(slock);

	pthread_t t1, t2;
	pthread_create(&t1, NULL, work1, NULL);
	pthread_create(&t2, NULL, work2, NULL);
	pthread_join(t1, NULL);
	pthread_join(t2, NULL);

	return 0;
}
