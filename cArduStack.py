import sys 
import colorama as c
from time import sleep

args = sys.argv
print(args)


try:
    file = open(f"{args[1]}", "r", encoding="utf-8")
    output = open(f"{args[2]}", "w", encoding="utf-8")
except FileNotFoundError:
    print(f"{c.Fore.RED}File not found{c.Fore.RESET}")
    exit(-5)
finally:
    pass

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '░' * (100 - int(percent))
    print(c.Fore.RED + f"\r[{bar}] {percent:.2f}%", end="\r")
    if progress == total:
        print(c.Fore.GREEN + f"\r[{bar}] {percent:.2f}%{c.Fore.RESET}", end="\n")

class keyword():
    i = 1
    def compile(file, output):
        currentLine = file.read()
        l = str(currentLine).split()
        print(l)
        i=0
        progress_bar(i, len(l))
        for i in range(len(l)):
            sleep(0.01)
            progress_bar(i+1, len(l))
            if l[i] == "setup":
                output.write("void setup(){\n")
            elif l[i] == "end":
                output.write("}\n")
            elif l[i] == "setPin":
                output.write(f"pinMode({l[i+1]}, {l[i+2]})")
            elif l[i] == ".":
                output.write(f";\n")
            elif l[i+1] == ">":
                output.write(f"void {l[i]}" + "(){\n")
            elif l[i+1] == "|":
                output.write(f"{l[i]}()")
            elif l[i] == "#":
                output.write(f"#include <{l[i+1]}>\n")
            elif l[i] == "pause":
                output.write(f"delay({l[i+1]})")
            elif l[i] == "s_init":
                output.write(f"Serial.begin({l[i+1]})")
            elif l[i] == "s_print":
                output.write(f"Serial.print({l[i+1]})")
            elif l[i] == "s_println":
                output.write(f"Serial.println({l[i+1]})")
            elif l[i] == "for":
                output.write(f"for({l[i+1]}; {l[i+2]}; {l[i+3]})" + "{\n")
            elif l[i] == "if":
                if l[i+1] == "o":
                    output.write(f"if({l[i+2]}=={l[i+3]})" + "{\n")
                if l[i+3] == "and":
                    output.write(f"if({l[i+2]}=={l[i+3]} && {l[i+4]}=={l[i+5]})" + "{\n")
                if l[i+3] == "or":
                    output.write(f"if({l[i+2]}=={l[i+3]} || {l[i+4]}=={l[i+5]})" + "{\n")
                if l[i+1] == "x":
                    output.write(f"if({l[i+2]}!={l[i+3]})" + "{\n")
                if l[i+1] == "xand":
                    output.write(f"if({l[i+2]}!={l[i+3]} && {l[i+4]}=={l[i+5]})" + "{\n")
                if l[i+1] == "xor":
                    output.write(f"if({l[i+2]}!={l[i+3]} || {l[i+4]}=={l[i+5]})" + "{\n")
                if l[i+1] == "xxand":
                    output.write(f"if({l[i+2]}!={l[i+3]} && {l[i+4]}!={l[i+5]})" + "{\n")
                if l[i+1] == "xxor":
                    output.write(f"if({l[i+2]}!={l[i+3]} || {l[i+4]}!={l[i+5]})" + "{\n")

# Digitals

            elif l[i] == "d_write":
                if l[i+1] == 'on':
                    output.write(f"digitalWrite({l[i+2]}, HIGH)")
                if l[i+1] == 'off':
                    output.write(f"digitalWrite({l[i+2]}, LOW)")
            elif l[i] == "d_read":
                if l[i+2] == ">>":
                    output.write(f"{l[i+3]} = digitalRead({l[i+1]})")
                if l[i+2] == ".":
                    output.write("digitalRead(l[i+1]);")

# Analogs

            elif l[i] == "a_write":
                output.write(f"analogWrite({l[i+1]}, {l[i+2]})")
            elif l[i] == "a_read":
                if l[i+2] == ">>":
                    output.write(f"{l[i+3]} = analogRead({l[i+1]})")
                if l[i+2] == ".":
                    output.write(f"analogRead({l[i+1]})")
            
            elif l[i] == "tone":
                if l[i+3] == ".":
                    output.write(f"tone({l[i+1]}, {l[i+2]})")
                if l[i+3] != ".":
                    output.write(f"tone({l[i+1]}, {l[i+2]}, {l[i+3]})")
            elif l[i] == "noTone":
                output.write(f"noTone({l[i+1]})")
            elif l[i] == "loop":
                output.write("void loop(){\n")

# Variable Types

            elif l[i] == "int":
                if l[i+2] == ".":
                    output.write(f"int {l[i+1]}")
                if l[i+2] != ".":
                    output.write(f"int {l[i+1]} = {l[i+2]}")
            elif l[i] == "float":
                if l[i+2] == ".":
                    output.write(f"float {l[i+1]}")
                if l[i+2] != ".":
                    output.write(f"float {l[i+1]} = {l[i+2]}")
            elif l[i] == "long":
                if l[i+2] == ".":
                    output.write(f"long {l[i+1]}")
                if l[i+2] != ".":
                    output.write(f"long {l[i+1]} = {l[i+2]}")
            elif l[i] == "byte":
                if l[i+2] == ".":
                    output.write(f"byte {l[i+1]}")
                if l[i+2] != ".":
                    output.write(f"byte {l[i+1]} = {l[i+2]}")



keyword.compile(file, output)
print(c.Fore.GREEN + "Compiled Successfully" + c.Fore.RESET)


file.close()
output.close()
exit(0)