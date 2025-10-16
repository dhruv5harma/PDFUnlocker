#!/usr/bin/env python3
# author: github/dhruv5harma
"""Remove password from a PDF (requires the password)."""

import argparse
import sys
import os
import pikepdf

def unlock_pdf(input_path, password, output_path=None):
    # Use default output name if not provided
    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_unlocked.pdf"

    try:
        with pikepdf.open(input_path, password=password) as pdf:
            pdf.save(output_path)
        print(f"PDF unlocked and saved to: {output_path}")
        return 0
    except FileNotFoundError:
        print(f"ERROR: File not found: {input_path}", file=sys.stderr)
        return 3
    except pikepdf.PasswordError:
        print("ERROR: Incorrect password or unable to open PDF.", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

def main():
    parser = argparse.ArgumentParser(description="Remove password from a PDF (requires the correct password).")
    parser.add_argument("-i", "--input", required=True, help="Path to the encrypted PDF file")
    parser.add_argument("-p", "--pass", dest="password", required=True, help="Password for the PDF")
    parser.add_argument("-o", "--output", help="Output PDF filename (optional)")

    args = parser.parse_args()
    sys.exit(unlock_pdf(args.input, args.password, args.output))

if __name__ == "__main__":
    main()
