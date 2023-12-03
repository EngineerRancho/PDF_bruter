from pikepdf import Pdf
import re

# def crack_password(digits, filename, pattern):
#     n = 1
#     n_max = 9999999999999999999 % (10**digits)
#     while n < n_max + 1:
#         pn = str(n).zfill(digits)
#         if pattern is None or re.match(pattern, pn):
#             try:
#                 Pdf.open(filename_or_stream=filename, password=pn)
#                 print("Password is " + pn)
#                 return True
#             except:
#                 # incorrect password
#                 pass
#         n += 1
#     return False


def crack_password(digits, filename, pattern):
    n = 0  # Start from 0
    n_max = 10 ** digits
    while n < n_max:
        pn = str(n).zfill(digits)
        if pattern is None or re.match(pattern, pn):
            try:
                Pdf.open(filename_or_stream=filename, password=pn)
                print("Password is " + pn)
                return True
            except:
                # incorrect password
                pass
        n += 1
    return False

# User Manual Inputs
print("                                           ")
print("                     `.-//:://:...         ")       
print("                 `/ymNNNNMNNNNNNNNmo/-`    ")       
print("                :dNMMMMMMMMMMMMMMMMMNNh    ")       
print("               /NMMMMMMMMMMMMMMMMMMMMMN.   ")       
print("              -mMMMMMMMMMMMNNMMMMMMMMMh`   ")       
print("              hMMMNmhsyyysoooshdNMMMMd.    ")       
print("              dMMNy+:--.....--:/oyNMMNo    ")       
print("              sMMm/:-.........--:/hMMMh    ")       
print("              .Nm+/+/::.````-::/++omMM+    ")       
print("               ys:yddddy:``-sddddhs+Nd`    ")       
print("              `/:-/ssd/::..::/ydsy/:d/`    ")       
print("              --...---..-..--.-/-:--//:    ")       
print("              --..`````....--.```..-:/:    ")       
print("              -:..`````.-`.:-````..-:+.    ")       
print("               ``.````.----:-.```..---     ")       
print("                 ```.-::---::::...-.       ")       
print("                 ````.-:--:-::-....`       ")       
print("                  `.....-::-....--`        ")       
print("                  ------------::::-        ")       
print("                 ./--:::///+////://        ")       
print("                  .---------::::::`        ")       
print("                    `....-------.`         ")       
print("                      `.....-..`           ")       
print("                       --.`....            ")       
print("                      .sdhhyhmy.           ")       
print("                        -hMmNo`            ")       
print("                         `dNy              ")       
print("                          hms              ")       
print("                         -NmN.   Pt.Gaurav ")       
print("                         oNdMs    Sharma   ")       
print("                         ydhMm`            ")       
print("                        `ddhNM-            ")       
print("                        .ddddM/        .+` ")   

print("")
filename = input("Enter the full path of the PDF file: ")
min_digits = int(input("Enter minimum number of digits in the password: "))
max_digits = int(input("Enter maximum number of digits in the password: "))
regex_pattern = input("Enter a regex pattern to match passwords (optional): ")

# Check and fix min and max digit values
if max_digits < min_digits:
    max_digits = min_digits

# Compile regex pattern if provided
pattern = None if not regex_pattern else re.compile(regex_pattern)

# Iterate over range of digits to crack password
found_password = False
print("Cracking. Please wait...")
for digits in range(min_digits, max_digits + 1):
    print(f"Trying to crack using {digits} digit passwords")
    found_password = crack_password(digits, filename, pattern)
    if found_password:
        break

if not found_password:
    print("Could not crack the password")