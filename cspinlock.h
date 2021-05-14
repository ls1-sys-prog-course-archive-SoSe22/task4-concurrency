typedef struct cspinlock{
	//define your locking structure here
} cspinlock_t;

//acquire the lock
extern int cspin_lock(cspinlock_t *slock);

//if the lock can not be acquired, return immediately
extern int cspin_trylock(cspinlock_t *slock);

//release the lock
extern int cspin_unlock(cspinlock_t *slock);

//initialize the lock
extern int cspin_init(cspinlock_t *slock);
