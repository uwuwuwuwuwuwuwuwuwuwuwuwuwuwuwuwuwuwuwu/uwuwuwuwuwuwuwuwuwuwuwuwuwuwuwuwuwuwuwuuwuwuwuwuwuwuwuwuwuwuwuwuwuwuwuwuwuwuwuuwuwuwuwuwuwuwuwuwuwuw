#include <efi.h>
#include <efilib.h>

EFI_STATUS
EFIAPI
efi_main (EFI_HANDLE hnd, EFI_SYSTEM_TABLE *SystemTable){
    InitializeLib(hnd, SystemTable);
    Print(L"uwu");
    while(1){
        Print(L"uwu");
    }
    return EFI_SUCCESS;
}
