#include <stdio.h>
#include <stdlib.h>

struct link {
	struct link *next;
	int data;
};

typedef struct {
	size_t size;
	struct link *list;
	struct link **lookup; // this is a big array of lookup[data] -> link
} circ_list;

circ_list new_circ_list(vals, len)
	size_t len;
	int vals[len];
{
	circ_list r = {
		.size = len,
		.list=malloc(sizeof(struct link)),
		.lookup=calloc(r.size + 1, sizeof(struct link*))
	};
	struct link *head = r.list;

	head->data = vals[0];
	r.lookup[vals[0]] = head;
	struct link *prev = head;
	for (int i = 1; i < len; i++) {
		struct link *node = malloc(sizeof(struct link));
		node->data = vals[i];
		r.lookup[vals[i]] = node;
		prev->next = node;
		prev = node;
	}
	prev->next = head;

	return r;
}

void print_circ_list(circ_list cups) {
	struct link *next = cups.list;
	printf("{");
	for (int i = 0; i < cups.size; i++) {
		printf("%i, ", next->data);
		next = next->next;
	}
	printf("}\n");
}

int modulo(int x,int N){
    return (x % N + N) %N;
}

circ_list *move(circ_list *cups) {
	int current = cups->list->data;
	// printf("cups: "); print_circ_list(*cups);
	// printf("current: %i\n", current);
	struct link *removed = cups->list->next; // three long
	// printf("pick up: %i, %i, %i\n", removed->data, removed->next->data, removed->next->next->data);
	cups->list->next = removed->next->next->next;
	cups->list = cups->list->next;

	int dest = current;
	do {
		dest = modulo(dest - 1, cups->size + 1);
		if (dest == 0) {
			dest = modulo(dest - 1, cups->size + 1);
		}
	} while (
		   dest == removed->data
		|| dest == removed->next->data
		|| dest == removed->next->next->data
	);
	// printf("dest: %i\n", dest);
	struct link *dest_p = cups->lookup[dest];

	// do the move
	removed->next->next->next = dest_p->next;
	dest_p->next = removed;
	return cups;
}

#define lenof(a) sizeof(a) / sizeof(a[0])
int main(int argc, char *argv[]) {
	int input[1000000] = {5, 6, 2, 8, 9, 3, 1, 4, 7};
	for (int i=9; i < 1000000; i++) {
		input[i] = i + 1;
	}
	circ_list list = new_circ_list(input, lenof(input));
	for (int i = 0; i < 10000000; i++) {
		move(&list);
	}
	printf("%li\n", (long int) list.lookup[1]->next->data * list.lookup[1]->next->next->data);
}
