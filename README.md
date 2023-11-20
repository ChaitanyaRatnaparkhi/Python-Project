# Python-Project
Chaitanya Ratnaparkhi cratnapa@stevens.edu

## Github URL

https://github.com/ChaitanyaRatnaparkhi/Python-Project



## Program Testing Script

### Overview

This Python script (`test.py`) is designed to evaluate the functionality of three programs: `wc.py`, `gron.py`, and `cc.py`. The script compares the output of these programs against expected output based on predefined test cases.

### 1. `wc.py` - Word Count Program

#### Purpose:
The `wc.py` program is designed to count the number of lines, words, and characters in a given text file. It provides basic statistics about the contents of a file.

#### Functionality:
- Counts the number of lines in the input text.
- Counts the number of words in the input text.
- Counts the number of characters in the input text.

#### Test Cases:
The test cases for `wc.py` include scenarios with different types of input files, ranging from small to large, to validate the accuracy of the word count, line count, and character count.

### 2. `gron.py` - JSON to GRON Converter

#### Purpose:
The `gron.py` program is a JSON to GRON converter. It transforms JSON data into a human-readable format called GRON, useful for debugging and analyzing JSON structures.

#### Functionality:
- Converts JSON input into GRON format.
- Provides a structured and readable representation of JSON data.

#### Test Cases:
Test cases for `gron.py` involve various JSON files with different structures to ensure correct conversion to GRON format. Cases may include nested structures and arrays.

### 3. `cc.py` - Caesar Cipher Encryption and Decryption

#### Purpose:
The `cc.py` program is designed for Caesar cipher encryption and decryption. It's a simple cryptographic technique where each letter in the plaintext is shifted a certain number of places down the alphabet.

#### Functionality:
- Encrypts a given plaintext using the Caesar cipher.
- Decrypts a given ciphertext to retrieve the original plaintext.

#### Test Cases:
Test cases for `cc.py` cover scenarios with different encryption keys, plaintexts, and ciphertexts. Cases may include both encryption and decryption to validate the bidirectional functionality of the Caesar cipher implementation.

### Prerequisites

- Python 3.x installed
- Programs (`wc.py`, `gron.py`, `cc.py`) available in the `prog` directory

### Running the Tests

1. **Prepare Test Files:**
   - For `wc.py`: Files starting with "wc" and ending with "in" or "out"
   - For `gron.py`: Files starting with "gron" and ending with "in" or "out"
   - For `cc.py`: Files starting with "cc" and ending with "in" or "out"

2. **Execute the Test Script:**

   ```bash
   python test.py


### Extensions: 

1. More advanced gron: control the base-object name

    - Implemented --obj flag to change the base object of the json.
    
    ```
        python prog/gron.py --obj o eg.json

    ```

    OUTPUT:
    
    ```

        o = {}
        o.menu = {{}}
        o.menu.id = "file"
        o.menu.value = "File"
        o.menu.popup = {{}}
        o.menu.popup.menuitem = []
        o.menu.popup.menuitem[0] = {}
        o.menu.popup.menuitem[0].value = "New"
        o.menu.popup.menuitem[0].onclick = "CreateNewDoc()"
        o.menu.popup.menuitem[1] = {}
        o.menu.popup.menuitem[1].value = "Open"
        o.menu.popup.menuitem[1].onclick = "OpenDoc()"
        o.menu.popup.menuitem[2] = {}
        o.menu.popup.menuitem[2].value = "Close"
        o.menu.popup.menuitem[2].onclick = "CloseDoc()"

    ```
2. Extension: More advanced wc: flags to control output
   - Implemented -l flag to count the number of lines in a file.
   - Implemented -lc flag to count the number of lines and characters in a file.
   - Implemented -w flag to count the number of words in a file.
   - Implemented -lcw flag to count the number of lines, words and characters in a file.
   - Implemented -c flag to count the number of characters in a file.
    
    ```
    python prog/wc.py -l  eg.json
    output : 12 eg.json

    python prog/wc.py -lc  eg.json
    output :  12     262 eg.json
    
    python prog/wc.py -w  eg.json
    output : 26 eg.json
    
    python prog/wc.py -lcw  eg.json
    output : 12      26     262 eg.json

    python prog/wc.py -c  eg.json
    output : 262 eg.json
