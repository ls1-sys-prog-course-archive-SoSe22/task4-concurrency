PYTHON3 ?= python3
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

check: ${ROOT_DIR}/test_mutual_exclusion ${ROOT_DIR}/lock_hashmap \
	${ROOT_DIR}/lockfree_hashmap
	$(PYTHON3) ${ROOT_DIR}/test_mutual_exclusion.py
	$(PYTHON3) ${ROOT_DIR}/test_lockhashmap.py
	$(PYTHON3) ${ROOT_DIR}/test_lockfreehashmap.py

${ROOT_DIR}/test_mutual_exclusion: ${ROOT_DIR}/test_mutual_exclusion.c
	gcc -I ${ROOT_DIR}/.. -Og -g -pthread -o $@ $< -L ${ROOT_DIR}/../ -lcspinlock

clean:
	rm *.o test_mutual_exclusion lock_hashmap


PROG1 := ${ROOT_DIR}/lock_hashmap
PROG2 := ${ROOT_DIR}/lockfree_hashmap


SRCS += \
	${ROOT_DIR}/hashmap-driver.c \
	${ROOT_DIR}/thread.c

CC       := gcc
CFLAGS   += -g -w -pthread -fpermissive
CFLAGS   += -O2
HEADERS  := ${ROOT_DIR}/../
CFLAGS   += -I$(HEADERS)
CPP      := g++
CPPFLAGS += $(CFLAGS)
LD       := gcc
LIBS1     += -lpthread -L ${ROOT_DIR}/../ -llockhashmap
LIBS2     += -lpthread -L ${ROOT_DIR}/../ -llockfreehashmap

#
OBJS := ${SRCS:.c=.o}

%.o: %.c *.h
	$(CC) $(CFLAGS) -c $< -o $@

$(PROG1): $(OBJS)
	$(LD) $(LDFLAGS) $^ $(LIBS1) -o $(PROG1)

$(PROG2): $(OBJS)
	$(LD) $(LDFLAGS) $^ $(LIBS2) -o $(PROG2)
