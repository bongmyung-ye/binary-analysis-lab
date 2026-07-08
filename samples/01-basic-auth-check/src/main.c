#include <stdio.h>
#include <string.h>

#define MAX_INPUT 64

static int verify_passphrase(const char *input) {
    const char *expected = "lab-pass-2026";
    return strcmp(input, expected) == 0;
}

int main(void) {
    char input[MAX_INPUT];

    printf("Binary Analysis Lab - Basic Auth Check\n");
    printf("Enter passphrase: ");

    if (fgets(input, sizeof(input), stdin) == NULL) {
        printf("No input received.\n");
        return 1;
    }

    input[strcspn(input, "\r\n")] = '\0';

    if (verify_passphrase(input)) {
        printf("Access granted for lab sample.\n");
        return 0;
    }

    printf("Access denied for lab sample.\n");
    return 1;
}
