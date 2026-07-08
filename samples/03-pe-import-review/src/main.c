#include <stdio.h>

#ifdef _WIN32
#include <windows.h>
#include <lmcons.h>
#endif

static void print_environment_note(void) {
#ifdef _WIN32
    char username[UNLEN + 1];
    DWORD username_len = sizeof(username);
    DWORD tick_count = GetTickCount();

    if (GetUserNameA(username, &username_len)) {
        printf("Current user: %s\n", username);
    } else {
        printf("Current user: unavailable\n");
    }

    printf("Tick count: %lu\n", (unsigned long)tick_count);
    MessageBoxA(NULL, "PE Import Review sample executed.", "Binary Analysis Lab", MB_OK | MB_ICONINFORMATION);
#else
    printf("PE import review sample. Build on Windows to inspect Windows API imports.\n");
#endif
}

int main(void) {
    printf("Binary Analysis Lab - PE Import Review\n");
    print_environment_note();
    return 0;
}
