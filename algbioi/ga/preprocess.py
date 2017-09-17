#!/usr/bin/env python

"""
    Copyright (C) 2016  Ivan Gregor

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    PE to SE Version: experimental
"""

import argparse
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

from algbioi.com import fq
from algbioi.ga.run import normPath


def _main():
    """
        PE to SE
    """
    # Command line parameters
    parser = argparse.ArgumentParser(
    description = 'Transform paired-end reads or single-end reads to an input for the Snowball assembler, s.t. the snowball assembler'
                  ' runs as if the input reads were single-end (set the insert size equal to the read length!).',
    epilog='GNU General Public License version 3 (http://www.gnu.org/licenses/).')

    parser.add_argument('-f1', '--fq-1-file-in', nargs=1, type=file, required=True,
                    help='FASTQ 1 file path containing first read-ends of Illumina paired-end reads or single-end reads.',
                    metavar='pair1_in.fq.gz',
                    dest='fq1File')

    parser.add_argument('-f2', '--fq-2-file-in', nargs=1, type=file, required=False,
                    help='FASTQ 2 file path containing second read-ends of Illumina paired-end reads '
                         '(mandatory parameter only for paired-end reads).',
                    metavar='pair2_in.fq.gz',
                    dest='fq2File')

    parser.add_argument('-o1', '--fq-1-file-out', nargs=1, type=str, required=True,
                    help='FASTQ 1 file path - input for Snowball to run as if the input was single-end reads.',
                    metavar='pair1_out.fq.gz',
                    dest='fq1FileOut')

    parser.add_argument('-o2', '--fq-2-file-out', nargs=1, type=str, required=True,
                    help='FASTQ 2 file path - input for Snowball to run as if the input was single-end reads.',
                    metavar='pair2_out.fq.gz',
                    dest='fq2FileOut')

    args = parser.parse_args()


    # reading arguments
    fq1File = normPath(args.fq1File[0].name)
    if args.fq2File:
        fq2File = normPath(args.fq2File[0].name)
    else:
        fq2File = None
    fq1FileOut = normPath(args.fq1FileOut[0])
    fq2FileOut = normPath(args.fq2FileOut[0])
    #
    to_se(fq1File, fq2File, fq1FileOut, fq2FileOut)


def to_se(fq1_in, fq2_in, out_fq1, out_fq2):

    out_fq1 = fq.WriteFq(out_fq1)
    out_fq2 = fq.WriteFq(out_fq2)
    file_counter = 0
    if fq2_in is None:
        inFQList = [fq1_in]
    else:
        inFQList = [fq1_in, fq2_in]

    for fq_in in inFQList:
        file_counter += 1
        for name1, dna1, p1, qs1 in fq.ReadFqGen(fq_in):
            dna2 = str(Seq(dna1, generic_dna).reverse_complement())
            qs2 = qs1[::-1]
            name1 = name1[:-2] + '_%s/1' % (file_counter)
            name2 = name1[:-1] + '2'
            out_fq1.writeFqEntry(name1, dna1, qs1)
            out_fq2.writeFqEntry(name2, dna2, qs2)

    out_fq1.close()
    out_fq2.close()


if __name__ == "__main__":
    _main()

