struct cspinlock;

//acquire the lock
int cspin_lock(struct cspinlock* slock);

//if the lock can not be acquired, return immediately
int cspin_trylock(struct cspinlock* slock);

//release the lock
int cspin_unlock(struct cspinlock* slock);

//initialize the lock
int cspin_init(struct cspinlock* slock);
