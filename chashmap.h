#include<stdio.h>

#define PAD 64

#define mark(A) ((unsigned long)(A) + 1)
#define marked(A) ({((unsigned long)(A)) % 2 != 0; })
#define unmark(A) ((unsigned long)(A) - 1)

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

static void print_hashmap(HM* hm){
  for (int i = 0; i < hm->n_buckets; i++) {
    printf("Bucket %d ", i);
    Node_HM* iter = hm->buckets[i]->sentinel;
    while(1){
			if(iter == NULL)
				break;
			else if(marked(iter->m_next)){
        Node_HM *next = (Node_HM *)unmark(iter->m_next);
        iter = next;
      }
      else{
				printf(" - %ld ", iter->m_val);
				iter = iter->m_next;
			}
    }
    printf("\n");
  }
}

HM* create_hashmap(int n_buckets);
int insert_item(HM* hm, long val);
int remove_item(HM* hm, long val);
int lookup_item(HM* hm, long val);
