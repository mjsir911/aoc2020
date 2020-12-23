#include <stdio.h>
#include <stdlib.h>

struct link {
	struct link *next;
	int data;
};

int modulo(int x,int N){
    return (x % N + N) %N;
}


#define NCUPS 1000000

#define lenof(a) sizeof(a) / sizeof(a[0])
int main(int argc, char *argv[]) {
	int input[] = {5, 6, 2, 8, 9, 3, 1, 4, 7};
	static struct link cups[NCUPS];
	#define rinput(i) ((i) < lenof(input) ? input[i] - 1 : i)
	for (int i = 0; i < NCUPS; i++) {
			cups[rinput(i)] = (struct link) { .data = rinput(i) + 1
			                                , .next = cups + rinput((i + 1) % NCUPS) };
	}

	struct link *cur = &cups[input[0] - 1];
	for (int i = 0; i < 10000000; i++) {
		int current = cur->data;
		// printf("cups: "); print_circ_list(*cups);
		// printf("current: %i\n", current);
		struct link *removed = cur->next; // three long
		// printf("pick up: %i, %i, %i\n", removed->data, removed->next->data, removed->next->next->data);
		cur->next = removed->next->next->next;
		cur = cur->next;

		int dest = current;
		do {
			dest = modulo(dest - 1, NCUPS + 1);
			if (dest == 0) {
				dest = modulo(dest - 1, NCUPS + 1);
			}
		} while (
				 dest == removed->data
			|| dest == removed->next->data
			|| dest == removed->next->next->data
		);
		// printf("dest: %i\n", dest);
		struct link *dest_p = &cups[dest - 1];

		// do the move
		removed->next->next->next = dest_p->next;
		dest_p->next = removed;
	}
	printf("%li\n", (long int) cups[0].next->data * cups[0].next->next->data);
}
