#define PAD 64

/*
Hashmap: list of buckets
bucket1 -> sentinel -> node1 -> node2 -> NULL
bucket2 -> sentinel -> node3 -> NULL
...
bucketN -> sentinel -> NULL
*/

//define a node in the hashmap
typedef struct Node_HM_t
{
	long m_val; //value of the node
	char padding[PAD];
	struct Node_HM_t* m_next; //pointer to next node in the bucket
} Node_HM;

//defining a bucket in the hashmap
typedef struct List_t
{
	Node_HM* sentinel; //list of nodes in a bucket
} List;

//defining the hashmap
typedef struct hm_t
{
	List** buckets; //list of buckets in the hashmap
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
