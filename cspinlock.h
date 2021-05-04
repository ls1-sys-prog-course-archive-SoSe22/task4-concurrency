typedef volatile int cspinlock;

int cspin_lock(cspinlock* slock);

int cspin_unlock(cspinlock* slock);

int cspin_init(cspinlock* slock);
