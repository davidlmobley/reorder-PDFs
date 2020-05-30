# reorder-PDFs
Reorder pages in a PDF which is scanned so that even pages occur first and odds afterwards. Makes pages be in correct order.

Basically a one-off script to fix a specific problem we had after scanning some large PDF documents.

Assumes first half of pages are even numbered (starting with 0) and second half are odd.

## Requirements:

- PyPDF2

## Usage:

`python -i infile.pdf -o outfile.pdf`

## Limitations:

Currently assumes there are same number of even and odd pages; will presumably break if there are not.
