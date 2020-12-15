#include <stdio.h>

int start[] = {2,1,10,11,0,6};

int *history;

int get(int val, int def) {
	if (history[val] == -1) {
		return def;
	}
	return history[val];
}

int main(int argc, char *argv[]) {
	history = malloc(30000000 * 8);
	for (int i = 0; i < 30000000; i++) {
		history[i] = -1;
	}
	int next_;
	for (int i = 0; i < 30000000 - 1; i++) {
		if (i < sizeof(start) / sizeof(start[0])) {
			next_ = i - get(start[i], i);
			history[start[i]] = i;
			continue;
		}
		int say = next_;
		next_ = i - get(say, i);
		history[say] = i;
	}
	printf("%i\n", next_);
}
