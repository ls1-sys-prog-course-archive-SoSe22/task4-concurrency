typedef volatile int cspinlock;

//acquire the lock
int cspin_lock(cspinlock* slock);

//release the lock
int cspin_unlock(cspinlock* slock);

//initialize the lock
int cspin_init(cspinlock* slock);
