import os, time, Teknikality, random, threading, shutil, sys
sys.stdout.reconfigure(encoding='utf-8') # type: ignore
logs = []
boot_time = time.time()
firstrun = True
def update_logs_screen():
    pass
    
def liveCD_create():
    print("Creating bootable installation CD...")
    base = "C:/python/XenonOS"
    if not os.path.exists(f"{base}/dd1"):
        os.mkdir(f"{base}/{osm.base_drive}")
    shutil.rmtree(f"{base}/{osm.base_drive}")
    os.makedirs(f"{base}/liveCD/", exist_ok=True)
    boot_file = os.path.join(base, "liveCD", "inboot.bin")
    disk_img = os.path.join(base, "liveCD", "predisk.img")
    write_file = os.path.join(base, "liveCD", "wrfiles.img")
    write_to_file_file = os.path.join(base, "liveCD", "dritefiles.img")
    files = [boot_file, disk_img, write_file, write_to_file_file]
    for file in files:
        try:
            if not os.path.exists(file):
                open(file, "w").close()
                print(f"XenonOS: Created {os.path.basename(file)} at {os.path.dirname(file)}/")
            else:
                print(f"XenonOS: {os.path.basename(file)} already exists at {os.path.dirname(file)}/")
        except OSError as e:
            print(f"XenonOS: Failed to create or access {file} — {e}")
    with open("C:/python/XenonOS/liveCD/inboot.bin", "w", encoding="utf-8") as bf:
        bf.write(r"""
import Teknikality, os, time
for i in range(5):
   print("_")
   Teknikality.clearscreen()
   time.sleep(0.7)
time.sleep(5)
print(Teknikality.colors.CYAN + "█" * 100000, end="")
print(Teknikality.colors.BG_CYAN + Teknikality.colors.BLACK) 
print("\x1b[H")
print("Everything on your disk will be REMOVED! Press enter to confirm!")
input()
print("Creating partition dd1")
os.makedirs("C:/python/XenonOS/dd1")
self.run("predisk.img")
                 """)
    with open("C:/python/XenonOS/liveCD/predisk.img", "w", encoding="utf-8") as bf:
        bf.write(r"""
import time, random
name = "dd1"
print("Creating system directories...")
base = "C:/python/XenonOS"
paths = [
        base,
        os.path.join(base, name),
        os.path.join(base, name, "boot"),
        os.path.join(base, name, "OS files"),
        os.path.join(base, name, "user files"),
        os.path.join(base, name, "OS files", "sysapps"),
    ]


for path in paths:
        time.sleep(random.uniform(0.3, 2))
        path_ready = path.replace("\\", "/")
        path_ready = path.split("\\")
        path_ready = path_ready[len(path_ready) - 1]
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Expect Write-d: {path_ready}")
            else:
                pass
        except OSError as e:
            print(f"Something went wrong and the installation has failed on {path_ready}")
print("Successfully created directories.")
print("Creating system files...")
print("Please wait whilst wrfiles.img starts.")
self.memory = []
self.run("wrfiles.img")
                 """)
    with open("C:/python/XenonOS/liveCD/wrfiles.img", "w", encoding="utf-8") as bf:
        bf.write(r'''
with open("C:/python/XenonOS/dd1/boot/boot.pex", "w") as wf:
        wf.write(r"""
self.loggingenabled = True
self.program_map = {}
self.detected_drives = []
self.program_alloc = {}
self.memoryView = {}
self.trace_back = ""
self.kcall_dump_map = {}
self.kcall_hascalled = False
self.kcall_file_stack = ["power_on"]
self.kcall_count = 0
self.kcall_stack = {} 
print(f"{self.memorySizeMax}B RAM detected.")
self.log(f"{self.memorySizeMax}B RAM detected.", component="Boot")
self.log(f"CPU @ {self.base_working_clock}GHz base clock", component="Boot")
print("XenonOS... Starting (For logs: {INSTALL_DRIVE}/OS files/log.rf)")
self.log("BOOT: Scanning for drives...", component="Boot")
def list_folders(base_path="C:/python/XenonOS"):
    # List all entries in the base path and filter only directories
    folder_names = [d for d in os.listdir(base_path)
                    if os.path.isdir(os.path.join(base_path, d))]
    return folder_names
folder_names = list_folders()
print(f"{len(folder_names)} drive(s) found.")
self.log(f"{len(folder_names)} drive(s) found: {folder_names}.", component="Boot")
self.detected_drives = folder_names
self.log("Memory data at address 1111 belongs to the amount of detected drives.", component="Boot")
d = int(len(folder_names))
self.writeToMemory(what=d)
self.log("Base drive will be treated as dd1.", component="Boot")
self.updMemView()




   
self.log("(MAIN) BOOT: LOADING KERNEL AT '{INSTALL_DRIVE}/boot/Kernel.pex'", component="Boot")
self.log("Clearning boot.pex from memory. (KERNEL STARTED (NO NEED))", component="Boot")
self.freeMemory(0, "boot.pex")
self.run("boot/Kernel.pex")
""")
with open("C:/python/XenonOS/dd1/boot/UEFI settings.pex", "w") as uefif:
        uefif.write("""
print("1: Change CPU max clock, 2: Change CPU base clock, 3: Change base drive (RISKY), 4: shutdown forcefully, 5: Change max cpu temp before throttle, 6: change max cpu temp before thermal shutdown (RISKY), 7: Change base power draw (RISKY), 8: boot")
while True:
                     act = input(">>>")
                     if act == "1":
                        self.max_clock = int(input())
                     elif act == "2":
                        self.base_working_clock = int(input())
                     elif act == "3":
                        self.base_drive = str(input())
                     elif act == "4":
                        Teknikality.clearscreen()
                        exit()
                     elif act == "5":
                        self.max_before_throttle = int(input())
                     elif act == "6":
                        self.max_before_thermal_shutdown = int(input())
                     elif act == "7":
                        self.base_power_draw = int(input())
                     elif act == "8":
                        self.memory = []
                        self.run("boot/boot.pex")
                     else:
                       continue                   
                    """)
with open("C:/python/XenonOS/dd1/boot/Kernel.pex", "w") as kf:
        kf.write("""
import time, Teknikality
import os
self.log("The kernel has started.", component="Kernel")
tb = self.get_traceBack()
self.log(f"Program traceback update: {tb}", component="Kernel")
print("Would you like to boot into safe mode?")
action = input("Y/N~$ ")
if action.lower() == "y":
   self.run("OS files/sysapps/safemode.pex")
else:
    print("Starting shell...")
    time.sleep(3)
    Teknikality.clearscreen()
    self.run("OS files/shell.xex")
    

""")
with open("C:/python/XenonOS/dd1/OS files/sysapps/safemode.pex", "w") as smf:
        smf.write("""
print("SAFEMODE")
print("1: UEFI-BIOS SETTINGS")
print("2. FORCE SHUTDOWN")
act = input("$>>>~")
while True:
 if act == "1":
   self.run("boot/UEFI settings.pex")
 elif act == "2":
   Teknikality.clearscreen()
   exit()
 else:
    continue
                  
                  """)
with open("C:/python/XenonOS/dd1/OS files/registry.xh", "w") as rf:
        rf.write("""
USERNAME = None
VERSION = None
SHELL_ACTIVE = False
USER_PERMISSIONS = 0
""")
with open("C:/python/XenonOS/dd1/OS files/shell.xex", "w") as sf:
        sf.write("""
self.log("SHELL: MAIN INIT, STARTING REGISTRY.", component="Shell")
self.exec_with_globals("OS files/registry.xh")
self.log("SHELL: REGISTRY LOADED. Current NameStates:", component="Shell")
self.log(f" USERNAME = {USERNAME}", component="Registry")
self.log(f" VERSION = {VERSION}", component="Registry")
self.log(f" SHELL_ACTIVE = {SHELL_ACTIVE}", component="Registry")
self.log(f" UESR_PERMISSIONS = {0}", component="Registry")
self.log("Process completed successfully.", component="Boot")
ms = self.listMemoryUsed()
self.log("Memory state after boot completion:", component="Boot")
self.log(f"  {ms}/{self.memorySizeMax}B Used ({Teknikality.numbertools.cap(round(ms / self.memorySizeMax * 100, 1))}%)", component="Boot")
MBA = hex(ms)
self.log(f"  {MBA} Max Byte Address", component="Boot")
self.log(f"  {self.baseaddr} Max Chunk Address", component="Boot")
self.log(f"Boot took {int((time.time() - boot_time) * 1000) / 1000} seconds.")
self.log(f"Full memory map:")
self.log(f"  {self.listProgramView()}")
Teknikality.clearscreen()
print(f"XENONOS - CMD:{USER_PERMISSIONS}")
user = input("Please enter a username:  ")
globals()[USERNAME] = user
self.log("Starting CLI parser...", component="Shell")
self.run("OS files/shellParseCode.cli")
Os
""")
with open("C:/python/XenonOS/dd1/OS files/shellParseCode.cli", "w") as spcf:
        spcf.write(r"""
import os, Teknikality
self.cpu_hz = 1.5
current_user_path = "OS files"
while True:
 try:
  cmd = input(f"CMD:{globals()[USERNAME]}@{current_user_path}~$").lower()
  self.log(f"ParseCommand: running {cmd}...", component="Shell Parse")
  if cmd.startswith("hex"):
    cmd_split = cmd.split(" ")
    args = cmd_split[1]
    func = cmd_split[2]
    if args == "get" and func == "systmsg":
        with open(f"C:\\python\\XenonOS\\{self.base_drive}\\OS files\\log.rf", "r") as f:
             l = f.read()
        print("LOGS =====")
        print(l)
        print("LOGS =====")
    if args == "dump" and func == "memory":
        self.byte_addr_dump()
    elif args == "manage" and func == "memory":
        ms = self.listMemoryUsed()
        self.listProgramView(log_or_print=False)
        print(f"  {ms / 1000} / {self.memorySizeMax / 1000}KB Used ({round(ms / self.memorySizeMax * 100, 1)}%)")
        MBA = hex(ms)
        print(f"  {MBA} Max Byte Address")
        print(f"  {self.baseaddr} Max Chunk Address")
    elif args == "view" and func == "programs":
        for program, info in self.program_map.items():
            print(f"{program}:")
            print(f"   {info}")
    elif args == "test" and func == "hardware":
         self.log("A hardware test is in progress!")
         print("Testing memory... (a restart WILL be required after to make sure there are no longer any zombie entries in memory!)")
         ms = self.listMemoryUsed()
         while round(ms / self.memorySizeMax * 100, 1) < 75:
             ms = self.listMemoryUsed()
             self.writeToMemory("MEMTEST")
         print("Complete!")
         print("Testing CPU...")
         while True:
                  self.log("Kernel-Power@CPU@Test: Inducing Payload!")
                  while True:
                     self.cpu_temp += 1
                     self.voltage = 60
                     self.cpu_hz = 3
                     if self.cpu_temp > self.max_before_throttle:
                        print("Stopping!")
                        print("Finished.")
                        print("Restart the computer. You completed the test.")
                        exit()
    elif args == "view" and func == "trace":
        print(self.get_traceBack())
        for n, b in self.program_alloc.items():
           print(f"{n}: {b}")
    elif args == "get" and func == "speed":
            print("CPU INFORMATION:")
            print(f"  CPU frequency: {self.cpu_hz} Hz")
            print(f"  CPU temperature: {self.cpu_temp} C")
            print(f"  Fan speed: {self.fan_speed} RPM")
            print(f"  Power Draw: {self.voltage}W")
  elif cmd.startswith("verb"):
        mode = cmd.split()
        mode = mode[1]
        if mode == "true":
           self.verbose_mode = True
           print("systmsg will now print to log.rf AND to the screen.")
        else:
           self.verbose_mode = False
  elif cmd.startswith("cd"):
        path = cmd.split()[1:]
        path = ' '.join(path)
        if os.path.exists(f"C:/python/XenonOS/{self.base_drive}/{path}/"):
           current_user_path = f"{path}"
           print(f"Changed to {path}")
        else:
           print(f"No such directory {path} ")
  elif cmd.startswith("ls"):
           path = current_user_path
           files = os.listdir(f"C:/python/XenonOS/{self.base_drive}/{path}/")
           for file in files:
               print(f"{Teknikality.colors.GREEN if "." in list(file) else Teknikality.colors.RED}  {file}  ", end="")
           print(Teknikality.colors.RESET)
  elif cmd.startswith("help"):
        print("Available commands: hex, view, help, start")
  elif cmd.startswith("clear"):
         self.cls()
  elif cmd.startswith("reboot"):
        print("Rebooting...")
        self.log("OS@Reboot~$ Sending shutdown signal to all tasks.")
        time.sleep(3)
        self.memory = []
        Teknikality.clearscreen()
        time.sleep(1.5)
        self.run("boot/boot.pex")
  elif cmd.startswith("start"):
       arg = cmd.split()[1]
       if arg == "filesys":
          print("Starting filesys...")
          self.log("memory@deallocProtection: Clearing shellParseCode.cli from memory.")
          self.freeMemory(block_program=self.program_alloc["OS files/shellParseCode.cli"], what_is_freeing="shellParseCode.cli")
          self.log("FileSys: Loading")
          self.run("OS files/sysapps/filesys.xex")
  else:
      self.log(f"NotAError: Invalid command: {cmd}", component="Shell Parse")
      raise Exception
 except Exception as e:
  print(e)
  self.log(msg=f"Invalid command: {cmd}, or error whilst executing command.", isErr=True, component="Shell Parse")
  print("Invalid command.")
  continue
                                   """)
with open("C:/python/XenonOS/dd1/OS files/sysapps/filesys.xex", "w") as ff:
        ff.write(r"""
import os, shutil
def delete_path(path):
    if os.path.isfile(path):
        os.remove(path)  # delete file
        print(f"Deleted file: {path}")
    elif os.path.isdir(path):
        shutil.rmtree(path)  # delete directory and all contents
        print(f"Deleted directory: {path}")
    else:
        print(f"Path does not exist: {path}")
selected_drive = self.base_drive
self.log("FileSys: LOADED", component="FS Viewer")
while True:
  try:
     command = input("FileSys~$ ")
     switches = command.split()
     self.log(f"FileSys@ReportCommandSplitData~$ {switches} (snapshot before execution: does not mean command will need it split!)", component="FS Viewer")
     self.log(f"FileSys: Running {command}", component="FS Viewer")
     if command.startswith("exit"):
        self.freeMemory(block_program=self.program_alloc["OS files/sysapps/filesys.xex"], what_is_freeing="filesys.xex")
        self.run("OS files/shellParseCode.cli")
     if switches[0] == "list":
        if len(switches) == 1:
         print(f"Contents of {selected_drive}:")
         c = os.listdir(path=f"C:/python/XenonOS/{selected_drive}")
         for f in c:
            print("  " + str(f))
        else:
          mainswitch = switches[1]
          if mainswitch == "-r":
              for r, d, f in os.walk(f"C:/python/XenonOS/{selected_drive}"):
                  file = r.replace(r"\\", "/")
                  file = file.split("/")
                  file = file[-1]
                  print(f"Contents of {file}:")
                  for dirs in d:
                     print(f"[ DIR ]@ {dirs}")
                  for files in f:
                      print("  ", files)
          else:
             print(f"Incorrect switch: {mainswitch}")
     if switches[0] == "delete":
           path = f"C:/python/XenonOS/{self.base_drive}/{' '.join(switches[1:])}"
           delete_path(path)
  except Exception as e:
     err = type(e).__name__
     err = str(err)
     if err == "PermissionError":
         print("Cannot delete file. File is in use! Please do not try to delete system files! All of them are critical to the OS booting and running normally.")
     self.log(f"Failed to run command {command}!", component="FS Viewer")
          
                     
                     
             """)
with open("C:/python/XenonOS/dd1/OS files/sysapps/panicErrorDump.xcfg", "w") as ehf:
        ehf.write("""
try:
    self.log("ErrorHandler@panicErrorDump.xcfg: Diagnosing...", component="PANIC")
    if self.latest_error is None:
        self.log("ErrorHandler@panicErrorDump.xcfg: Failed to diagnose!", component="PANIC")
        exit()
    else:
        human_readable = {
            "SyntaxError": "RUNTIME_FAILED_PARSE",
            "IndentationError": "RUNTIME_FAILED_PARSE",
            "IndexError": "RUNTIME_FAILED_PARSE",
            "KeyError": "RUNTIME_ACCESS_ERROR",
            "NameError": "RUNTIME_INCORRECT_POINT",
            "OSError": "INTERNAL_EXECUTION_FAILURE",
            "Unknown": "UNKNOWN",
            "OutOfMemoryError": "STACK_MEMORY_OVERFLOW",
            "FileNotFoundError": "FILE_NOT_FOUND",
            "BootError": "PREX_RUNTIME_BOOT_FAILURE",
            "MemoryAccessViolation": "MEMORY_ACCESS_FAULT",
            "ThermalShutdown": "THERMAL_SAFETY_EXCEPTION"
        }
        human_easy_read = human_readable.get(self.latest_error, "UNKNOWN")
        self.log(f"Stop code (FROM LAST ERROR):{human_easy_read}.", component="PANIC")
        print(f"Stop code: {human_easy_read}")
        while True:
          print("Press D to dump memory. Press T to view traceback. Press E to exit.")
          act = input("ErrorHandler@panicErrorDump.xcfg> ")
          act = act.lower()
          if act == "d":
             self.byte_addr_dump()
          elif act == "t":
              print(self.trace_back)
          elif act == "e":
             exit()
          else:
             print("Incorrect action!")
except Exception:
    self.log("ErrorHandler@panicErrorDump.xcfg: During handling of the last exception, another occured and the panic handler cannot continue", component="PANIC")
    exit()
   
                    """)
               
   
                   
                 ''')
    print("done!")
    exit()
def simulation_start():
    global firstrun
    if not firstrun:
        exit()
    print("DEBUG: simulation_start() ENTER")
    print("Generate new filesystem?")
    action = input("Y/N: ")
    if action.lower() != "y":
           osm.clslogs()
           firstrun = False
           osm.memory.clear()
           osm.memoryView.clear()
           osm.baseaddr = 1111
           osm.boot()
           exit()
    print("Installer Or Full OS?")
    print("Y=installer, N=OS")
    if input().lower() == "y":
        liveCD_create()
        osm.boot()
    print("XenonOS: Rebuilding filesystem...")
    osm.base_drive = "dd1"
    osm.clslogs()
    base = "C:/python/XenonOS"
    os.system('del "C:/python/XenonOS/dd1/OS files/modules"')
    paths = [
        base,
        os.path.join(base, "dd1"),
        os.path.join(base, "dd1", "boot"),
        os.path.join(base, "dd1", "OS files"),
        os.path.join(base, "dd1", "user files"),
        os.path.join(base, "dd1", "OS files", "sysapps"),
        os.path.join(base, "dd1", "OS files", "modules"),
    ]

    # Create directories safely
    for path in paths:
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"XenonOS: Created directory at {path}/")
            else:
                print(f"XenonOS: Directory already exists at {path}/")
        except OSError as e:
            print(f"XenonOS: Failed to create or access {path}/ — {e}")

    # Create empty system files
    boot_file = os.path.join(base, "dd1", "boot", "boot.pex")
    kernel_file = os.path.join(base, "dd1", "boot", "Kernel.pex")
    filesys_file = os.path.join(base, "dd1", "OS files", "sysapps", "filesys.xex")
    shell_file = os.path.join(base, "dd1", "OS files", "shell.xex")
    log_file = os.path.join(base, "dd1", "OS files", "log.rf")
    registry_file = os.path.join(base, "dd1", "OS files", "registry.xh")
    safe_mode_file = os.path.join(base, "dd1", "OS files", "sysapps", "safemode.pex")
    error_handling_file = os.path.join(base, "dd1", "OS files", "sysapps", "panicErrorDump.xcfg")
    UEFI_file = os.path.join(base, "dd1", "boot", "UEFI settings.pex")
    
    files = [boot_file, filesys_file, shell_file, log_file, registry_file, kernel_file, safe_mode_file, error_handling_file, UEFI_file]

    for file in files:
        try:
            if not os.path.exists(file):
                open(file, "w").close()
                print(f"XenonOS: Created {os.path.basename(file)} at {os.path.dirname(file)}/")
            else:
                print(f"XenonOS: {os.path.basename(file)} already exists at {os.path.dirname(file)}/")
        except OSError as e:
            print(f"XenonOS: Failed to create or access {file} — {e}")
    with open("C:/python/XenonOS/dd1/boot/boot.pex", "w") as wf:
        wf.write(r"""
self.loggingenabled = True
self.program_map = {}
self.detected_drives = []
self.program_alloc = {}
self.memoryView = {}
self.trace_back = ""
self.kcall_dump_map = {}
self.kcall_hascalled = False
self.kcall_file_stack = ["power_on"]
self.kcall_count = 0
self.kcall_stack = {} 
print(f"{self.memorySizeMax}B RAM detected.")
self.log(f"{self.memorySizeMax}B RAM detected.", component="Boot")
self.log(f"CPU @ {self.base_working_clock}GHz base clock", component="Boot")
print("XenonOS... Starting (For logs: {INSTALL_DRIVE}/OS files/log.rf)")
self.log("BOOT: Scanning for drives...", component="Boot")
def list_folders(base_path="C:/python/XenonOS"):
    # List all entries in the base path and filter only directories
    folder_names = [d for d in os.listdir(base_path)
                    if os.path.isdir(os.path.join(base_path, d))]
    return folder_names
folder_names = list_folders()
print(f"{len(folder_names)} drive(s) found.")
self.log(f"{len(folder_names)} drive(s) found: {folder_names}.", component="Boot")
self.detected_drives = folder_names
self.log("Memory data at address 1111 belongs to the amount of detected drives.", component="Boot")
d = int(len(folder_names))
self.writeToMemory(what=d)
self.log("Base drive will be treated as dd1.", component="Boot")
self.updMemView()




   
self.log("(MAIN) BOOT: LOADING KERNEL AT '{INSTALL_DRIVE}/boot/Kernel.pex'", component="Boot")
self.log("Clearning boot.pex from memory. (KERNEL STARTED (NO NEED))", component="Boot")
self.freeMemory(0, "boot.pex")
self.run("boot/Kernel.pex")
""")
    with open("C:/python/XenonOS/dd1/boot/UEFI settings.pex", "w") as uefif:
        uefif.write("""
print("1: Change CPU max clock, 2: Change CPU base clock, 3: Change base drive (RISKY), 4: shutdown forcefully, 5: Change max cpu temp before throttle, 6: change max cpu temp before thermal shutdown (RISKY), 7: Change base power draw (RISKY), 8: boot")
while True:
                     act = input(">>>")
                     if act == "1":
                        self.max_clock = int(input())
                     elif act == "2":
                        self.base_working_clock = int(input())
                     elif act == "3":
                        self.base_drive = str(input())
                     elif act == "4":
                        Teknikality.clearscreen()
                        exit()
                     elif act == "5":
                        self.max_before_throttle = int(input())
                     elif act == "6":
                        self.max_before_thermal_shutdown = int(input())
                     elif act == "7":
                        self.base_power_draw = int(input())
                     elif act == "8":
                        self.memory = []
                        self.run("boot/boot.pex")
                     else:
                       continue                   
                    """)
    with open("C:/python/XenonOS/dd1/boot/Kernel.pex", "w") as kf:
        kf.write("""
import time, Teknikality
import os
self.log("The kernel has started.", component="Kernel")
tb = self.get_traceBack()
self.log(f"Program traceback update: {tb}", component="Kernel")
print("Would you like to boot into safe mode?")
action = input("Y/N~$ ")
if action.lower() == "y":
   self.run("OS files/sysapps/safemode.pex")
else:
    print("Starting shell...")
    time.sleep(3)
    Teknikality.clearscreen()
    self.run("OS files/shell.xex")
    

""")
    with open("C:/python/XenonOS/dd1/OS files/sysapps/safemode.pex", "w") as smf:
        smf.write("""
print("SAFEMODE")
print("1: UEFI-BIOS SETTINGS")
print("2. FORCE SHUTDOWN")
act = input("$>>>~")
while True:
 if act == "1":
   self.run("boot/UEFI settings.pex")
 elif act == "2":
   Teknikality.clearscreen()
   exit()
 else:
    continue
                  
                  """)
    with open("C:/python/XenonOS/dd1/OS files/registry.xh", "w") as rf:
        rf.write("""
USERNAME = None
VERSION = "XenonOS-5.2x"
SHELL_ACTIVE = False
USER_PERMISSIONS = 0
""")
    with open("C:/python/XenonOS/dd1/OS files/shell.xex", "w") as sf:
        sf.write("""
self.log("SHELL: MAIN INIT, STARTING REGISTRY.", component="Shell")
self.exec_with_globals("OS files/registry.xh")
self.log("SHELL: REGISTRY LOADED. Current NameStates:", component="Shell")
self.log(f" USERNAME = {USERNAME}", component="Registry")
self.log(f" VERSION = {VERSION}", component="Registry")
self.log(f" SHELL_ACTIVE = {SHELL_ACTIVE}", component="Registry")
self.log(f" UESR_PERMISSIONS = {0}", component="Registry")
self.log("Process completed successfully.", component="Boot")
ms = self.listMemoryUsed()
self.log("Memory state after boot completion:", component="Boot")
self.log(f"  {ms}/{self.memorySizeMax}B Used ({Teknikality.numbertools.cap(round(ms / self.memorySizeMax * 100, 1))}%)", component="Boot")
MBA = hex(ms)
self.log(f"  {MBA} Max Byte Address", component="Boot")
self.log(f"  {self.baseaddr} Max Chunk Address", component="Boot")
self.log(f"Boot took {int((time.time() - boot_time) * 1000) / 1000} seconds.")
self.log(f"Full memory map:")
self.log(f"  {self.listProgramView()}")
Teknikality.clearscreen()
print(f"XENONOS - CMD:{USER_PERMISSIONS}")
user = input("Please enter a username:  ")
globals()[USERNAME] = user
self.log("Starting CLI parser...", component="Shell")
self.run("OS files/shellParseCode.cli")
""")
    with open("C:/python/XenonOS/dd1/OS files/shellParseCode.cli", "w") as spcf:
        spcf.write(r"""
import os, Teknikality, time, random
self.cpu_hz = 1.5
cap = "xyz"
current_user_path = "/"
sa = True
up = 0
while True:
 try:
  cmd = input(f"CMD:{globals()[USERNAME]}@{current_user_path}~$").lower()
  if "verb" in cmd and up < 2:
     print("Invalid permissions!")
     continue
  if "mdpkg" in cmd and up < 3:
     print("Invalid permissions!")
     continue
  if "start" in cmd and up < 2:
     print("Invalid permissions!")
     continue
  self.log(f"ParseCommand: running {cmd}...", component="Shell Parse")
  if cmd.startswith("hex"):
    cmd_split = cmd.split(" ")
    args = cmd_split[1]
    func = cmd_split[2]
    if args == "get" and func == "systmsg":
        with open(f"C:\\python\\XenonOS\\{self.base_drive}\\OS files\\log.rf", "r") as f:
             l = f.read()
        print("LOGS =====")
        print(l)
        print("LOGS =====")
    if args == "dump" and func == "memory":
        self.byte_addr_dump()
    elif args == "get" and func == "up":
       if input("Enter Password:  ") == cap:
          print("Password is correct!")
          up = 3
       else:
          print("Invalid Password!") 
    elif args == "manage" and func == "memory":
        ms = self.listMemoryUsed()
        self.listProgramView(log_or_print=False)
        print(f"  {ms / 1000} / {self.memorySizeMax / 1000}KB Used ({round(ms / self.memorySizeMax * 100, 1)}%)")
        MBA = hex(ms)
        print(f"  {MBA} Max Byte Address")
        print(f"  {self.baseaddr} Max Chunk Address")
    elif args == "view" and func == "programs":
        for program, info in self.program_map.items():
            print(f"{program}:")
            print(f"   {info}")
    elif args == "view" and fun == "reg":
          print(sa, up)
    elif args == "test" and func == "hardware":
         self.log("A hardware test is in progress!")
         print("Testing memory... (a restart WILL be required after to make sure there are no longer any zombie entries in memory!)")
         ms = self.listMemoryUsed()
         while round(ms / self.memorySizeMax * 100, 1) < 75:
             ms = self.listMemoryUsed()
             self.writeToMemory("MEMTEST")
         print("Complete!")
         print("Testing CPU...")
         while True:
                  self.log("Kernel-Power@CPU@Test: Inducing Payload!")
                  while True:
                     self.cpu_temp += 1
                     self.voltage = 60
                     self.cpu_hz = 3
                     if self.cpu_temp > self.max_before_throttle:
                        print("Stopping!")
                        print("Finished.")
                        print("Restart the computer. You completed the test.")
                        exit()
    elif args == "view" and func == "trace":
        print(self.get_traceBack())
        for n, b in self.program_alloc.items():
           print(f"{n}: {b}")
    elif args == "get" and func == "speed":
            print("CPU INFORMATION:")
            print(f"  CPU frequency: {self.cpu_hz} Hz")
            print(f"  CPU temperature: {self.cpu_temp} C")
            print(f"  Fan speed: {self.fan_speed} RPM")
            print(f"  Power Draw: {self.voltage}W")
  elif cmd.startswith("mdpkg"):
        split = cmd.split()[1:]
        switch = split[0]
        if switch == "-i":
            name = split[1]
            print(f"Acquiring {name}...")
            if os.path.exists(f"C:/python/xmodules/{name}"):
                size = os.path.getsize(f"C:/python/xmodules/{name}")
                print(f"Found name {name}. Installing {size} bytes of data.")
                with open(f"C:/python/xmodules/{name}", "r", encoding="utf-8") as f:
                     print(f"Opened!")
                     contents = f.read()
                     print("Writing to OS files/modules")
                with open(f"C:/python/XenonOS/{self.base_drive}/OS files/modules/{name}", "w") as f2:
                    f2.write(contents)
                time.sleep(2)
                print(f"Successfully installed {name}")
            else:
              print(f"Module {name} does not exist!")
        elif switch == "-r":
            name = split[1]
            with open(f"C:/python/XenonOS/{self.base_drive}/OS files/modules/{name}", "r") as f:
                    print(f"Executing {name}")
                    code = f.read()
            try:
             exec(code)
            except Exception as e:
               print(f"Error in python module {name}: {e}")
            print(f"Finished {name}")
        elif switch == "-?":
               print("To install modules: -i, to run modules: -r, to delete modules: -d, to list available modules: -l")
        elif switch == "-d":
               name = split[1]
               os.remove(f"C:/python/XenonOS/dd1/OS files/modules/{name}")
               print(f"Successfully removed module {name}!")
        elif switch == "-l":
             files = os.listdir("C:/python/xmodules")
             print("========")
             for file in files:
                print(file)
             print("========")
  elif cmd.startswith("verb"):
        mode = cmd.split()
        mode = mode[1]
        if mode == "true":
           self.verbose_mode = True
           print("systmsg will now print to log.rf AND to the screen.")
        else:
           self.verbose_mode = False
  elif cmd.startswith("cd"):
        path = cmd.split()[1:]
        path = ' '.join(path)
        if os.path.exists(f"C:/python/XenonOS/{self.base_drive}/{path}/"):
           current_user_path = f"{path}"
           print(f"Changed to {path}")
        else:
           print(f"No such directory {path} ")
  elif cmd.startswith("ls"):
           path = current_user_path
           files = os.listdir(f"C:/python/XenonOS/{self.base_drive}/{path}/")
           for file in files:
               print(f"{Teknikality.colors.GREEN if "." in list(file) else Teknikality.colors.RED}  {file}  ", end="")
           print(Teknikality.colors.RESET)
  elif cmd.startswith("help"):
        print("Available commands: hex, view, help, start")
  elif cmd.startswith("clear"):
         self.cls()
  elif cmd.startswith("reboot"):
        print("Rebooting...")
        self.log("OS@Reboot~$ Sending shutdown signal to all tasks.")
        time.sleep(3)
        self.memory = []
        Teknikality.clearscreen()
        time.sleep(1.5)
        self.run("boot/boot.pex")
  elif cmd.startswith("start"):
       arg = cmd.split()[1]
       if arg == "filesys":
          print("Starting filesys...")
          self.log("memory@deallocProtection: Clearing shellParseCode.cli from memory.")
          self.freeMemory(block_program=self.program_alloc["OS files/shellParseCode.cli"], what_is_freeing="shellParseCode.cli")
          self.log("FileSys: Loading")
          self.run("OS files/sysapps/filesys.xex")
  else:
      self.log(f"NotAError: Invalid command: {cmd}", component="Shell Parse")
      raise Exception
 except Exception as e:
  self.log(msg=f"Invalid command: {cmd}, or error whilst executing command.", isErr=True, component="Shell Parse")
  print("Invalid command.")
  continue
                                   """)
    with open("C:/python/XenonOS/dd1/OS files/sysapps/filesys.xex", "w") as ff:
        ff.write(r"""
import os, shutil
def delete_path(path):
    if os.path.isfile(path):
        os.remove(path)  # delete file
        print(f"Deleted file: {path}")
    elif os.path.isdir(path):
        shutil.rmtree(path)  # delete directory and all contents
        print(f"Deleted directory: {path}")
    else:
        print(f"Path does not exist: {path}")
selected_drive = self.base_drive
self.log("FileSys: LOADED", component="FS Viewer")
while True:
  try:
     command = input("FileSys~$ ")
     switches = command.split()
     self.log(f"FileSys@ReportCommandSplitData~$ {switches} (snapshot before execution: does not mean command will need it split!)", component="FS Viewer")
     self.log(f"FileSys: Running {command}", component="FS Viewer")
     if command.startswith("exit"):
        self.freeMemory(block_program=self.program_alloc["OS files/sysapps/filesys.xex"], what_is_freeing="filesys.xex")
        self.run("OS files/shellParseCode.cli")
     if switches[0] == "list":
        if len(switches) == 1:
         print(f"Contents of {selected_drive}:")
         c = os.listdir(path=f"C:/python/XenonOS/{selected_drive}")
         for f in c:
            print("  " + str(f))
        else:
          mainswitch = switches[1]
          if mainswitch == "-r":
              for r, d, f in os.walk(f"C:/python/XenonOS/{selected_drive}"):
                  file = r.replace(r"\\", "/")
                  file = file.split("/")
                  file = file[-1]
                  print(f"Contents of {file}:")
                  for dirs in d:
                     print(f"[ DIR ]@ {dirs}")
                  for files in f:
                      print("  ", files)
          else:
             print(f"Incorrect switch: {mainswitch}")
     if switches[0] == "delete":
           path = f"C:/python/XenonOS/{self.base_drive}/{' '.join(switches[1:])}"
           delete_path(path)
  except Exception as e:
     err = type(e).__name__
     err = str(err)
     if err == "PermissionError":
         print("Cannot delete file. File is in use! Please do not try to delete system files! All of them are critical to the OS booting and running normally.")
     self.log(f"Failed to run command {command}!", component="FS Viewer")
          
                     
                     
             """)
    with open("C:/python/XenonOS/dd1/OS files/sysapps/panicErrorDump.xcfg", "w") as ehf:
        ehf.write("""
try:
    self.log("ErrorHandler@panicErrorDump.xcfg: Diagnosing...", component="PANIC")
    if self.latest_error is None:
        self.log("ErrorHandler@panicErrorDump.xcfg: Failed to diagnose!", component="PANIC")
        exit()
    else:
        human_readable = {
            "SyntaxError": "RUNTIME_FAILED_PARSE",
            "IndentationError": "RUNTIME_FAILED_PARSE",
            "IndexError": "RUNTIME_FAILED_PARSE",
            "KeyError": "RUNTIME_ACCESS_ERROR",
            "NameError": "RUNTIME_INCORRECT_POINT",
            "OSError": "INTERNAL_EXECUTION_FAILURE",
            "Unknown": "UNKNOWN",
            "OutOfMemoryError": "STACK_MEMORY_OVERFLOW",
            "FileNotFoundError": "FILE_NOT_FOUND",
            "BootError": "PREX_RUNTIME_BOOT_FAILURE",
            "MemoryAccessViolation": "MEMORY_ACCESS_FAULT",
            "ThermalShutdown": "THERMAL_SAFETY_EXCEPTION"
        }
        human_easy_read = human_readable.get(self.latest_error, "UNKNOWN")
        self.log(f"Stop code (FROM LAST ERROR):{human_easy_read}.", component="PANIC")
        print(f"Stop code: {human_easy_read}")
        while True:
          print("Press D to dump memory. Press T to view traceback. Press E to exit.")
          act = input("ErrorHandler@panicErrorDump.xcfg> ")
          act = act.lower()
          if act == "d":
             self.byte_addr_dump()
          elif act == "t":
              print(self.trace_back)
          elif act == "e":
             exit()
          else:
             print("Incorrect action!")
except Exception:
    self.log("ErrorHandler@panicErrorDump.xcfg: During handling of the last exception, another occured and the panic handler cannot continue", component="PANIC")
    exit()
   
                    """)
        
    
    exit()


class osmain:
    def __init__(self):
        self.verbose_mode = True
        self.kcall_dump_map = {}
        self.kcall_hascalled = False
        self.kcall_file_stack = ["power_on"]
        self.kcall_count = 0
        self.kcall_stack = {} # This will be a dictionary of EVERYTHING. Do not care about neat layout, just DUMP EVERYTHING. (Everything is a subject of boot.pex)
        self.install_timer_enabled = False
        self.enabled = True
        self.latest_error = None
        self.base_drive = "dd1"
        self.loggingenabled = True
        self.memorySizeMax = 32000 # 32KB: 32000  bytes
        self.cpu_hz = 0
        self.baseaddr = 1111
        self.fan_speed = 0
        self.cpu_temp = 21
        self.fan_speed = 0
        self.base_working_clock = 2
        self.base_power_draw = 20
        self.max_before_throttle = 75
        self.max_before_thermal_shutdown = 120
        self.max_clock = 3
        self.voltage = 20
        self.memory = []
        self.program_map = {}
        self.detected_drives = []
        self.program_alloc = {}
        self.memoryView = {}
        self.trace_back = "\n"
    def cls(self):
        Teknikality.clearscreen()
    def byte_addr_dump(self):
        for ca in self.memory:
            ca = list(str(ca))
            for addr, d in enumerate(ca):
                print(f"{hex(addr)}: {hex(ord(d))}")
    def hexDump(self):
        print(Teknikality.text_to_hex_dump(self.memoryView))
    def listProgramView(self, log_or_print=True):
        if log_or_print:
         for program, info in self.program_map.items():
            self.log(program, component="List Programs")
            self.log(f"   {info}", component="List Programs")
        else:
          for program, info in self.program_map.items():
            self.log(program, component="List Programs")
            self.log(f"   {info}", component="List Programs")      
            
    def clslogs(self):
        self.writeTo(dir="OS files/log.rf", data="")
    def getError(self, error, isFatal=True, what_failed="NOT PROVIDED", isBootIssue=False, basic_information="Fatal Error!"):
        self.verbose_mode = False
        print("Where am i?!")
        if self.kcall_hascalled:
            print("Looks like a second kcall-panic has been called.")
            print("0xF4 -> HLT (Kernel forced halt)")
            print("Restart your computer. No longer synced with I/O")
            exit()
        print(Teknikality.colors.BLACK, Teknikality.colors.BG_RED, end="")
        print()
        print("-----------------------------------")
        print("KERNEL EXCECPTION                  ")
        print("-----------------------------------")
        print(Teknikality.colors.RESET)
        self.kcall_hascalled = True
        print("kernel-kcall: invoke kcall (PANIC)")
        self.log("kernel-kcall: invoke kcall (PANIC)", component="Kernel kcall")
        error = str(error)
        REGISTERS = ["EAX", "EBX", "ECX", "EDX", "ESI", "EDI", "EBP", "ESP"]
        print(Teknikality.colors.BLACK, Teknikality.colors.BG_RED, end="")
        print()
        print(f"Kernel Panic - {'Not Syncing' if not self.loggingenabled else 'Still Syncing'} - {basic_information}")
        print(Teknikality.colors.RESET)
        print(Teknikality.colors.RED)
        keys = {
            "SyntaxError": 1,
            "IndentationError": 2,
            "IndexError": 3,
            "KeyError": 4,
            "NameError": 5,
            "OSError": 6,
            "Unknown": 115292150459,
            "OutOfMemoryError": 7,
            "FileNotFoundError": 8,
            "BootError": 9,
            "MemoryAccessViolation": 10,
            "ThermalShutdown": 11
        }
        self.log(self.kcall_stack, component="Kernel kcall")
        print("Kcall CALL STACK")
        print("================================")
        for _, info in self.kcall_dump_map.items():
            print(info, end="")
            self.log(info, component="Kernel kcall")
        print("================================")
        print("Additional Program Information:")
        for call_count, information in self.kcall_stack.items():
            print(f"CALLED: {call_count}, INFORMATION: {information}")
            self.log(f"CALLED: {call_count}, INFORMATION: {information}", component="Kernel kcall")
        print("\nExecution order:")
        print(' -> '.join(self.kcall_file_stack))
        print("================================")
        size = 0
        for reg in REGISTERS:
           print(f" {reg}= 0x{random.randint(0, 0xFFFFFFFF):08X} ", end="")
           self.log(f"{reg}= 0x{random.randint(0, 0xFFFFFFFF):08X}", component="Kernel kcall")
           if size > 3:
               size = 0
               print()
           size += 1
        print()
        self.latest_error = error if error in keys else "Unknown"
        if self.latest_error not in keys:
            self.latest_error = "Unknown"
        if error not in keys:
            error = "Unknown"
        self.log(isErr=True, msg=f"Eror in {what_failed}: {hex((keys[error]) * 10000000)}", component="Kernel kcall")
        if not isFatal:
         print(f"Error occurred whilst running {what_failed} ({hex((keys[error]) * 10000000)})")
         print(f"See OS files/log.rf for more information.")
        else:
            self.log("IsFatal=True, running dd1/OS files/sysapps/panicErrorDump.xcfg", component="Kernel kcall")
            self.log(isErr=True, msg=f"{hex((keys[error]) * 10000000)}: FATAL: cannot continue due to error.", component="Kernel kcall")
            print(f"Fatal error occurred whilst running {what_failed} ({hex((keys[error]) * 10000000)})")
            print(f"See OS files/log.rf for more information.")
            if isBootIssue:
                self.log(isErr=True, msg=f"preXecutionEnviroment@{what_failed}: A previous issue was identified as a boot issue!", component="Kernel kcall")
                print(f"{what_failed} is a .pex subject of boot.pex (preXecutionEnviroment@{what_failed})")
            try:
              print("kcall: invoke panicErrorDump.xcfg")
              self.run("OS files/sysapps/panicErrorDump.xcfg")
            except Exception:
                print("The panic handler failed to start!")
            print(Teknikality.colors.WHITE + "Hanging Here... (Manually power cycle your computer.)")
            print(Teknikality.colors.RESET)
            exit()

    def exec_with_globals(self, dir):
      self.enabled = False
      content_len = os.path.getsize(f"C:/python/XenonOS/{self.base_drive}/{dir}")
      current_boot_ms_time = int((time.time() - boot_time) * 1000)
      if self.listMemoryUsed() / self.memorySizeMax * 100 > 90:
        self.log(warn=True, msg=f"MemoryWarning: More than 90% of memory is in use (needing to run program {dir}).", component="Execve")
      try:
     
       with open(f"C:/python/XenonOS/{self.base_drive}/{dir}", "r") as f:
        d = f.read()
        before_alloc = self.listMemoryUsed()
        self.kcall_stack[str(self.kcall_count)] = {
            "SUBJECT-OF": self.kcall_file_stack[-1],
            "BEFORE-ALLOCATION": before_alloc,
            "FILE-NAME": dir,
            "IS-GLOBAL": True,
            "IS_PREX_ENVIRO": True,
            "FILE-SIZE": content_len
        }
        self.kcall_file_stack.append(dir)
        self.writeToMemory(what=d)
        self.kcall_dump_map[dir] = f"{hex(before_alloc)}+{hex(self.listMemoryUsed())}  [{dir} + GLOBAL] ({current_boot_ms_time}MS)\n"
        self.log(f"{dir} will take an estimated {len(d) / 1000 + self.memory.index(d) / 1000 + self.listMemoryUsed() / 1000 + round(random.uniform(0, 1.8), 1)} seconds to run.", component="Execve")
        self.log(f"Allocated {len(d)}B ({len(d) / 1000}KB) ({round(len(d) / self.memorySizeMax * 100, 2)}% Of memory) For {dir} (Adresses {hex(before_alloc)}-{hex(self.listMemoryUsed())}) (THIS PROGRAM IS RUNNING WITH GLOBALS())", component="Execve")
        self.program_map[dir] = f"{len(d)}B"
        time.sleep(len(d) / 1000 + self.memory.index(d) / 1000 + self.listMemoryUsed() / 1000)
        self.cpu_hz += len(d) / 1000 + self.memory.index(d) / 1000 + self.listMemoryUsed() / 1000
        self.cpu_hz = Teknikality.numbertools.cap(self.cpu_hz, min=1, max=2 if len(d) < 100 else 3)
        self.cpu_hz = round(self.cpu_hz, 1)
        if self.listMemoryUsed() > self.memorySizeMax:
            self.log(isErr=True, msg="Out of memory!", component="Execve")
            print("Out of memory.")
            self.getError("OutOfMemoryError", what_failed=f"run() on {dir}", isFatal=True, basic_information="Out Of memory")
        workload = len(d) / 200  # ~5 for a 1000B program
        workload = Teknikality.numtools.cap(workload, min=0, max=5)
        randomcoolingeffect = random.randint(-5, 5)
        self.cpu_temp += workload * self.cpu_hz + randomcoolingeffect
        self.cpu_temp -= self.fan_speed / 1000
        self.fan_speed = workload * self.cpu_hz * 200
        self.fan_speed = Teknikality.numtools.cap(self.fan_speed, min=0, max=4000)
        if self.fan_speed > 3000:
            self.log(warn=True, msg=f"High fan speed! ({self.fan_speed})", component="Execve")
        self.voltage = self.base_power_draw + (workload * self.cpu_hz * 2)
        self.voltage = Teknikality.numtools.cap(self.voltage, min=0, max=60)
        
        if self.cpu_temp > self.max_before_throttle:  
            self.log("Power@CPU@thermalControl: CPU is throttling.", warn=True, component="Execve")
            self.cpu_hz = 1
            if self.cpu_temp > self.max_before_thermal_shutdown:
                self.log(isErr=True, msg="Kernel-Power@CPUunsafeShutdown@thermalControl: A thermal shutdown has occoured.", component="Execve") 
                Teknikality.clearscreen() 
                print("--- THERMAL ERROR ---")
                print("A thermal shutdown has occoured.") 
                time.sleep(5) 
                Teknikality.clearscreen() 
                self.cpu_temp = 40
                self.getError("ThermalShutdown", what_failed="ThermalShutdown@run()", isFatal=True, basic_information=f"CPU#{random.randint(0, 4)} reports {round(self.cpu_temp)}C!") 
                exit()
        if self.cpu_temp > 200:
            exit()
        self.log(f"CPU: Working at {self.cpu_hz}Hz, Temp:{round(self.cpu_temp, 1)}C, FanSpeed:{round(self.fan_speed)}RPM, Power Draw:{self.voltage}W", component="Execve")
        if self.listMemoryUsed() / self.memorySizeMax * 100 > 90:
           self.log(warn=True, msg=f"MemoryWarning: More than 90% of memory is in use (after running {dir}).", component="Execve")
       self.trace_back += f"{current_boot_ms_time}MS at run(GLOBALS):{dir}, \n"
       self.enabled = True
       self.kcall_count += 1
       self.log(f"kernel-kcall: invoke {dir} ({dir}: CHECKSUMS COMPLETE)", component="kcall")
       exec(d, globals())
      except Exception as e:
        err = type(e).__name__
        err = str(err)
        self.getError(err, what_failed=dir, basic_information=f"Failed during execution of global program {dir}")
    def updMemView(self):
        last = self.baseaddr
        self.baseaddr = 1111
        self.log(f"UpdMemView: Ressetting baseaddr to reset chunk addressing. [last={last}]", component="Execve")
        loop = 0
        for m in self.memory:
            self.memoryView[self.baseaddr] = m
            self.baseaddr += 11
            loop += 1
            self.log(f"updMemView: baseaddr set to {self.baseaddr}. Execute 'hex dump memory' in shell to see full hex dump.", component="Execve")
        self.log(f"updMemView: FINISHED! (loop:{loop}-{last}/{self.baseaddr})", component="Execve")
    def listMemoryUsed(self):
        size = 0
        for obj in self.memory:
                size += len(str(obj))
        return size
    def freeMemory(self, block_program, what_is_freeing="NOT PROVIDED"):
        try:
            current_boot_ms_time = int((time.time() - boot_time) * 1000)
            self.log(f"Freeing {len(str(self.memory[block_program]))}B Of memory that once belonged to program {what_is_freeing}", component="Memory")
            self.baseaddr -= 11
            del self.memory[block_program]
            self.log("Successfully freed memory", component="Memory")
            self.kcall_dump_map[what_is_freeing] = f"{what_is_freeing}-{self.listMemoryUsed()} [ FREED ] ({current_boot_ms_time}MS)\n"
            self.updMemView()
        except Exception as e:
            self.getError("MemoryAccessViolation", isFatal=True, what_failed=f"freeMemory() whilst freeing {what_is_freeing}", basic_information=f"Segfault whilst freeing {what_is_freeing}")
            self.log(isErr=True, msg=f"(MEMORY ACCESS VIOLATION) FATAL: SEGMENTATION FAULT: OUT OF RANGE: Memory could not be read. (whilst clearing program {what_is_freeing}'s memory)", component="Memory")
            print("XenonOS cannot continue due to a fatal error. See XenonOS/OS files/log.rf for more information.")
            exit()
    def editMemory(self, addr, what):
        if self.listMemoryUsed() > self.memorySizeMax:
            self.log(isErr=True, msg="Out of memory!", component="Memory")
            print("Out of memory.")
            self.getError("OutOfMemoryError", what_failed="editMemory()", isFatal=True, basic_information="Out of memory!")
        self.memory[addr] = what
        self.log(f"Changed data at raw address {self.memory.index(what) + 1}", component="Memory")
        self.log(f"{Teknikality.numbertools.cap(round(self.listMemoryUsed() / self.memorySizeMax * 100, 2))}% of memory used.", component="Memory")
    def writeToMemory(self, what, what_is_it="NOT PROVIDED", reserve=False):
        if self.listMemoryUsed() > self.memorySizeMax:
            self.log(isErr=True, msg="Out of memory!", component="Memory")
            print("Out of memory.")
            self.getError("OutOfMemoryError", what_failed="writeToMemory()", isFatal=True, basic_information="Out of memory!")
        beforeWrite = self.listMemoryUsed()
        self.memory.append(what)
        self.program_alloc[what_is_it] = len(self.memory) - 1
        if not reserve:
          self.log(f"Wrote to memory at addresses {hex(beforeWrite)}-{hex(self.listMemoryUsed())}", component="Memory")
        else:
            self.log(f"Reserved memory at addresses {hex(beforeWrite)}-{hex(self.listMemoryUsed())} for {what_is_it}", component="Memory")
        self.log(f"{Teknikality.numbertools.cap(round(self.listMemoryUsed() / self.memorySizeMax * 100, 2))}% of memory used.", component="Memory")
    def log(self, msg, isErr=False, warn=False, component="UNKNOWN"):
       if not self.loggingenabled:
           return
       try:
        current_boot_ms_time = (time.time() - boot_time)
        if isErr:
            self.appendTo(dir="OS files/log.rf", data=f"[{round(current_boot_ms_time, 4):<7}]  [ FAILED ]  {component}: {msg}")
            if self.verbose_mode:
                print(f"[{Teknikality.colors.WHITE}{round(current_boot_ms_time, 4):<7}]  [ {Teknikality.colors.RED}FAILED{Teknikality.colors.RESET} ]{Teknikality.colors.WHITE}  {component}: {msg}")
            logs.append(f"[{round(current_boot_ms_time, 4):<7}]  [ FAILED ] {component}: {msg}")
        elif warn:
            self.appendTo(dir="OS files/log.rf", data=f"[{round(current_boot_ms_time, 4):<7}]  [  WARN  ] {component}: {msg}")
            if self.verbose_mode:
                print(f"[{Teknikality.colors.WHITE}{round(current_boot_ms_time, 4):<7}]  [  {Teknikality.colors.YELLOW}WARN{Teknikality.colors.RESET}  ]{Teknikality.colors.WHITE}  {component}: {msg}")
            logs.append(f"[{round(current_boot_ms_time, 4):<7}]  [  WARN  ] {component}: {msg}")
        else:
            self.appendTo(dir="OS files/log.rf", data=f"[{round(current_boot_ms_time, 4):<7}]   [   OK   ] {component}: {msg}")
            if self.verbose_mode:
                print(f"[{Teknikality.colors.WHITE}{round(current_boot_ms_time, 4):<7}]        [ {Teknikality.colors.GREEN}  OK {Teknikality.colors.RESET}  ]{Teknikality.colors.WHITE}  {component}: {msg}")
            logs.append(f"[{round(current_boot_ms_time, 4):<7}]   [   OK   ] {component}: {msg}")
       except FileNotFoundError:
           print(f"log.rf could not be found. Failed to log: {msg} [IsErr={isErr}]")
           self.loggingenabled = False
           print("Logging disabled.")
           return
    def appendTo(self, dir, data):
        try:
          with open(f"C:/python/XenonOS/{self.base_drive}/{dir}", "a") as f:
            f.write(data + "\n")   
        except FileNotFoundError:
           print(f"No such file/directory: {dir}")
           if "log.rf" in dir:
                print("Logging has been disabled because of an error that can cause recursion.")  
                self.loggingenabled = False
                return 
           if self.loggingenabled:
             self.log(isErr=True, msg=f"No such file/directory: {dir}", component="FS")
          
    def get_traceBack(self):
        return self.trace_back           
    def writeTo(self, dir, data):
        try:
          with open(f"C:/python/XenonOS/{self.base_drive}/{dir}", "w") as f:
            f.write(data)
        except FileNotFoundError:
           print(f"No such file/directory: {dir}")
           self.log(isErr=True, msg=f"No such file/directory: {dir}", component="Memory")
    def run(self, dir):
     content_len = os.path.getsize(f"C:/python/XenonOS/{self.base_drive}/{dir}")
     if int(self.listMemoryUsed()) + int(content_len) > self.memorySizeMax:
        self.log(f"MemoryOverflowProtection: Cannot proceed running {dir}: Not enough memory space.", isErr=True, component="Execve")
        self.getError("Not enough memory", what_failed="run()", isFatal=True, basic_information=f"Out Of Memory! {self.listMemoryUsed()}/{self.memorySizeMax}B")
        exit()
     ext = os.path.splitext(str(dir))[1].lstrip('.').lower()
     pre_X = (ext == 'pex')
     current_boot_ms_time = int((time.time() - boot_time) * 1000)
     if self.listMemoryUsed() / self.memorySizeMax * 100 > 90:
         self.log(warn=True, msg=f"MemoryWarning: More than 90% of memory is in use (needing to run program {dir}).", component="Execve")
     try:
      self.enabled = False
      with open(f"C:/python/XenonOS/{self.base_drive}/{dir}", "r", encoding="utf-8") as f:
        d = f.read()
        before_alloc = self.listMemoryUsed()
        self.kcall_stack[str(self.kcall_count)] = {
            "SUBJECT-OF": self.kcall_file_stack[-1],
            "RAM-SIZE-BEFORE-ALLOCATION": before_alloc,
            "FILE-NAME": dir,
            "IS-GLOBAL": False,
            "IS-PREX-ENVIRO": pre_X,
            "FILE-SIZE": content_len
        }
        self.kcall_file_stack.append(dir)
        self.writeToMemory(what=d, reserve=True, what_is_it=dir)
        self.kcall_dump_map[dir] = f"{hex(before_alloc)}+{hex(self.listMemoryUsed())}  [{dir}] ({current_boot_ms_time}MS)\n"
        self.log(f"{dir} will take an estimated {((len(d) / 1000 + self.memory.index(d) / 1000 + self.listMemoryUsed() / 1000) - self.cpu_hz) + round(random.uniform(0, 1.8), 1)} seconds to run.", component="Execve")
        self.log(f"Allocated {len(d)}B ({len(d) / 1000}KB) ({round(len(d) / self.memorySizeMax * 100, 2)}% Of memory) For {dir} (Adresses {hex(before_alloc)}-{hex(self.listMemoryUsed())})", component="Execve")
        self.program_map[dir] = {"byte_size": f"{len(d)}B", "address_filled": f"{hex(before_alloc)}-{hex(self.listMemoryUsed())}", "file_origin": dir}
        time.sleep(Teknikality.numtools.cap((len(d) / 1000 + self.memory.index(d) / 1000 + self.listMemoryUsed() / 100) - self.cpu_hz, max=5, min=0)) 
        self.cpu_hz += len(d) / 1000 + self.memory.index(d) / 1000 + self.listMemoryUsed() / 1000
        self.cpu_hz = Teknikality.numbertools.cap(self.cpu_hz, min=1, max=self.base_working_clock if len(d) < 100 else self.max_clock)
        self.cpu_hz = round(self.cpu_hz, 1) 
        workload = len(d) / 200  # ~5 for a 1000B program
        workload = Teknikality.numtools.cap(workload, min=0, max=5)
        randomcoolingeffect = random.randint(-5, 5)
        self.cpu_temp += workload * self.cpu_hz + randomcoolingeffect
        self.cpu_temp -= self.fan_speed / 1000
        self.fan_speed = workload * self.cpu_hz * 200
        self.fan_speed = Teknikality.numtools.cap(self.fan_speed, min=0, max=4000)
        if self.fan_speed > 3000:
            self.log(warn=True, msg=f"High fan speed! ({self.fan_speed})", component="Execve")
        self.voltage = self.base_power_draw + (workload * self.cpu_hz * 2)
        self.voltage = Teknikality.numtools.cap(self.voltage, min=0, max=60)
        
        if self.cpu_temp > self.max_before_throttle:  
            self.log("Power@CPU@thermalControl: CPU is throttling.", warn=True, component="Execve")
            self.cpu_hz = 1
            if self.cpu_temp > self.max_before_thermal_shutdown:
                self.log(isErr=True, msg="Kernel-Power@CPUunsafeShutdown@thermalControl: A thermal shutdown has occoured.", component="Execve") 
                Teknikality.clearscreen()  
                self.max_before_thermal_shutdown = 300 # Get rid of recursion
                self.getError("ThermalShutdown", what_failed="ThermalShutdown@run()", isFatal=True, basic_information=f"CPU#{random.randint(0, 4)} reports {round(self.cpu_temp)}C!") 
                exit()
        if self.cpu_temp > 200:
            exit()
        self.log(f"CPU: Working at {self.cpu_hz}Hz, Temp:{round(self.cpu_temp, 1)}C, FanSpeed:{round(self.fan_speed)}RPM, Power Draw:{self.voltage}W", component="Execve")
        if self.listMemoryUsed() > self.memorySizeMax:
            self.log(isErr=True, msg="Out of memory!", component="Execve")
            print("Out of memory.")
            self.getError("OutOfMemoryError", what_failed=f"run() on {dir}", isFatal=True, basic_information=f"Out Of memory!")
        if self.listMemoryUsed() / self.memorySizeMax * 100 > 90:
           self.log(warn=True, msg=f"MemoryWarning: More than 90% of memory is in use (after running {dir}).", component="Execve")
        self.trace_back += f"{current_boot_ms_time}MS at run():{dir}, \n"
        self.enabled = True
        self.kcall_count += 1
        self.log(f"kernel-kcall: invoke {dir} ({dir}: CHECKSUMS COMPLETE)", component="kcall")
        exec(d)
     except Exception as e:
        print(e)
        err = type(e).__name__
        err = str(err)
        self.getError(err, what_failed=dir, basic_information=f"Fatal exception in {dir}")
    
  
    def boot(self, skip_flag=False):
        Teknikality.clearscreen()
        self.loggingenabled = False
        firstrun = False
        base_path="C:/python/XenonOS"
        folder_names = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
        if self.base_drive not in folder_names:
            Teknikality.clearscreen()
            print(f"Disc {self.base_drive} does not exist or does not contain a OS.")
            if "liveCD" in folder_names:
                print("Boot from CD?")
                if input().lower() != "n":
                    print("Setting base drive to liveCD and rebooting.")
                    self.base_drive = "liveCD"
                    Teknikality.clearscreen()
                    time.sleep(2)
                    try:
                      self.run("inboot.bin")
                    except:
                        print("There is no bootloader in liveCD. Insert bootable media and restart. (inboot.BIN missing!)")
                        exit()
                else:
                    print("Reboot and select proper boot device.")
                    exit()
            exit()
        self.log("Starting XenonOS...", component="Boot")
        Teknikality.clearscreen()
        try:
          self.run("boot/boot.pex")
        except Exception:
            print("Bootloader at dd1/boot/boot.pex is corrupt or missing.")
            self.log("FATAL: Bootloader at dd1/boot/boot.pex is corrupt or missing.", isErr=True, component="Boot")
            self.getError("BootError", what_failed="boot()@run()->boot.pex:MISSING_OR_CORRUPT", isFatal=True, isBootIssue=True, basic_information="Failed to mount bootloader!")
    def passive_cooling(self):
      while True:
       try:
        if self.enabled:
         if self.cpu_temp > 21:
          self.cpu_temp -= self.fan_speed / 1000 - (self.cpu_hz / 10)
         self.voltage = self.base_power_draw + (1 * self.cpu_hz * 2)
         self.cpu_hz = 1.5
         self.fan_speed = 1 * self.cpu_hz * 200
         time.sleep(1) # So it doesn't cool it like its being smothered in LN
       except Exception:
           self.getError(error="what", isFatal=True, what_failed="UNKNOWN", basic_information="???")

osm = osmain()
threading.Thread(target=osm.passive_cooling, daemon=True).start()
if firstrun == True:
    simulation_start()
    firstrun = False   
else:
   osm.boot()

    