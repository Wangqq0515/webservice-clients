<?php

# ======================================================================
# 
# Copyright 2009-2018 EMBL - European Bioinformatics Institute
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# ======================================================================
# PHP InterProScan 5 (SOAP) command-line client.
#
# Note: this is a command-line program, call using:
#  php iprscan5_cli_php_soap.php [options...]
#
# Tested with:
#   PHP 5.1.6 (CentOS 5)
#   PHP 5.3.2 (Ubuntu 10.04 LTS)
#   PHP 5.3.3 (CentOS 6)
#   PHP 5.3.10 (Ubuntu 12.04 LTS)
#
# See:
# http://www.ebi.ac.uk/Tools/webservices/services/pfa/iprscan5_soap
# http://www.ebi.ac.uk/Tools/webservices/tutorials/php
# ======================================================================
# Load InterProScan 5 (SOAP) client library
require_once('iprscan5_lib_php_soap.php');

// Extend client class
class IPRScan5CliClient extends IPRScan5Client {
  // Print list of tool parameters
  function printGetParameters() {
    $this->printDebugMessage('printGetParameters', 'Begin', 1);
    $paramList = $this->getParameters();
    foreach($paramList as $paramName) {
      print $paramName . "\n";
    }
    $this->printDebugMessage('printGetParameters', 'End', 1);
  }

  // Print details of a parameter
  function printGetParameterDetails($parameterId) {
    $this->printDebugMessage('printGetParameterDetails', 'Begin', 1);
    $paramDetail = $this->getParameterDetails($parameterId);
    print $paramDetail->name . "\t" . $paramDetail->type . "\n";
    print $paramDetail->description . "\n";
    if(isset($paramDetail->values)) {
      foreach($paramDetail->values->value as $val) {
	print $val->value . "\t";
	if($val->defaultValue) print 'default';
	print "\n";
	if($val->label) print "\t" . $val->label . "\n";
	if(array_key_exists('properties', $val)) {
	  if(is_array($val->properties->property)) {
	    foreach($val->properties->property as $wsProperty) {
	      print "\t" .  $wsProperty->key . "\t" . $wsProperty->value . "\n";
	    }
	  }
	  else {
	    print "\t" .  $val->properties->property->key . "\t" . $val->properties->property->value . "\n";
	  }
	}
      }
    }
    $this->printDebugMessage('printGetParameterDetails', 'Begin', 1);
  }

  // Print available result types for a job
  function printGetResultTypes($jobId) {
    $this->printDebugMessage('PrintGetResultTypes', 'Begin', 1);
    $resultTypes = $this->getResultTypes($jobId);
    foreach($resultTypes as $resultType) {
      print $resultType->identifier . "\n";
      print "\t" . $resultType->label . "\n";
      if($resultType->description) {
	print "\t" . $resultType->description . "\n";
      }
      print "\t" . $resultType->mediaType . "\n";
      print "\t" . $resultType->fileSuffix . "\n";
    }
    $this->printDebugMessage('PrintGetResultTypes', 'End', 1);
  }
  
  // Submit a job.
  function submit($options) {
    $this->printDebugMessage('submit', 'Begin', 1);
    if(!isset($options['title'])) $options['title'] = '';
    $jobId = $this->run(
			$options['email'],
			$options['title'],
			$options['params']);
    // Async submission
    if($options['async'] || (isset($options['outputLevel']) && $options['outputLevel'] > 0)) {
      echo "$jobId\n";
    }
    // Sync submission... get results
    if(!$options['async']) {
      $options['jobId'] = $jobId;
      $this->poll($options);
    }
    $this->printDebugMessage('submit', 'End', 1);
  }

  // Client-side job polling.
  function clientPoll($jobId) {
    $this->printDebugMessage('clientPoll', 'Begin', 1);
    // Get status
    $status = 'PENDING';
    while(strcmp($status, 'PENDING') == 0 || strcmp($status, 'RUNNING') == 0) {
      $status = $this->getStatus($jobId);
      echo "$status\n";
      if(strcmp($status, 'PENDING') == 0 || strcmp($status, 'RUNNING') == 0) {
	sleep(15);
      }
    }
    $this->printDebugMessage('clientPoll', 'End', 1);
  }

  // Get results for finished job.
  function poll($options) {
    $this->printDebugMessage('poll', 'Begin', 1);
    // Check status and wait if necessary
    $this->clientPoll($options['jobId']);
    // Get the result types
    $resultTypeList = $this->getResultTypes($options['jobId']);
    if(isset($options['outfile'])) {
      $baseName = $options['outfile'];
    } else {
      $baseName = $options['jobId'];
    }
    foreach($resultTypeList as $resultType) {
      $this->printDebugMessage('poll', 'resultType: ' . $resultType->identifier, 1);
      $result = '';
      $filename = $baseName . '.' . $resultType->identifier . '.' . $resultType->fileSuffix;
      if(isset($options['input']['outformat'])) {
	if(strcmp($options['input']['outformat'], $resultType->identifier) == 0) {
	  $result = $this->getResult($options['jobId'], $resultType->identifier);
	}
      } else {
	$result = $this->getResult($options['jobId'], $resultType->identifier);
      }
      if($result) {
	print "$filename\n";
	file_put_contents($filename, $result);
      }
    }
    $this->printDebugMessage('poll', 'End', 1);
  }
}

try {
  // Parse command-line options
  $options = parseCommandLine($argv);

  // For no options or explict help request
  if($argc == 1 || strcmp($options['action'], 'help') == 0) {
    printUsage();
    exit(0);
  }

  // Get service proxy
  $client = new IPRScan5CliClient();
  // HTTP proxy config.
  //$client->setHttpProxy($proxy_host, $proxy_port);

  // Debug options
  if(array_key_exists('trace', $options)) $client->trace = 1;
  if(array_key_exists('debugLevel', $options)) {
    $client->debugLevel = $options['debugLevel'];
  }
  if(array_key_exists('WSDL', $options)) {
    $client->setWsdlUrl($options['WSDL']);
  }

  // Perform requested action
  switch($options['action']) {
    // List params
  case 'params':
    $client->printGetParameters();
    break;
    // Parameter information
  case 'paramDetail':
    $client->printGetParameterDetails($options['parameterId']);
    break;
    // Submit job
  case 'submit':
    $client->submit($options);
    break;
    // Get status
  case 'status':
    $status = $client->getStatus($options['jobId']);
    echo "$status\n";
    break;
    // Get result types
  case 'resultTypes':
    $client->printGetResultTypes($options['jobId']);
    break;
    // Get results
  case 'polljob':
    $client->poll($options);
    break;
  }
}
catch(SoapFault $ex) {
  echo 'Error: ';
  if($ex->getMessage() != '') {
    echo $ex->getMessage();
  }
  else {
    echo $ex;
  }
  echo "\n";
}

// Parse command-line options
function parseCommandLine($argList) {
  $options = array(
    'action' => 'unknown',
    'async' => FALSE,
    'params' => array(),
  );
  for($i=0; $i<count($argList); $i++) {
    $arg = $argList[$i];
    switch($arg) {
      // Help/usage
      case '--help':
        $options['action'] = 'help';
        break;
      // SOAP message trace
      case '--trace':
        $options['trace'] = 1;
        break;
      // Debug output
      case '--debugLevel':
	$i++;
        $options['debugLevel'] = $argList[$i];
        break;
      // Service WSDL location
      case '--WSDL':
	$i++;
        $options['WSDL'] = $argList[$i];
        break;

	// List params
    case '--params':
      $options['action'] = 'params';
      break;
	// List param details
    case '--paramDetail':
      $i++;
      $options['parameterId'] =  $argList[$i];
      $options['action'] = 'paramDetail';
      break;

      // Job identifier
    case '--jobid':
      $i++;
      $options['jobId'] = $argList[$i];
      break;
      // Get job status
    case '--status':
      $options['action'] = 'status';
      break;
      // Get available result types
    case '--resultTypes':
      $options['action'] = 'resultTypes';
      break;
      // Get job results
    case '--polljob':
      $options['action'] = 'polljob';
      break;
      // Output filename
    case '--outfile':
      $i++;
      $options['outfile'] = $argList[$i];
      break;
      // Output format
    case '--outformat':
      $i++;
      $options['input']['outformat'] = $argList[$i];
      break;
      // User e-mail
    case '--email':
      $i++;
      $options['action'] = 'submit';
      $options['email'] = $argList[$i];
      break;
      // Job title
    case '--title':
      $i++;
      $options['title'] = $argList[$i];
      break;
      // Async submission
    case '--async':
      $options['async'] = TRUE;
      break;

      // ### InterProScan parameters ###
      // Signature method(s)
    case '--appl':
    case '-appl':
    case '--app':
    case '-app':
      $i++;
      $options['params']['appl'] = split('[ ,;]+', $argList[$i]);
      break;
      // InterProScan Matches CRC look-up. Ignore for compatibility.
    case '--crc':
    case '-crc':
      //$options['params']['nocrc'] = FALSE;
      break;
    case '--nocrc':
    case '-nocrc':
      //$options['params']['nocrc'] = TRUE;
      break;
      // Include Gene Ontology (GO) terms in result.
    case '--goterms':
    case '-goterms':
      $options['params']['goterms'] = TRUE;
      break;
    case '--nogoterms':
    case '-nogoterms':
      $options['params']['goterms'] = FALSE;
      break;
      // Include pathway terms in result.
    case '--pathways':
    case '-pathways':
      $options['params']['pathways'] = TRUE;
      break;
    case '--nopathways':
    case '-nopathways':
      $options['params']['pathways'] = FALSE;
      break;
      // Query sequence data
    case '--sequence':
        $i++;
    default:
      if($i != 0) {
	if(file_exists($argList[$i])) {
	  // It's a file
	  $options['params']['sequence'] = file_get_contents($argList[$i]);
	}
	else {
	  // Assume it's an ID
	  $options['params']['sequence'] = $argList[$i];
	}
      }
    }
  }
  return $options;
}

// Print usage message
function printUsage() {
  $scriptName = 'iprscan5_cli_php_soap.php';
  print <<<EOF
InterProScan 5
==============

Identify protein family, domain and signal signatures in a protein sequence.

For more information on InterPro and InterProScan refer to 
http://www.ebi.ac.uk/interpro/

[Required]

  seqFile            : file : query sequence ("-" for STDIN, \@filename for
                              identifier list file)

[Optional]

      --appl         : str  : Comma separated list of signature methods to run,
                              see --paramDetail appl. 
      --goterms      :      : retrieve GO terms
      --nogoterms    :      : do not retrieve GO terms
      --pathways     :      : retrieve pathway terms
      --nopathways   :      : do not retrieve pathway terms

[General]

      --help         :      : prints this help text
      --async        :      : forces to make an asynchronous query
      --email        : str  : e-mail address
      --title        : str  : title for job
      --status       :      : get job status
      --resultTypes  :      : get available result types for job
      --polljob      :      : poll for the status of a job
      --jobid        : str  : jobid that was returned when an asynchronous job 
                              was submitted.
      --outfile      : str  : file name for results (default is jobid)
      --outformat    : str  : result format to retrieve
      --params       :      : list input parameters
      --paramDetail  : str  : display details for input parameter
      --trace        :      : show SOAP messages being interchanged 

Synchronous job:

  The results/errors are returned as soon as the job is finished.
  Usage: $scriptName --email <your\@email> [options...] seqFile
  Returns: results as an attachment

Asynchronous job:

  Use this if you want to retrieve the results at a later time. The results 
  are stored for up to 24 hours. 
  Usage: $scriptName --async --email <your\@email> [options...] seqFile
  Returns: jobid

  Use the jobid to query for the status of the job. If the job is finished, 
  it also returns the results/errors.
  Usage: $scriptName --polljob --jobid <jobId> [--outfile string]
  Returns: string indicating the status of the job and if applicable, results 
  as an attachment.

Further information:

  http://www.ebi.ac.uk/Tools/webservices/services/pfa/iprscan5_soap
  http://www.ebi.ac.uk/Tools/webservices/tutorials/php

Support/Feedback:

  http://www.ebi.ac.uk/support/

EOF;
}
?>
