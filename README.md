# Generic task template

1. Edit Makefile to include the build command used for your language
2. For building run 
   ```console
   $ make all
   ```
3. For running the tests run:
   ```console
   $ make check
   ```

## The assignment for this week
This week you will implement a simple locking construct by relying only on primitive atomic operations. You will also implement a thread-safe concurrent data-structure while ensuring its scalability. This will be achieved by following two different paths:
1. using locks
2. using a lock-free algorithm.

### Deliverables
1. Implement the spinlock that is declared in `cspinlock.h` to generate a library called `libcspinlock.so`
2. Implement a lock-based hashmap datastructure that is declared in `chashmap.h` to generate a library called `liblockhashmap.so`
3. Implement a lock-free hashmap datastructure that is declared in `chashmap.h` to generate a library called `liblockfreehashmap.so`

## Going further
1. If you want to further develop your concurrent programming skills you can check other synchronization techniques such as Read-Copy-Update (RCU) and figure out how can the hashmap use RCU. 
2. Another direction that is important for lock-free programming is memory reclamation. You can try to understand how to safely reclaim deleted nodes from the hashmap.
 
