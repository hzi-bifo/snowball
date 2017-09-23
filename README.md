# **Snowball gene assembler**

ALGORITHM DESCRIPTION

http://bioinformatics.oxfordjournals.org/content/32/17/i649.full.pdf

LICENSE

GNU General Public License version 3 (http://www.gnu.org/licenses/).

(Note that python modules in the `algbioi.com` package have a less restrictive license.)

SYSTEM REQUIREMENTS
* Linux or OS X (tested on: OS X 10.10.5, Ubuntu 14.10, Debian 7.8)
* Python 2.7, biopython (tested with biopython 1.64)
* HMMER 3 (http://hmmer.janelia.org, tested with HMMER 3.0; for latest Pfam 30, you will need HMMER v3.1b2)

MINIMUM HARDWARE REQUIREMENTS
* 1 CPU (but use as many as you can)
* 4GB RAM (typically 1-4GB per CPU)

DATABASE
* Pfam profile HMMs can be downloaded from: http://pfam.xfam.org
* Tested with Pfam v27, the decompressed `Pfam-A.hmm` file
* Amphora 2 profile HMMs can be downloaded from: https://github.com/martinwu/AMPHORA2/tree/master/Marker
* The program was tested with the following Amphora 2 profile HMMs: dnaG, infC, pgk, rpoB, tsf, frr, nusA, pyrG, rpmA, smpB, rpsC, rpsI, rpsK, rpsS, rpsB, rpsE, rpsJ, rpsM, rplA, rplB, rplC, rplD, rplE, rplF, rplK, rplL, rplM, rplN, rplP, rplS and rplT.
* To use several profile HMMs, please concatenate all respective HMM files and run Snowball with a single HMM file.
* To get the latest Pfam profile HMMs version 30.0, issue the following command from the command line: 
`wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam30.0/Pfam-A.hmm.gz`
Note that you will also need to install HMMER v3.1b2 (http://hmmer.org)

INSTALLATION
* Install Python, biopython, HMMER (if not already available)
* Download the latest version of _Snowball_ from: https://github.com/algbioi/snowball/releases (click on `snowball_1_2.tar.gz`)
* Decompress the downloaded file (e.g. `tar -zxvf snowball_1_2.tar.gz`)
* Let `$INSTALL_DIR` be the directory that contains the `algbioi` directory that you just decompressed. 
* Set the `PYTHONPATH` variable:
 
`export PYTHONPATH=$INSTALL_DIR:$PYTHONPATH`

BENCHMARK DATASETS

https://figshare.com/articles/Snowball_benchmark_datasets/3124909 (10.6084/m9.figshare.3124909)

RUNNING _Snowball_

* Run _Snowball_ with `-h` to learn all available parameters: 

`python $INSTALL_DIR/algbioi/ga/run.py -h`

* For instance, you could run _Snowball_ with parameters: 

`python $INSTALL_DIR/algbioi/ga/run.py -f pair1.fq.gz -s pair2.fq.gz -m Pfam-A.hmm -i 225`

Note

* Although this software has been thoroughly tested, please report any issue, by creating an _Issue_ on the download site. 
* The site from which this repository was forked is: https://github.com/algbioi/snowball/wiki

Known Issues
* Version <= 1.2: All the input reads has to be of the same size. We recommend to trim the reads to the same size and filter out short reads. 
* Version <= 1.2: The input reads has to be in an older Illumina format, where the name of the read-ends of a paired-end read differ only in the last character (i.e. “1” and “2”), e.g. a paired-end read named “read_name” has two read-ends: “read_name\1” and “read_name\2”. In the case, your reads follow a different convention, please rename the reads.
* Version <= 1.1: It is necessary to provide absolute paths or paths relative to the home directory (e.g. ~/Documents/fq_1.gz) version 1.2 does not have this limitation.
