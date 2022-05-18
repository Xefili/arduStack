import sys 
import colorama as c


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


class keyword():
    i = 1
    def compile(file, output):
        currentLine = file.read()
        l = str(currentLine).split()
        print(l)
        for i in range(len(l)):
            if l[i] == "setup":
                output.write("void setup(){\n")
            elif l[i] == "end":
                output.write("}\n")
            elif l[i] == "setPin":
                output.write(f"pinMode({l[i+1]}, {l[i+2]});\n")

# Digitals

            elif l[i] == "d_write":
                if l[i+1] == 'on':
                    output.write(f"digitalWrite({l[i+2]}, HIGH);\n")
                if l[i+1] == 'off':
                    output.write(f"digitalWrite({l[i+2]}, LOW);\n")

# Analogs

            elif l[i] == "a_write":
                output.write(f"analogWrite({l[i+1]}, {l[i+2]});\n")
            elif l[i] == "a_read":
                output.write(f"analogRead({l[i+1]});\n")
            elif l[i] == "tone":
                output.write(f"tone({l[i+1]}, {l[i+2]});\n")
            elif l[i] == "noTone":
                output.write(f"noTone({l[i+1]});\n")
            elif l[i] == "loop":
                output.write("void loop(){\n")

# Variable Types

            elif l[i] == "int":
                output.write(f"int {l[i+1]} = {l[i+2]};\n")
            elif l[i] == "float":
                output.write(f"float {l[i+1]} = {l[i+2]};\n")
            elif l[i] == "long":
                output.write(f"long {l[i+1]} = {l[i+2]};\n")
            elif l[i] == "byte":
                output.write(f"byte {l[i+1]} = {l[i+2]};\n")



keyword.compile(file, output)


file.close()
output.close()
exit(0)