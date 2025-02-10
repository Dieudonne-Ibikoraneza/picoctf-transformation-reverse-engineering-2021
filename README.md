# 🛠 Reverse Engineering > Transformation > PicoCTF 2021
## 🔍 Challenge Description
We are given an encoded flag stored in an `enc` file. The encoding process combines two characters into a single Unicode character using bitwise operations. Our task is to reverse this process and retrieve the original flag.

## 🚀 Steps to Solve
1. **Download** the `enc` file from the challenge.
2. **Open the file** and **copy** the encoded text.
3. **Replace** the `enc_flag` variable in the **Python script** with the copied text.
4. **Run** the script to decode the flag.

## Decoding Script (transformation_reverse_engineering.py)
```python
# Paste the encoded string from the enc file here
enc_flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽" # Replace with the content of your enc file

decoded_flag = []
for c in enc_flag:
    num = ord(c)  # Get the number representation
    first = chr(num >> 8)  # Extract the first character (higher bits)
    second = chr(num & 0xFF)  # Extract the second character (lower bits)
    decoded_flag.append(first + second)

flag = ''.join(decoded_flag)
print(flag)  # Output the flag
```
## 🏃 Running the Script
Run the script using the following command:

```bash
python transformation_reverse_engineering.py
```
The flag should appear in the output in the format: picoCTF{...}

🔗 Resources
- [Python ord() and chr() functions](https://docs.python.org/3/library/functions.html#ord)
- [Bitwise operations in Python](https://wiki.python.org/moin/BitwiseOperators)
