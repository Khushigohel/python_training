'''Create a Python script that encrypts and decrypts text files using a simple substitution 
cipher. 
● Implement functions for encryption and decryption using a basic substitution cipher 
algorithm (e.g., shifting each letter by a fixed number of positions in the alphabet).
● Prompt users to enter a filename and choose whether to encrypt or decrypt the file.
● Ensure the script handles cases where the file does not exist or cannot be opened for 
reading/writing.'''

class File_Encryption:
    
    def encryption_file(self, text, key):
        result = ''
        for char in text:
            if char.isalpha():
                shift = ord('A') if char.isupper() else ord('a')   # ord is convert alohabet into the ascii value
                result += chr((ord(char) - shift + key) % 26 + shift)   # it is main cipher logic
            else:
                result += char
        return result
    
    def decryption_file(self, text, key):
        return self.encryption_file(text, -key)
    
    def main(self):
        import os
        os.chdir("Final_Assignments/FileEncryption_task")

        file_name = input("Enter the File Name: ")
        
        try:
            with open(file_name, 'r') as file_read:
                Data = file_read.read()
        except FileNotFoundError:
            print("\nError: File Not Found..")
            return
        except IOError:
            print("\nError: Unable to open file..")
            return
        
        print("\n1. Encrypt File")
        print("2. Decrypt File")
        
        choice = int(input("Enter choice: "))
        key = int(input("Enetr the encryption key : "))
        
        if choice == 1:
            result = self.encryption_file(Data, key)
            out_file = "encrypted_" + file_name
        elif choice == 2:
            result = self.decryption_file(Data, key)
            out_file = "decrypted_" + file_name
        else:
            print("\nInvalid Choice...")
            return
        
        try:
            with open(out_file, "w") as file:
                file.write(result)
            print(f"\nOperation successful! Output saved to '{out_file}'")
        except IOError:
            print("\nError: Unable to write to file!")


obj = File_Encryption()
obj.main()
