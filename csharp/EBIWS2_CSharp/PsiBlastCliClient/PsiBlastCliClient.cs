/* $Id$
 * ======================================================================
 * 
 * Copyright 2010-2018 EMBL - European Bioinformatics Institute
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * 
 * ======================================================================
 * jDispatcher SOAP command-line client for NCBI PSI-BLAST
 * ====================================================================== */
using System;
using System.IO;
using EbiWS.PsiBlastWs;

namespace EbiWS
{
	class PsiBlastCliClient : EbiWS.PsiBlastClient
	{
		/// <summary>Tool specific options for usage</summary>
		private string usageMsg0 = @"NCBI PSI-BLAST
==============

Rapid sequence database search programs utilizing the PSI-BLAST algorithm.

[Required]

  -D, --database      : str  : database(s) to search, space separated. See
                               --paramDetail database
  seqFile             : file : query sequence (""-"" for STDIN, \@filename for
                               identifier list file)

[Optional]

  -M, --matrix        : str  : scoring matrix, see --paramDetail matrix
  -e, --expthr        : real : 0<E<= 1000. Statistical significance threshold 
                               for reporting database sequence matches.
  -h, --psithr        : real : E-value limit for inclusion in PSSM
  -F, --filter        :      : filter the query sequence for low complexity 
                               regions, see --paramDetail filter
  -m, --alignView     : int  : pairwise alignment format, 
                               see --paramDetail align
  -v, --scores        : int  : number of scores to be reported
  -b, --alignments    : int  : number of alignments to report
  -G, --gapopen       : int  : Gap open penalty
  -E, --gapext        : int  : Gap extension penalty
  -X, --dropoff       : int  : Drop-off
  -Z, --finaldropoff  : int  : Final dropoff score
      --seqrange      : str  : region within input to use as query
      --previousjobid : str  : Job Id for last iteration
      --selectedHits  : file : Selected hits from last iteration for building 
                               search profile (PSSM)
  -R, --cpfile        : file : PSI-BLAST checkpoint from last iteration
";
		/// <summary>Additional tool details</summary>
		private string usageMsg1 = @"Iterations:

  To generate and refine the profile (PSSM) used to perform the search after 
  the first iteration the set of hits to be included in the generation of the 
  PSSM needs to be specified for each iteration. This can be either obtained 
  from the previous iteration using the job identifier of the iteration, or 
  be explicit specification of a file containing the list of identifiers. 
  
  Iteration 1:
  PsiBlastCliClient.exe --email <email> --database <db> <seqFile> [options...]
  
  Iteration 2:
  PsiBlastCliClient.exe --email <email> --previousjobid <jobId> \
    [--selectedHits <selFile>] [options...]

  Iteration 3+:
  PsiBlastCliClient.exe --email <email> --previousjobid <jobId> \
    [--selectedHits <selFile>] [--cpfile <checkpoint>] [options...]

Further information:

http://www.ebi.ac.uk/Tools/webservices/services/sss/psiblast_soap
http://www.ebi.ac.uk/Tools/webservices/tutorials/06_programming/dot_net/csharp

Support/Feedback:

http://www.ebi.ac.uk/support/
";

		/// <summary>Execution entry point</summary>
		/// <param name="args">Command-line parameters</param>
		/// <returns>Exit status</returns>
		public static int Main(string[] args)
		{
			int retVal = 0; // Return value
			// Create an instance of the wrapper object
			PsiBlastCliClient wsApp = new PsiBlastCliClient();
			// If no arguments print usage and return
			if (args.Length < 1)
			{
				wsApp.PrintUsageMessage();
				return retVal;
			}
			try
			{
				// Parse the command line
				wsApp.ParseCommand(args);
				// Perform the selected action
				switch (wsApp.Action)
				{
					case "paramList": // List parameter names
						wsApp.PrintParams();
						break;
					case "paramDetail": // Parameter detail
						wsApp.PrintParamDetail(wsApp.ParamName);
						break;
					case "submit": // Submit a job
						wsApp.SubmitJobs();
						break;
					case "status": // Get job status
						wsApp.PrintStatus();
						break;
					case "resultTypes": // Get result types
						wsApp.PrintResultTypes();
						break;
					case "polljob": // Get job results
						wsApp.GetResults();
						break;
					case "getids": // Get IDs from job result
						wsApp.PrintGetIds();
						break;
					case "version": // Version information.
						wsApp.PrintVersionMessage();
						break;
					case "help": // Do help
						wsApp.PrintUsageMessage();
						break;
					default: // Any other action.
						Console.WriteLine("Error: unknown action " + wsApp.Action);
						retVal = 1;
						break;
				}
			}
			catch (System.Exception ex)
			{ // Catch all exceptions
				Console.Error.WriteLine("Error: " + ex.Message);
				Console.Error.WriteLine(ex.StackTrace);
				retVal = 2;
			}
			return retVal;
		}

		/// <summary>
		/// Print the usage message.
		/// </summary>
		private void PrintUsageMessage()
		{
			PrintDebugMessage("PrintUsageMessage", "Begin", 1);
			Console.WriteLine(usageMsg0);
			PrintGenericOptsUsage();
			Console.WriteLine(usageMsg1);
			PrintDebugMessage("PrintUsageMessage", "End", 1);
		}

		/// <summary>
		/// Print the version message.
		/// </summary>
		private void PrintVersionMessage()
		{
			PrintDebugMessage("PrintVersionMessage", "Begin", 1);
			PrintClientVersion(this.GetType().Assembly);
			PrintClientLicense();
			PrintDebugMessage("PrintVersionMessage", "End", 1);
		}

		/// <summary>Parse command-line options</summary>
		/// <param name="args">Command-line options</param>
		private void ParseCommand(string[] args)
		{
			PrintDebugMessage("ParseCommand", "Begin", 1);
			InParams = new InputParameters();
			for (int i = 0; i < args.Length; i++)
			{
				PrintDebugMessage("parseCommand", "arg: " + args[i], 2);
				switch (args[i])
				{
						// Generic options
					case "--help": // Usage info
						Action = "help";
						break;
					case "/help":
						goto case "--help";
					case "--version": // Version info
						Action = "version";
						break;
					case "/version":
						goto case "--version";
					case "--params": // List input parameters
						Action = "paramList";
						break;
					case "/params":
						goto case "--params";
					case "--paramDetail": // Parameter details
						ParamName = args[++i];
						Action = "paramDetail";
						break;
					case "/paramDetail":
						goto case "--paramDetail";
					case "--jobid": // Job Id to get status or results
						JobId = args[++i];
						break;
					case "/jobid":
						goto case "--jobid";
					case "--status": // Get job status
						Action = "status";
						break;
					case "/status":
						goto case "--status";
					case "--resultTypes": // Get result types
						Action = "resultTypes";
						break;
					case "/resultTypes":
						goto case "--resultTypes";
					case "--polljob": // Get results for job
						Action = "polljob";
						break;
					case "/polljob":
						goto case "--polljob";
					case "--outfile": // Base name for results file(s)
						OutFile = args[++i];
						break;
					case "/outfile":
						goto case "--outfile";
					case "--outformat": // Only save results of this format
						OutFormat = args[++i];
						break;
					case "/outformat":
						goto case "--outformat";
					case "--ids": // Get entry IDs from result
						Action = "getids";
						break;
					case "/ids":
						goto case "--ids";
					case "--verbose": // Output level
						OutputLevel++;
						break;
					case "/verbose":
						goto case "--verbose";
					case "--quiet": // Output level
						OutputLevel--;
						break;
					case "/quiet":
						goto case "--quiet";
					case "--email": // User e-mail address
						Email = args[++i];
						break;
					case "/email":
						goto case "--email";
					case "--title": // Job title
						JobTitle = args[++i];
						break;
					case "/title":
						goto case "--title";
					case "--async": // Async submission
						Action = "submit";
						Async = true;
						break;
					case "/async":
						goto case "--async";
					case "--debugLevel":
						DebugLevel = Convert.ToInt32(args[++i]);
						break;
					case "/debugLevel":
						goto case "--debugLevel";
					case "--endpoint": // Service endpoint
						ServiceEndPoint = args[++i];
						break;
					case "/endpoint":
						goto case "--endpoint";
					case "--multifasta": // Multiple sequence input (fasta format)
						this.multifasta = true;
						break;
					case "/multifasta":
						goto case "--multifasta";

						// Tool specific options
					case "--database": // Database to search
						InParams.database = args[++i];
						Action = "submit";
						break;
					case "-D":
						goto case "--database";
					case "/database":
						goto case "--database";
					case "/D":
						goto case "--database";
					case "--matrix": // Scoring matrix
						InParams.matrix = args[++i];
						Action = "submit";
						break;
					case "-M":
						goto case "--matrix";
					case "/matrix":
						goto case "--matrix";
					case "/M":
						goto case "--matrix";
					case "--expthr": // E-value threshold
						InParams.expthr = Convert.ToDouble(args[++i]);
						InParams.expthrSpecified = true;
						Action = "submit";
						break;
					case "-e":
						goto case "--expthr";
					case "/expthr":
						goto case "--expthr";
					case "/e":
						goto case "--expthr";
				case "--psithr": // PSI E-value threshold
					InParams.psithr = Convert.ToDouble(args[++i]);
					InParams.psithrSpecified = true;
					break;
				case "-h":
					goto case "--psithr";
				case "/psithr":
					goto case "--psithr";
				case "/h":
					goto case "--psithr";
					case "--filter": // Low complexity filter
						InParams.filter = "1"; // Set true
						Action = "submit";
						break;
					case "-F":
						goto case "--filter";
					case "/filter":
						goto case "--filter";
					case "/F":
						goto case "--filter";
					case "--alignView": // Alignment format
						InParams.alignView = Convert.ToInt32(args[++i]);
						Action = "submit";
						break;
				case "-m":
					goto case "--alignView";
					case "/alignView":
						goto case "--alignView";
				case "/m":
					goto case "--alignView";
					case "--scores": // Maximum number of scores to report
						InParams.scores = Convert.ToInt32(args[++i]);
						Action = "submit";
						break;
					case "-v":
						goto case "--scores";
					case "/scores":
						goto case "--scores";
					case "/v":
						goto case "--scores";
					case "--alignments": // Maximum number of alignments to report
						InParams.alignments = Convert.ToInt32(args[++i]);
						Action = "submit";
						break;
				case "-b":
					goto case "--alignments";
					case "/alignments":
						goto case "--alignments";
				case "/b":
					goto case "--alignments";
					case "--gapopen": // Gap open penalty
						InParams.gapopen = Convert.ToInt32(args[++i]);
						Action = "submit";
						break;
					case "-G":
						goto case "--gapopen";
					case "/gapopen":
						goto case "--gapopen";
					case "/G":
						goto case "--gapopen";
					case "--gapext": // Gap extension penalty
						InParams.gapext = Convert.ToInt32(args[++i]);
						Action = "submit";
						break;
					case "-E":
						goto case "--gapext";
					case "/gapext":
						goto case "--gapext";
					case "/E":
						goto case "--gapext";
					case "--dropoff": // Drop-off score
						InParams.dropoff = Convert.ToInt32(args[++i]);
						Action = "submit";
						break;
					case "-X":
						goto case "--dropoff";
					case "/dropoff":
						goto case "--dropoff";
					case "/X":
						goto case "--dropoff";
					case "--finaldropoff": // Final drop-off score
						InParams.finaldropoff = Convert.ToInt32(args[++i]);
						Action = "submit";
						break;
					case "-Z":
						goto case "--finaldropoff";
					case "/finaldropoff":
						goto case "--finaldropoff";
					case "/Z":
						goto case "--finaldropoff";
				case "--seqrange":
					InParams.seqrange = args[++i];
					break;
				case "/seqrange":
					goto case "--seqrange";
				case "--previousjobid":
					InParams.previousjobid = args[++i];
					Action = "submit";
					break;
				case "/previousjobid":
					goto case "--previousjobid";
				case "--selectedHits":
					InParams.selectedHits = ReadFile(args[++i]);
					break;
				case "/selectedHits":
					goto case "/selectedHits";
				case  "--cpfile":
					InParams.cpfile = ReadFile(args[++i]);
					break;
				case "/cpfile":
					goto case "--cpfile";
				case "-R":
					goto case "--cpfile";
				case "/R":
					goto case "--cpfile";

						// Input data/sequence option
					case "--sequence": // Input sequence
						i++;
						goto default;
					default:
						// Check for unknown option
						if (args[i].StartsWith("--") || args[i].LastIndexOf('/') == 0)
						{
							Console.Error.WriteLine("Error: unknown option: " + args[i] + "\n");
							Action = "exit";
							return;
						}
						// Must be data argument
						InParams.sequence = args[i];
						Action = "submit";
						break;
				}
			}
			PrintDebugMessage("ParseCommand", "End", 1);
		}
	}
}
