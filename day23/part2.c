#include <stdio.h>
#include <stdlib.h>

typedef struct cup {
	struct cup *next;
	int data;
} cup;

#define NCUPS 1000000

#define lenof(a) sizeof(a) / sizeof(a[0])

#define next(c) (c->next)
#define label(c) (c->data)

int main(int argc, char *argv[]) {
	int input[] = {5, 6, 2, 8, 9, 3, 1, 4, 7};
	static cup cups[NCUPS];
	#define rinput(i) ((i) < lenof(input) ? input[i] - 1 : i)
	for (int i = 0; i < NCUPS; i++) {
			cups[rinput(i)] = (cup) { .data = rinput(i) + 1
			                                , .next = cups + rinput((i + 1) % NCUPS) };
	}

	cup *cur = &cups[input[0] - 1];
	for (int i = 0; i < 10000000; i++) {
		int current = label(cur);
		cup *removed = next(cur); // three long
		next(cur) = next(next(next(removed)));
		cur = next(cur);

		int dest = current;
		#define WRAP(n) (((n) - 1 + NCUPS) % NCUPS + 1)
		do {
			dest = WRAP(dest - 1);
		} while (
				 dest == label(removed)
			|| dest == label(next(removed))
			|| dest == label(next(next(removed)))
		);
		// printf("dest: %i\n", dest);
		cup *dest_p = &cups[dest - 1];

		// do the move
		next(next(next(removed))) = next(dest_p);
		next(dest_p) = removed;
	}
	printf("%li\n", (long int) label(next(cups)) * label(next(next(cups))));
}
