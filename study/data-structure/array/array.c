#include <stdio.h>
#include <stdlib.h>

void print_array(char *array_type, int *array) {
	printf("%s\t: ", array_type);
	for (int idx = 0; idx < 5; idx++) {
		printf("%d\t", array[idx]);
	}
	printf("\n");
}

int main() {
	int static_array[5];

	for (int idx = 0; idx < 5; idx++) {
		static_array[idx] = idx * 10;
	}

	print_array("Static array", static_array);

	int *dynamic_array;

	dynamic_array = malloc(sizeof(int) * 5);
	for (int idx = 0; idx < 5; idx++) {
		dynamic_array[idx] = idx * 10;
	}

	print_array("Dynamic array", dynamic_array);
	free(dynamic_array);
}