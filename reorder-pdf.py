#!/bin/env python

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from optparse import OptionParser

# Parse inputs
parser = OptionParser()
parser.add_option("-i", "--infile", dest="infile",
                  help="Input PDF file", metavar="FILE")
parser.add_option("-o", "--outfile", dest="outfile",
                  help="Output PDF file (will be created or overwritten)", metavar = "FILE")

(options, args) = parser.parse_args()

if not options.infile or not options.outfile:
    parser.error("Input and output filenames required via options `-i FILENAME` and `-o FILENAME`.")

# Prepare input file for reading
input_pdf = PdfFileReader(options.infile)

# Get number of pages in PDF
total_pages = input_pdf.getNumPages()

# Prep output file
writefile = open(options.outfile, "wb")
output_pdf = PdfFileWriter()

# Store even and odd pages
evens = []
odds = []

# Read in pages from input PDF and store them into even and odd piles
for pagenr in range(total_pages):
    if pagenr < total_pages/2:
        evens.append(input_pdf.getPage(pagenr))
    else:
        odds.append(input_pdf.getPage(pagenr))

evenct = 0
oddct = 0

# Loop over full page number and compile into correct order
for pagenr in range(total_pages):
    if pagenr%2==1:
        output_pdf.addPage(odds[oddct])
        oddct+=1
    else:
        output_pdf.addPage(evens[evenct])
        evenct+=1

# Write and close output file
output_pdf.write(writefile)
writefile.close()
