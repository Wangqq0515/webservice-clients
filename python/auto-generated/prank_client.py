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
baseUrl = u'http://www.ebi.ac.uk/Tools/services/rest/prank'

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
    PRANK is a probabilistic multiple alignment program for DNA, codon and amino-acid sequences. It\'s based on a novel algorithm that treats insertions correctly and avoids over-estimation of the number of deletion events. In addition, PRANK borrows ideas from maximum likelihood methods used in phylogenetics and correctly takes into account the evolutionary distances between sequences. Lastly, PRANK allows for defining a potential structure for sequences to be aligned and then, simultaneously with the alignment, predicts the locations of structural units in the sequences.\
'''
epilog = u'''For further information about the Prank web service, see
http://www.ebi.ac.uk/tools/webservices/services/msa/prank_rest.'''
version = u'98c6601'

# Process command-line options
parser = OptionParser(usage=usage, description=description, epilog=epilog, version=version)

# Tool specific options (Try to print all the commands automatically)

parser.add_option('--sequence', help='Three or more sequences to be aligned can be entered directly into this form. The sequences must be in FASTA format. Partially formatted sequences are not accepted. Adding a return to the end of the sequence may help certain applications understand the input. Note that directly using data from word processors may yield unpredictable results as hidden/control characters may be present. There is a limit of 500 sequences or 1MB of data.')
parser.add_option('--data_file', help='A file containing valid sequences in FASTA format can be used as input for the sequence similarity search. Word processors files may yield unpredictable results as hidden/control characters may be present in the files. It is best to save files with the Unix format option to avoid hidden Windows characters.')
parser.add_option('--tree_file', help='Tree file in Newick Binary Format.')
parser.add_option('--do_njtree', help='compute guide tree from input alignment')
parser.add_option('--do_clustalw_tree', help='compute guide tree using Clustalw2')
parser.add_option('--model_file', help='Structure Model File.')
parser.add_option('--output_format', help='Format for output alignment file')
parser.add_option('--trust_insertions', help='Trust inferred insertions and do not allow their later matching')
parser.add_option('--show_insertions_with_dots', help='Show gaps created by insertions as dots, deletions as dashes')
parser.add_option('--use_log_space', help='Use log space for probabilities; slower but necessary for large numbers of sequences')
parser.add_option('--use_codon_model', help='Use codon substutition model for alignment; requires DNA, multiples of three in length')
parser.add_option('--translate_DNA', help='Translate DNA sequences to proteins and backtranslate results')
parser.add_option('--mt_translate_DNA', help='Translate DNA sequences to mt proteins, align and backtranslate results')
parser.add_option('--gap_rate', help='Gap Opening Rate')
parser.add_option('--gap_extension', help='Gap Extension Probability')
parser.add_option('--tn93_kappa', help='Parameter kappa for Tamura-Nei DNA substitution model')
parser.add_option('--tn93_rho', help='Parameter rho for Tamura-Nei DNA substitution model')
parser.add_option('--guide_pairwise_distance', help='Fixed pairwise distance used for generating scoring matrix in guide tree computation')
parser.add_option('--max_pairwise_distance', help='Maximum pairwise distance allowed in progressive steps of multiple alignment; allows making matching more stringent or flexible')
parser.add_option('--branch_length_scaling', help='Factor for scaling all branch lengths')
parser.add_option('--branch_length_fixed', help='Fixed value for all branch lengths')
parser.add_option('--branch_length_maximum', help='Upper limit for branch lengths')
parser.add_option('--use_real_branch_lengths', help='Use real branch lengths; using this can be harmful as scoring matrices became flat for large distances; rather use max_pairwise_distance')
parser.add_option('--do_no_posterior', help='Do not compute posterior probability; much faster if those not needed')
parser.add_option('--run_once', help='Do not iterate alignment')
parser.add_option('--run_twice', help='Iterate alignment')
parser.add_option('--penalise_terminal_gaps', help='Penalise terminal gaps as any other gap')
parser.add_option('--do_posterior_only', help='Compute posterior probabilities for given *aligned* sequences; may be unstable but useful')
parser.add_option('--use_chaos_anchors', help='Use chaos anchors to massively speed up alignments; DNA only')
parser.add_option('--minimum_anchor_distance', help='Minimum chaos anchor distance')
parser.add_option('--maximum_anchor_distance', help='Maximum chaos anchor distance')
parser.add_option('--skip_anchor_distance', help='Chaos anchor skip distance')
parser.add_option('--drop_anchor_distance', help='Chaos anchor drop distance')
parser.add_option('--output_ancestors', help='Output ancestral sequences and probability profiles; note additional files')
parser.add_option('--noise_level', help='Noise level; progress and debugging information')
parser.add_option('--stay_quiet', help='Stay quiet; disable all progress information')
parser.add_option('--random_seed', help='Set seed for random number generator; not recommended')
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

    if options.sequence:
            params['sequence'] = options.sequence
    if options.data_file:
            params['data_file'] = options.data_file
    if options.tree_file:
            params['tree_file'] = options.tree_file
    if options.do_njtree:
        params['do_njtree'] = True
    else:
        params['do_njtree'] = False
    if options.do_clustalw_tree:
        params['do_clustalw_tree'] = True
    else:
        params['do_clustalw_tree'] = False
    if options.model_file:
            params['model_file'] = options.model_file
    if options.output_format:
            params['output_format'] = options.output_format
    if options.trust_insertions:
        params['trust_insertions'] = True
    else:
        params['trust_insertions'] = False
    if options.show_insertions_with_dots:
        params['show_insertions_with_dots'] = True
    else:
        params['show_insertions_with_dots'] = False
    if options.use_log_space:
        params['use_log_space'] = True
    else:
        params['use_log_space'] = False
    if options.use_codon_model:
        params['use_codon_model'] = True
    else:
        params['use_codon_model'] = False
    if options.translate_DNA:
        params['translate_DNA'] = True
    else:
        params['translate_DNA'] = False
    if options.mt_translate_DNA:
        params['mt_translate_DNA'] = True
    else:
        params['mt_translate_DNA'] = False
    if options.gap_rate:
            params['gap_rate'] = options.gap_rate
    if options.gap_extension:
            params['gap_extension'] = options.gap_extension
    if options.tn93_kappa:
            params['tn93_kappa'] = options.tn93_kappa
    if options.tn93_rho:
            params['tn93_rho'] = options.tn93_rho
    if options.guide_pairwise_distance:
            params['guide_pairwise_distance'] = options.guide_pairwise_distance
    if options.max_pairwise_distance:
            params['max_pairwise_distance'] = options.max_pairwise_distance
    if options.branch_length_scaling:
            params['branch_length_scaling'] = options.branch_length_scaling
    if options.branch_length_fixed:
            params['branch_length_fixed'] = options.branch_length_fixed
    if options.branch_length_maximum:
            params['branch_length_maximum'] = options.branch_length_maximum
    if options.use_real_branch_lengths:
        params['use_real_branch_lengths'] = True
    else:
        params['use_real_branch_lengths'] = False
    if options.do_no_posterior:
        params['do_no_posterior'] = True
    else:
        params['do_no_posterior'] = False
    if options.run_once:
        params['run_once'] = True
    else:
        params['run_once'] = False
    if options.run_twice:
        params['run_twice'] = True
    else:
        params['run_twice'] = False
    if options.penalise_terminal_gaps:
        params['penalise_terminal_gaps'] = True
    else:
        params['penalise_terminal_gaps'] = False
    if options.do_posterior_only:
        params['do_posterior_only'] = True
    else:
        params['do_posterior_only'] = False
    if options.use_chaos_anchors:
        params['use_chaos_anchors'] = True
    else:
        params['use_chaos_anchors'] = False
    if options.minimum_anchor_distance:
            params['minimum_anchor_distance'] = options.minimum_anchor_distance
    if options.maximum_anchor_distance:
            params['maximum_anchor_distance'] = options.maximum_anchor_distance
    if options.skip_anchor_distance:
            params['skip_anchor_distance'] = options.skip_anchor_distance
    if options.drop_anchor_distance:
            params['drop_anchor_distance'] = options.drop_anchor_distance
    if options.output_ancestors:
        params['output_ancestors'] = True
    else:
        params['output_ancestors'] = False
    if options.noise_level:
            params['noise_level'] = options.noise_level
    if options.stay_quiet:
        params['stay_quiet'] = True
    else:
        params['stay_quiet'] = False
    if options.random_seed:
            params['random_seed'] = options.random_seed
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