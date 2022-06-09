# -*- coding: utf-8 -*-
import os
import pymem
import ctypes
import time
from keystone import Ks, KS_ARCH_X86, KS_MODE_32


def asm2code(asm_code, syntax=0):
    ks = Ks(KS_ARCH_X86, KS_MODE_32)
    bytes_code, _ = ks.asm(asm_code, as_bytes=True)
    return bytes_code


def WxBaseStruct(process_handle, content):
    struct_address = pymem.memory.allocate_memory(process_handle, 20)
    bcontent = content.encode('utf-16le')
    content_address = pymem.memory.allocate_memory(process_handle, len(bcontent) + 16)
    pymem.ressources.kernel32.WriteProcessMemory(process_handle, content_address, bcontent, len(bcontent), None)
    pymem.memory.write_int(process_handle, struct_address, content_address)
    pymem.memory.write_int(process_handle, struct_address + 0x4, len(content))
    pymem.memory.write_int(process_handle, struct_address + 0x8, len(content) * 2)
    pymem.memory.write_int(process_handle, struct_address + 0xC, 0)
    pymem.memory.write_int(process_handle, struct_address + 0x10, 0)
    return struct_address, content_address


def start_thread(process_handle, address, params=None):
    params = params or 0
    NULL_SECURITY_ATTRIBUTES = ctypes.cast(0, pymem.ressources.structure.LPSECURITY_ATTRIBUTES)
    thread_h = pymem.ressources.kernel32.CreateRemoteThread(
        process_handle,
        NULL_SECURITY_ATTRIBUTES,
        0,
        address,
        params,
        0,
        ctypes.byref(ctypes.c_ulong(0))
    )
    last_error = ctypes.windll.kernel32.GetLastError()
    if last_error:
        pymem.logger.warning('Got an error in start thread, code: %s' % last_error)
    pymem.ressources.kernel32.WaitForSingleObject(thread_h, -1)
    return thread_h


def main(wxpid, wxid, msg):
    process_handle = pymem.process.open(wxpid)
    wxNull_address = pymem.memory.allocate_memory(process_handle, 0x100)
    buffer_address = pymem.memory.allocate_memory(process_handle, 0x3B0)
    wxid_struct_address, wxid_address = WxBaseStruct(process_handle, wxid)
    msg_struct_address, msg_address = WxBaseStruct(process_handle, msg)

    process_WeChatWin_handle = pymem.process.module_from_name(process_handle, "WeChatWin.dll")
    call_address = process_WeChatWin_handle.lpBaseOfDll + 0x521D30
    call_p_address = pymem.memory.allocate_memory(process_handle, 4)
    pymem.memory.write_int(process_handle, call_p_address, call_address)
    format_asm_code = '''
    push edi;
    lea eax,dword ptr ds:[{wxNull:#02x}];
    push 0x1;
    push eax;
    lea edi,dword ptr ds:[{wxTextMsg:#02x}];
    push edi;
    lea edx,dword ptr ds:[{wxWxid:#02x}];
    lea ecx,dword ptr ds:[{buffer:#02x}];
    call dword ptr ds:[{callAddress:#02x}];
    add esp, 0xC;
    pop edi;
    ret;
    '''
    asm_code = format_asm_code.format(wxNull=wxNull_address,
                                      wxTextMsg=msg_struct_address,
                                      wxWxid=wxid_struct_address,
                                      buffer=buffer_address,
                                      callAddress=call_p_address)
    shellcode = asm2code(asm_code.encode())
    shellcode_address = pymem.memory.allocate_memory(process_handle, len(shellcode) + 5)
    pymem.ressources.kernel32.WriteProcessMemory(process_handle, shellcode_address, shellcode, len(shellcode), None)
    thread_h = start_thread(process_handle, shellcode_address)
    time.sleep(0.5)
    pymem.memory.free_memory(process_handle, wxNull_address)
    pymem.memory.free_memory(process_handle, buffer_address)
    pymem.memory.free_memory(process_handle, wxid_struct_address)
    pymem.memory.free_memory(process_handle, wxid_address)
    pymem.memory.free_memory(process_handle, msg_struct_address)
    pymem.memory.free_memory(process_handle, msg_address)
    pymem.memory.free_memory(process_handle, call_p_address)
    pymem.memory.free_memory(process_handle, shellcode_address)
    pymem.process.close_handle(process_handle)


if __name__ == "__main__":
    wxpid = 18604
    wxid = "filehelper"
    msg = "python test msg"
    main(wxpid, wxid, msg)


