# QueryPathways
# Language: Python
# Input: TXT
# Output: TXT
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin to query reactions from the PathwayTools
database (Karp et al, 2015) for taxa and/or metabolites.  It returns pathways in TXT format.

The input is a parameters TXT file of tab-delimited keyword-value pairs:
pathways: TXT file of pathways from PathwayTools
query: TXT file of query

The query input file should contain one or two lines.  A simple lookup of a taxa or
metabolite would be one line.  To query all reactions for a specific pair of taxa, taxa/metabolite,
or metabolites, provide both on separate lines.

Note: The example folder contains this query file and the parameters TXT file,
but not the pathways file as this contains information from the PathwayTools database.

However if you have PathwayTools installed, the "PathwayTools" plugin
(http://github.com/PathwayTools) will produce this TXT file for the pathways.
