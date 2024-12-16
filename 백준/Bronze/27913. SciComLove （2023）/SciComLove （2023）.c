#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    int N, Q;
    scanf("%d %d", &N, &Q);

    // Initialize the string "SciComLove" repeated to the required length
    char s[20001];
    char base[] = "SciComLove";
    int base_length = strlen(base);

    for (int i = 0; i < N; i++) {
        s[i] = base[i % base_length];
    }
    s[N] = '\0'; // Null-terminate the string

    while (Q--) {
        int index;
        scanf("%d", &index);
        index--; // Convert to 0-based indexing

        // Toggle the case of the character at the given index
        if (isupper(s[index])) {
            s[index] = tolower(s[index]);
        } else {
            s[index] = toupper(s[index]);
        }

        // Count the number of uppercase letters
        int count = 0;
        for (int i = 0; i < N; i++) {
            if (isupper(s[i])) {
                count++;
            }
        }

        printf("%d\n", count);
    }

    return 0;
}