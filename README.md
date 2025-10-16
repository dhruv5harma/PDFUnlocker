# 📄 PDF Password Remover

A simple Python script to **remove password protection from a PDF** using [`pikepdf`](https://pikepdf.readthedocs.io/).  
🔐 **You must know the PDF password** — this tool does **not** crack or bypass encryption.

## Features

* Remove password from encrypted PDFs
* Requires correct password (does not crack)
* Custom output filename or auto-generate
* Uses `pikepdf` (QPDF-based, reliable)

## Requirements

* Python 3.7+
* [`pikepdf`](https://pypi.org/project/pikepdf/)

Install with pip:

```bash
pip install pikepdf
```

# Usage & Options — PDF Password Remover

Below are the **command-line options**, **detailed usage**, and **examples**. 

The script this documents is `remove_pdf_password.py` which accepts `-i/--input`, `-p/--pass`, and `-o/--output`.

## Usage

```bash
python remove_pdf_password.py -i <input.pdf> -p <password> [-o <output.pdf>]
```
