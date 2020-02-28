#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#
# Python Client Automatically generated with:
# https://github.com/ebi-wp/webservice-client-generator
#
# Copyright (C) 2006-2018 EMBL - European Bioinformatics Institute
# Under GNU GPL v3 License - See LICENSE for more details!
###############################################################################

from __future__ import print_function
import platform, os, sys, time
from xmltramp2 import xmltramp
from optparse import OptionParser

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
    from urllib.request import __version__ as urllib_version
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError
    from urllib2 import __version__ as urllib_version

# allow unicode(str) to be used in python 3
try:
    unicode('')
except NameError:
    unicode = str

# Base URL for service
baseUrl = u'http://www.ebi.ac.uk/Tools/services/rest/pratt'

# Set interval for checking status
pollFreq = 3
# Output level
outputLevel = 1
# Debug level
debugLevel = 0
# Number of option arguments.
numOpts = len(sys.argv)

# Usage message
usage = u'''`Usage: %prog [options...] [seqFile]'''
description = u'''\
    Pratt - Pattern Matching. An important problem in sequence analysis is to find patterns matching sets or subsets of sequences. This tool allows the user to search for patterns conserved in sets of unaligned protein sequences. The user can specify what kind of patterns should be searched for, and how many sequences should match a pattern to be reported.\
'''
epilog = u'''For further information about the PRATT web service, see
http://www.ebi.ac.uk/tools/webservices/services/pfa/pratt_rest.'''
version = u'98c6601'

# Process command-line options
parser = OptionParser(usage=usage, description=description, epilog=epilog, version=version)

# Tool specific options (Try to print all the commands automatically)

parser.add_option('--minPerc', help='Set the minimum percentage of the input sequences that should match a pattern (C%). \
\	\	\	\	If you set this to, say 80, Pratt will only report patterns matching at least 80 % of the sequences input. \
\	\	\	')
parser.add_option('--patternPosition', help='Pattern position in sequence (PP parameter)')
parser.add_option('--maxPatternLength', help='Maximum pattern length (PL parameter) allows you to set the maximum length of a pattern. \
\	\	\	\	The length of the pattern C-x(2,4)-[DE] is 1+4+1=6. \
\	\	\	\	The memory requirement of Pratt depends on L; a higher L value gives higher memory requirement.\
\	\	\	')
parser.add_option('--maxNumPatternSymbols', help='Maximum number of pattern symbols (PN parameter). Using this you can set the maximum number of symbols in a pattern. \
\	\	\	\	The pattern C-x(2,4)-[DE] has 2 symbols (C and [DE]). When PN is increased, Pratt will require more memory. \
\	\	\	')
parser.add_option('--maxNumWildcard', help='Maximum length of a widecard (x). \
\	\	\	\	Using this option  you can set the maximum length of a wildcard (PX parameter). Increasing this will increase the time used by Pratt, and also slightly the memory required. \
\	\	\	')
parser.add_option('--maxNumFlexSpaces', help='Maximum length of flexible spaces.  \
\	\	\	\	Using this option you can set the maximum number of flexible wildcards (matching a variable number of arbitrary sequence symbols) (FN parameter). Increasing this will increase the time used by Pratt. \
\	\	\	')
parser.add_option('--maxFlexibility', help='Maximum flexibility.\
\	\	\	\	You can set the maximum flexibility of a flexible wildcard (matching a variable number of arbitrary sequence symbols) (FL parameter). \
\	\	\	\	For instance x(2,4) and x(10,12) has flexibility 2, and x(10) has flexibility 0. Increasing this will increase the time used by Pratt. \
\	\	\	')
parser.add_option('--maxFlexProduct', help='Maximum flex. product.\
\	\	\	\	Using this option you can set an upper limit on the product of a flexibilities for a pattern (FP parameter). \
\	\	\	\	This is related to the memory requirements of the search, and increasing the limit, increases the memory usage. \
\	\	\	')
parser.add_option('--patternSymbolFile', help='Pattern Symbol File (BI parameter)')
parser.add_option('--numPatternSymbols', help='Number of pattern symbols used in the initial search (BN parameter).\
\	\	\	')
parser.add_option('--patternScoring', help='Pattern scoring (S parameter)')
parser.add_option('--patternGraph', help='Pattern Graph (G parameter) allows the use of an alignment or a query sequence to restrict the pattern search.')
parser.add_option('--searchGreediness', help='Using the greediness parameter (E) you can adjust the greediness of the search. Setting E to 0 (zero), the search will be exhaustive. \
\	\	\	\	Increasing E increases the greediness, and decreases the time used in the search. \
\	\	\	')
parser.add_option('--patternRefinement', help='Pattern Refinement (R parameter). \
\	\	\	\	When the R option is switched on, patterns found during the initial pattern search are input to a refinement algorithm where more ambiguous pattern symbols can be added. \
\	\	\	')
parser.add_option('--genAmbigSymbols', help='Generalise ambiguous symbols (RG parameter). \
\	\	\	\	If the RG option is switched on, then ambiguous symbols listed in the symbols file are used. \
\	\	\	\	If RG is off, only the letters needed to match the input sequences are included in the ambiguous pattern positions. \
\	\	\	')
parser.add_option('--patternFormat', help='PROSITE Pattern Format (OP parameter).\
\	\	\	\	When switched on, patterns will be output in PROSITE style (for instance C-x(2,4)-[DE]). \
\	\	\	\	When switched off, patterns are output in a simpler consensus pattern style (for instance Cxx--[DE]\
\	\	\	\	where x matches exactly one arbitrary sequence symbol and - matches zero or one arbitrary sequence symbol).\
\	\	\	')
parser.add_option('--maxNumPatterns', help='Maximum number of patterns (ON parameter) between 1 and 100.\
\	\	\	')
parser.add_option('--maxNumAlignments', help='Maximum number of alignments (OA parameter) between 1 and 100. \
\	\	\	')
parser.add_option('--printPatterns', help='Print Patterns in sequences (M parameter)\
\	\	\	\	If the M option is set, then Pratt will print out the location of the sequence segments matching each of the (maximum 52) best patterns. \
\	\	\	\	The patterns are given labels A, B,...Z,a,b,...z in order of decreasing pattern score. Each sequence is printed on a line, one character per K-tuple in the sequence. \
\	\	\	\	If pattern with label C matches the third K-tuple in a sequence C is printed out. If several patterns match in the same K-tuple, only the best will be printed. \
\	\	\	')
parser.add_option('--printingRatio', help='Printing ratio (MR parameter). sets the K value (ratio) used for printing the summary information about where in each sequence the pattern matches are found.\
\	\	\	')
parser.add_option('--printVertically', help='Print vertically (MV parameter). if set, the output is printed vertically instead of horizontally, vertical output can be better for large sequence sets.')
parser.add_option('--stype', help='Defines the type of the sequences to be aligned.')
parser.add_option('--sequence', help='The input set of up to 100 sequences can be entered directly into this form. The sequences can be in FASTA or UniProtKB/Swiss-Prot format. A partially formatted sequences are not accepted. Note that directly using data from word processors may yield unpredictable results as hidden/control characters may be present.')
parser.add_option('--ppfile', help='Pattern restriction file. \
\	\	\	\	The restriction file limits the sequence range via the start/end parameter and is in the format \'>Sequence (start, end)\'. If parameter PP is off, the restiction file will be ignored.')
# General options
parser.add_option('--email', help='e-mail address')
parser.add_option('--title', help='job title')
parser.add_option('--outfile', help='file name for results')
parser.add_option('--outformat', help='output format for results')
parser.add_option('--async', action='store_true', help='asynchronous mode')
parser.add_option('--jobid', help='job identifier')
parser.add_option('--polljob', action="store_true", help='get job result')
parser.add_option('--pollFreq', type='int', default=3, help='poll frequency in seconds (default 3s)')
parser.add_option('--status', action="store_true", help='get job status')
parser.add_option('--resultTypes', action='store_true', help='get result types')
parser.add_option('--params', action='store_true', help='list input parameters')
parser.add_option('--paramDetail', help='get details for parameter')
parser.add_option('--quiet', action='store_true', help='decrease output level')
parser.add_option('--verbose', action='store_true', help='increase output level')
parser.add_option('--baseURL', default=baseUrl, help='Base URL for service')
parser.add_option('--debugLevel', type='int', default=debugLevel, help='debug output level')

(options, args) = parser.parse_args()

# Increase output level
if options.verbose:
    outputLevel += 1

# Decrease output level
if options.quiet:
    outputLevel -= 1

# Debug level
if options.debugLevel:
    debugLevel = options.debugLevel

if options.pollFreq:
    pollFreq = options.pollFreq


# Debug print
def printDebugMessage(functionName, message, level):
    if (level <= debugLevel):
        print(u'[' + functionName + u'] ' + message, file=sys.stderr)


# User-agent for request (see RFC2616).
def getUserAgent():
    printDebugMessage(u'getUserAgent', u'Begin', 11)
    # Agent string for urllib2 library.
    urllib_agent = u'Python-urllib/%s' % urllib_version
    clientRevision = u'$Revision: 2107 $'
    clientVersion = u'0'
    if len(clientRevision) > 11:
        clientVersion = clientRevision[11:-2]
    # Prepend client specific agent string.
    user_agent = u'EBI-Sample-Client/%s (%s; Python %s; %s) %s' % (
        clientVersion, os.path.basename(__file__),
        platform.python_version(), platform.system(),
        urllib_agent
    )
    printDebugMessage(u'getUserAgent', u'user_agent: ' + user_agent, 12)
    printDebugMessage(u'getUserAgent', u'End', 11)
    return user_agent


# Wrapper for a REST (HTTP GET) request
def restRequest(url):
    printDebugMessage(u'restRequest', u'Begin', 11)
    printDebugMessage(u'restRequest', u'url: ' + url, 11)
    try:
        # Set the User-agent.
        user_agent = getUserAgent()
        http_headers = {u'User-Agent': user_agent}
        req = Request(url, None, http_headers)
        # Make the request (HTTP GET).
        reqH = urlopen(req)
        resp = reqH.read()
        contenttype = reqH.info()

        if (len(resp) > 0 and contenttype != u"image/png;charset=UTF-8"
                and contenttype != u"image/jpeg;charset=UTF-8"
                and contenttype != u"application/gzip;charset=UTF-8"):

            try:
                result = unicode(resp, u'utf-8')
            except UnicodeDecodeError:
                result = resp
        else:
            result = resp
        reqH.close()
    # Errors are indicated by HTTP status codes.
    except HTTPError as ex:
        print(xmltramp.parse(ex.read())[0][0])
        quit()
    printDebugMessage(u'restRequest', u'End', 11)
    return result


# Get input parameters list
def serviceGetParameters():
    printDebugMessage(u'serviceGetParameters', u'Begin', 1)
    requestUrl = baseUrl + u'/parameters'
    printDebugMessage(u'serviceGetParameters', u'requestUrl: ' + requestUrl, 2)
    xmlDoc = restRequest(requestUrl)
    doc = xmltramp.parse(xmlDoc)
    printDebugMessage(u'serviceGetParameters', u'End', 1)
    return doc[u'id':]


# Print list of parameters
def printGetParameters():
    printDebugMessage(u'printGetParameters', u'Begin', 1)
    idList = serviceGetParameters()
    for id_ in idList:
        print(id_)
    printDebugMessage(u'printGetParameters', u'End', 1)


# Get input parameter information
def serviceGetParameterDetails(paramName):
    printDebugMessage(u'serviceGetParameterDetails', u'Begin', 1)
    printDebugMessage(u'serviceGetParameterDetails', u'paramName: ' + paramName, 2)
    requestUrl = baseUrl + u'/parameterdetails/' + paramName
    printDebugMessage(u'serviceGetParameterDetails', u'requestUrl: ' + requestUrl, 2)
    xmlDoc = restRequest(requestUrl)
    doc = xmltramp.parse(xmlDoc)
    printDebugMessage(u'serviceGetParameterDetails', u'End', 1)
    return doc


# Print description of a parameter
def printGetParameterDetails(paramName):
    printDebugMessage(u'printGetParameterDetails', u'Begin', 1)
    doc = serviceGetParameterDetails(paramName)
    print(unicode(doc.name) + u"\t" + unicode(doc.type))
    print(doc.description)
    for value in doc.values:
        print(value.value)
        if unicode(value.defaultValue) == u'true':
            print(u'default')
        print
        print(u"\t" + unicode(value.label))
        if hasattr(value, u'properties'):
            for wsProperty in value.properties:
                print(u"\t" + unicode(wsProperty.key) + u"\t" + unicode(wsProperty.value))
    printDebugMessage(u'printGetParameterDetails', u'End', 1)


# Submit job
def serviceRun(email, title, params):
    printDebugMessage(u'serviceRun', u'Begin', 1)
    # Insert e-mail and title into params
    params[u'email'] = email
    if title:
        params[u'title'] = title
    requestUrl = baseUrl + u'/run/'
    printDebugMessage(u'serviceRun', u'requestUrl: ' + requestUrl, 2)

    # Get the data for the other options
    requestData = urlencode(params)

    printDebugMessage(u'serviceRun', u'requestData: ' + requestData, 2)
    # Errors are indicated by HTTP status codes.
    try:
        # Set the HTTP User-agent.
        user_agent = getUserAgent()
        http_headers = {u'User-Agent': user_agent}
        req = Request(requestUrl, None, http_headers)
        # Make the submission (HTTP POST).
        reqH = urlopen(req, requestData.encode(encoding=u'utf_8', errors=u'strict'))
        jobId = unicode(reqH.read(), u'utf-8')
        reqH.close()
    except HTTPError as ex:
        print(xmltramp.parse(ex.read())[0][0])
        quit()
    printDebugMessage(u'serviceRun', u'jobId: ' + jobId, 2)
    printDebugMessage(u'serviceRun', u'End', 1)
    return jobId


# Get job status
def serviceGetStatus(jobId):
    printDebugMessage(u'serviceGetStatus', u'Begin', 1)
    printDebugMessage(u'serviceGetStatus', u'jobId: ' + jobId, 2)
    requestUrl = baseUrl + u'/status/' + jobId
    printDebugMessage(u'serviceGetStatus', u'requestUrl: ' + requestUrl, 2)
    status = restRequest(requestUrl)
    printDebugMessage(u'serviceGetStatus', u'status: ' + status, 2)
    printDebugMessage(u'serviceGetStatus', u'End', 1)
    return status


# Print the status of a job
def printGetStatus(jobId):
    printDebugMessage(u'printGetStatus', u'Begin', 1)
    status = serviceGetStatus(jobId)
    print(status)
    printDebugMessage(u'printGetStatus', u'End', 1)


# Get available result types for job
def serviceGetResultTypes(jobId):
    printDebugMessage(u'serviceGetResultTypes', u'Begin', 1)
    printDebugMessage(u'serviceGetResultTypes', u'jobId: ' + jobId, 2)
    requestUrl = baseUrl + u'/resulttypes/' + jobId
    printDebugMessage(u'serviceGetResultTypes', u'requestUrl: ' + requestUrl, 2)
    xmlDoc = restRequest(requestUrl)
    doc = xmltramp.parse(xmlDoc)
    printDebugMessage(u'serviceGetResultTypes', u'End', 1)
    return doc[u'type':]


# Print list of available result types for a job.
def printGetResultTypes(jobId):
    printDebugMessage(u'printGetResultTypes', u'Begin', 1)
    resultTypeList = serviceGetResultTypes(jobId)
    for resultType in resultTypeList:
        print(resultType[u'identifier'])
        if (hasattr(resultType, u'label')):
            print(u"\t", resultType[u'label'])
        if (hasattr(resultType, u'description')):
            print(u"\t", resultType[u'description'])
        if (hasattr(resultType, u'mediaType')):
            print(u"\t", resultType[u'mediaType'])
        if (hasattr(resultType, u'fileSuffix')):
            print(u"\t", resultType[u'fileSuffix'])
    printDebugMessage(u'printGetResultTypes', u'End', 1)


# Get result
def serviceGetResult(jobId, type_):
    printDebugMessage(u'serviceGetResult', u'Begin', 1)
    printDebugMessage(u'serviceGetResult', u'jobId: ' + jobId, 2)
    printDebugMessage(u'serviceGetResult', u'type_: ' + type_, 2)
    requestUrl = baseUrl + u'/result/' + jobId + u'/' + type_
    result = restRequest(requestUrl)
    printDebugMessage(u'serviceGetResult', u'End', 1)
    return result


# Client-side poll
def clientPoll(jobId):
    printDebugMessage(u'clientPoll', u'Begin', 1)
    result = u'PENDING'
    while result == u'RUNNING' or result == u'PENDING':
        result = serviceGetStatus(jobId)
        print(result, file=sys.stderr)
        if result == u'RUNNING' or result == u'PENDING':
            time.sleep(pollFreq)
    printDebugMessage(u'clientPoll', u'End', 1)


# Get result for a jobid
# function modified by Mana to allow more than one output file written when 'outformat' is defined.
def getResult(jobId):
    printDebugMessage(u'getResult', u'Begin', 1)
    printDebugMessage(u'getResult', u'jobId: ' + jobId, 1)
    # Check status and wait if necessary
    clientPoll(jobId)
    # Get available result types
    resultTypes = serviceGetResultTypes(jobId)

    for resultType in resultTypes:
        # Derive the filename for the result
        if options.outfile:
            filename = (options.outfile + u'.' + unicode(resultType[u'identifier']) +
                        u'.' + unicode(resultType[u'fileSuffix']))
        else:
            filename = (jobId + u'.' + unicode(resultType[u'identifier']) +
                        u'.' + unicode(resultType[u'fileSuffix']))
        # Write a result file

        outformat_parm = str(options.outformat).split(',')
        for outformat_type in outformat_parm:
            outformat_type = outformat_type.replace(' ', '')

            if outformat_type == 'None':
                outformat_type = None

            if not outformat_type or outformat_type == unicode(resultType[u'identifier']):
                # Get the result
                result = serviceGetResult(jobId, unicode(resultType[u'identifier']))
                if (unicode(resultType[u'mediaType']) == u"image/png"
                        or unicode(resultType[u'mediaType']) == u"image/jpeg"
                        or unicode(resultType[u'mediaType']) == u"application/gzip"):
                    fmode = 'wb'
                else:
                    fmode = 'w'

                fh = open(filename, fmode)

                fh.write(result)
                fh.close()
                print(filename)
    printDebugMessage(u'getResult', u'End', 1)


# Read a file
def readFile(filename):
    printDebugMessage(u'readFile', u'Begin', 1)
    fh = open(filename, 'r')
    data = fh.read()
    fh.close()
    printDebugMessage(u'readFile', u'End', 1)
    return data


# No options... print help.
if numOpts < 2:
    parser.print_help()
# List parameters
elif options.params:
    printGetParameters()
# Get parameter details
elif options.paramDetail:
    printGetParameterDetails(options.paramDetail)
# Submit job
elif options.email and not options.jobid:
    params = {}
    if len(args) > 0:
        if os.access(args[0], os.R_OK):  # Read file into content
            params[u'sequence'] = readFile(args[0])
        else:  # Argument is a sequence id
            params[u'sequence'] = args[0]
    elif options.sequence:  # Specified via option
        if os.access(options.sequence, os.R_OK):  # Read file into content
            params[u'sequence'] = readFile(options.sequence)
        else:  # Argument is a sequence id
            params[u'sequence'] = options.sequence
    # Booleans need to be represented as 1/0 rather than True/False

    if options.minPerc:
            params['minPerc'] = options.minPerc
    if options.patternPosition:
            params['patternPosition'] = options.patternPosition
    if options.maxPatternLength:
            params['maxPatternLength'] = options.maxPatternLength
    if options.maxNumPatternSymbols:
            params['maxNumPatternSymbols'] = options.maxNumPatternSymbols
    if options.maxNumWildcard:
            params['maxNumWildcard'] = options.maxNumWildcard
    if options.maxNumFlexSpaces:
            params['maxNumFlexSpaces'] = options.maxNumFlexSpaces
    if options.maxFlexibility:
            params['maxFlexibility'] = options.maxFlexibility
    if options.maxFlexProduct:
            params['maxFlexProduct'] = options.maxFlexProduct
    if options.patternSymbolFile:
        params['patternSymbolFile'] = True
    else:
        params['patternSymbolFile'] = False
    if options.numPatternSymbols:
            params['numPatternSymbols'] = options.numPatternSymbols
    if options.patternScoring:
            params['patternScoring'] = options.patternScoring
    if options.patternGraph:
            params['patternGraph'] = options.patternGraph
    if options.searchGreediness:
            params['searchGreediness'] = options.searchGreediness
    if options.patternRefinement:
        params['patternRefinement'] = True
    else:
        params['patternRefinement'] = False
    if options.genAmbigSymbols:
        params['genAmbigSymbols'] = True
    else:
        params['genAmbigSymbols'] = False
    if options.patternFormat:
        params['patternFormat'] = True
    else:
        params['patternFormat'] = False
    if options.maxNumPatterns:
            params['maxNumPatterns'] = options.maxNumPatterns
    if options.maxNumAlignments:
            params['maxNumAlignments'] = options.maxNumAlignments
    if options.printPatterns:
        params['printPatterns'] = True
    else:
        params['printPatterns'] = False
    if options.printingRatio:
            params['printingRatio'] = options.printingRatio
    if options.printVertically:
        params['printVertically'] = True
    else:
        params['printVertically'] = False
    if options.stype:
            params['stype'] = options.stype
    if options.sequence:
            params['sequence'] = options.sequence
    if options.ppfile:
            params['ppfile'] = options.ppfile
# Submit the job
    jobid = serviceRun(options.email, options.title, params)
    if options.async: # Async mode
        print(jobid)
    else: # Sync mode
        print(jobid, file=sys.stderr)
        time.sleep(5)
        getResult(jobid)
# Get job status
elif options.status and options.jobid:
    printGetStatus(options.jobid)
# List result types for job
elif options.resultTypes and options.jobid:
    printGetResultTypes(options.jobid)
# Get results for job
elif options.polljob and options.jobid:
    getResult(options.jobid)
else:
    # Checks for 'email' parameter; added by Mana.
    if not options.email:
        print('\nParameter "--email" is missing in your command. It is required!\n')

    print(u'Error: unrecognised argument combination', file=sys.stderr)
    parser.print_help()