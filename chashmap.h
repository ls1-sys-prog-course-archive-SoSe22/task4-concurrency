#include<stdio.h>

#define PAD 64

typedef struct Node_HM_t
{
	long m_val;
	char padding[PAD];
	struct Node_HM_t* m_next;
} Node_HM;

typedef struct List_t
{
	volatile int lock;
	Node_HM* sentinel;
} List;

typedef struct hm_t
{
	int n_buckets;
	List** buckets;
} HM;


//initialize the hashamp with given number of buckets
HM* create_hashmap(int n_buckets);

//insert val into the hm and return 0 if successful
int insert_item(HM* hm, long val);

//remove val from the hm, if it exist and return 0 if successful
int remove_item(HM* hm, long val);

//check if val exists in hm, return 0 if found
int lookup_item(HM* hm, long val);

//print all elements in the hashmap as follows:
//Bucket 1 - val1 - val2 - val3 ...
//Bucket 2 - val4 - val5 - val6 ...
//Bucket N -  ...
void print_hashmap(HM* hm);
