#include <stdio.h>
#include <stdlib.h>

typedef void* cup;

#define NCUPS 1000000

#define lenof(a) sizeof(a) / sizeof(a[0])

#define label(p) (long)(p - cups + 1)
#define next(p) (*(cup **)p)

int main(int argc, char *argv[]) {
	int input[] = {5, 6, 2, 8, 9, 3, 1, 4, 7};
	static cup cups[NCUPS];
	#define rinput(i) ((i) < lenof(input) ? input[i] - 1 : i)
	for (int i = 0; i < NCUPS; i++) {
		cups[rinput(i)] = &cups[rinput((i + 1) % NCUPS)];
	}

	cup *cur = &cups[input[0] - 1];
	for (int i = 0; i < 10000000; i++) {
		cup *moved[3] = {next(cur), next(moved[0]), next(moved[1])};

		int dest = label(cur);
		#define WRAP(n) (((n) - 1 + NCUPS) % NCUPS + 1)
		do {
			dest = WRAP(dest - 1);
		} while (
				 dest == label(moved[0])
			|| dest == label(moved[1])
			|| dest == label(moved[2])
		);
		// printf("dest: %i\n", dest);
		cup *dest_p = &cups[dest - 1];

		// do the moves
		next(cur) = next(moved[2]);
		next(moved[2]) = next(dest_p);
		next(dest_p) = moved[0];
		cur = next(cur);
	}
	printf("%li\n", (long int) label(next(cups)) * label(next(next(cups))));
}
