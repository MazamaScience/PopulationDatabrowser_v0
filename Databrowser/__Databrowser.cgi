#!__PYTHON__
# -*- coding: utf-8 -*-
#
# Name:
#       __DATABROWSER__.cgi
#
# Author:
#       Jonathan Callahan <jonathan@mazamascience.com>
#
# SECURITY: 1) All incoming parameter names and values are validated before being used.
# SECURITY: 2) All commands are run inside a try/except block.

__version__ = "0.9.2.0"  # Examples of jquery-ui built in.


################################################################################
# BEGIN configuration.
################################################################################

# Variables configured with config/Makefile_vars_~
URL_PATH = '__URL_PATH__'
DATABROWSER_PATH = '__DATABROWSER_PATH__'
OUTPUT_DIR = '__OUTPUT_DIR__'
CACHE_SIZE = __CACHE_SIZE__

# Directories
URL_OUT = URL_PATH + '/' + OUTPUT_DIR
ABS_OUT = DATABROWSER_PATH + '/' + OUTPUT_DIR

# Minimal request object
request = {'debug': 'none',
           'responseType': 'json',
           'plotWidth': '500',
           'plotType': 'DEFAULT'}

# NOTE:  You can set up a request object with all required parameters and run this
# NOTE:  this cgi script from the command line for debugging.
#request = {'debug': 'transcript',
#           'responseType': 'json',
#           'plotWidth': '500',
#           'plotHeight': '500',
#           'plotDevice': 'png',
#           'language': 'en',
#           'lineColor': 'black',
#           'plotType': 'TrigFunctions',
#           'trigFunction': 'cos'}



# Create a dictionary of valids against which incoming parameters will be compared
valids = {}

# Start off by assuming all parameters are alpha-numeric strings
for key in request.keys():
    valids[key] = ['ALPHANUMERIC']

# Now override for specific elements that are numeric
numeric_parameters = ['plotWidth','plotHeight']
for key in numeric_parameters:
    valids[key] = ['NUMERIC']

# Special case for 'debug'
valids['debug'] = ['none', 'transcript']

# NOTE:  This should be enough protection but specific values can be included in
# NOTE:  order to trap bad parameters and generate error strings within this CGI
# NOTE:  script.
# NOTE:  E.g. valids['fruit'] = ['apple','banana','orange']

# Special case for 'responseType'
valids['responseType'] = ['json']


################################################################################
# END configuration. BEGIN setup.
################################################################################


# Initialize the default status and message strings
status = 'OK'
error_text = ''
debug_text = ''

# Import required python modules
import sys, os, re, time
import cgi
# The json module was introduced in python 2.6
# For backwards compatibility you can import simplejson
try:
    import json
except ImportError:
    import simplejson as json 

start = time.time()
timepoint = time.time()

# Set up the TRANSCRIPT file and redirect stdout there
try:
    transcript = DATABROWSER_PATH + '/TRANSCRIPT.txt'
    sys.stdout=open(transcript,'w')
    transcript_was_used = True
except Exception, e:
    transcript_was_used = False
    error_text = "cannot open transcript file:  " + str(e)
    status = 'ERROR'

# Profiling point
elapsed = time.time() - timepoint
debug_text += "\n# %07.4f seconds to open TRANSCRIPT.txt\n" % elapsed
timepoint = time.time()

# Debugging info
debug_text += "\nEnvironment Variables:\n"
for param in os.environ.keys():
  debug_text += "\t%20s: %s\n" % (param, os.environ[param])


# Use the parameter:value pairs from the web server to override the default 'request' parameters
FS = cgi.FieldStorage()
for key in FS.keys():
    try:
        request[key] = FS[key].value
    except Exception, e:
        status = 'ERROR'
        error_text = "incoming parameter '%s' has no value:  %s" % (key,str(e))

    # parameters not mentioned in request{} above are assigned to ALPHANUMERIC by default
    if key not in valids:
        valids[key] = ['ALPHANUMERIC']

# Validate every parameter against the list of valids for that parameter
debug_text += "\nRequest:\n"
for key in request:
    value = request[key]
    debug_text += "\t%s = '%s'\n" % (key,value)
    
    if key == 'plotWidth':
        try:
            if int(value) < 100 or int(value) > 2000:
                request['plotWidth'] = '500'
        except Exception, e:
            error_text = "parameter '%s' has a value of '%s' which is not an integer: %s" % (key,value,e)
            status = 'ERROR'

    elif key == 'plotHeight':
        try:
            if int(value) < 100 or int(value) > 1200:
                request['plotHeight'] = request['plotWidth']
        except Exception, e:
            error_text = "parameter '%s' has a value of '%s' which is not an integer: %s" % (key,value,e)
            status = 'ERROR'

    elif key == 'countryName':
        pass

    elif valids[key][0] == 'NUMERIC':
        try:
            val = float(value)
        except Exception, e:
            error_text = "parameter '%s' has a value of '%s' which is not numeric: %s" % (key,value,e)
            status = 'ERROR'

    elif valids[key][0] == 'ALPHANUMERIC':
        # NOTE:  Accept '' as a valid alphanumeric value
        if value != '':
            # NOTE:  Accept alphanumeric strings which may also contain '.', ',', '_' or '-'
            if not value.replace(' ','').replace('.','').replace(',','').replace('_','').replace('-','').replace('(','').replace(')','').isalnum():    
                error_text = "parameter '%s' has a value of '%s' which is not alphanumeric" % (key,value)
                status = 'ERROR'

    else:
        if value not in valids[key]:
            error_text = "parameter '%s' has a value of '%s' which is not a valid value" % (key,value)
            status = 'ERROR'


# Profiling point
elapsed = time.time() - timepoint
debug_text += "\n# %07.4f seconds to validate parameters\n" % elapsed
timepoint = time.time()


################################################################################
# END setup. BEGIN generation of result.
################################################################################

from_cache = False

if status == 'OK':

    # Create unique filebase from request    
    import copy
    import hashlib

    # Remove 'responseType' and any other parameters that do not require the
    # generation of new output products.  We want things to be found in cache
    # as often as possible.
    dummyDict = copy.deepcopy(request)
    dummy = dummyDict.pop('responseType')
    unique_ID = hashlib.sha256(str(dummyDict)).hexdigest()

    # Set up filenames to be used
    abs_base = ABS_OUT + '/' + unique_ID
    rel_base = OUTPUT_DIR + '/' + unique_ID
    abs_png = abs_base + '.png'
    abs_json = abs_base + '.json'
    abs_file = abs_base + '.' + request['responseType']

    # modify the request
    request['outputFileBase'] = unique_ID

    # Determine whether the output file is found in cache
    if (request['responseType'] == 'json'):
        from_cache = os.path.exists(abs_png) and os.path.exists(abs_json)
    else:
        from_cache = os.path.exists(abs_file)

    # Check for a previously generated result.
    if from_cache:
        # File exists -- no action necessary
        debug_text += "\n'%s' already exists\n" % abs_file
        debug_text += "\nRetrieving file from cache\n"
        elapsed = time.time() - start
        debug_text += "\n# %07.4f seconds from start to finish\n" % elapsed
        print(debug_text)
        from_cache = True

    else:

        # We're going to generate a new plot so we need to make sure
        # that we have room in the cache.

        # Cache management by Lucy Williams ----------------------------------------
    
        # Compiles statistics on all files in the output directory
        files = (os.listdir(ABS_OUT))
        stats = []
        totalSize = 0
        for file in files:
            path = ABS_OUT + '/' + file
            statList = os.stat(path)
            # path, size, atime
            newStatList = [path, statList.st_size, statList.st_atime]
            totalSize = totalSize + statList.st_size
            # don't want hidden files so don't add stuff that starts with .
            if not file.startswith('.'):
                stats.append(newStatList)
        
        # Sort file stats by last access time
        stats = sorted(stats, key=lambda file: file[2])
        
        # Delete old files until we get under CACHE_SIZE (configured in megabytes)
        numDeletions = 0
        while totalSize > CACHE_SIZE * 1000000:
            # front of stats list is the file with the smallest (=oldest) access time
            lastAccessedFile = stats[0]
            # index 1 is where size is
            totalSize = totalSize - lastAccessedFile[1]
            # index 0 is where path is
            os.remove(lastAccessedFile[0])
            # remove the file from the stats list
            stats.pop(0)
            numDeletions = numDeletions + 1
            
        # Profiling point
        elapsed = time.time() - timepoint
        debug_text += "\n# %07.4f seconds to keep the cache at %07.2f megabytes -- %d files deleted\n" % (elapsed,CACHE_SIZE,numDeletions)
        timepoint = time.time()
    
        # END Cache management -----------------------------------------------------
    
    
        # Need to generate a new plot
        try:
            import rpy2.robjects as robjects
            r = robjects.r
        except Exception, e:
            status = 'ERROR'
            error_text = str(e)

        elapsed = time.time() - timepoint
        debug_text += "\n# %07.4f seconds to import the rpy module\n" % elapsed
        timepoint = time.time()

        script = DATABROWSER_PATH + '/__DATABROWSER__.R'

        # Create debugging output to appear in the transcript
        r_commands = "\n# NOTE:  Next lines are for interactive debugging in R.\n\n"

        r_commands += "\nsource('" + script + "')\n\n"
        r_commands += "__DATABROWSER__(jsonArgs='" + json.dumps(request) + "')\n"

        # NOTE:  The R script may return the results of calculations as a FloatVector.
        # NOTE:  The default plotting script returns a list of 4 values.
        r_return_values = [0.0,0.0,0.0,0.0]
        return_values = [0.0,0.0,0.0,0.0]

        # Run the R commands using the rpy2 module 
        try:

            # We convert the incoming request dictionary into a JSON string and
            # pass this string to the databrowser function where it is converted
            # into the infoList.
            r_command = "__DATABROWSER__(jsonArgs='" + json.dumps(request) + "')"
            
            r.source(script)
            r_return_values = r(r_command)

            # Easy conversion from Rpy FloatVector to normal python array
            for i in range(len(r_return_values)):
                return_values[i] = r_return_values[i]

            # Profiling point
            elapsed = time.time() - timepoint
            debug_text += "\n# %07.4f seconds to run the R commands\n" % elapsed
            debug_text += r_commands
            timepoint = time.time()

            elapsed = time.time() - start
            debug_text += "\n# %07.4f seconds from start to finish\n" % elapsed

            print(debug_text)

        except Exception, e:
            status = 'ERROR'
            error_text = str(e)
            try:
                debug_file = DATABROWSER_PATH + "/DEBUG.txt"
                dbg = open(debug_file,'a')
                dbg.write("\n\nR ERROR on " + str(time.ctime()) + ":\n")
                dbg.write(error_text)
                dbg.write("R COMMANDS:\n" + r_commands + "\n")
                dbg.close()
            except Exception, e:
                error_text = str(e)
                print("\nAn error occurred writing the debug file: " + error_text)


################################################################################
# END generation of result. BEGIN response.
################################################################################


# Restore stdout
if transcript_was_used:
    sys.stdout.close()
    sys.stdout=sys.__stdout__

########################################
# JSON response
########################################
if request['responseType'] == 'json':
    
    # Set up the response object
    response = {}
    if status == 'OK':
        if from_cache:
            # Read the json response object if it had been stored previously so that return_values can be retrieved
            try:
                f = open(abs_json,'r')
                response = json.loads(f.read())
                f.close()
            except Exception, e:
                status = 'ERROR'
                error_text = 'CGI ERROR: cannot read cached json file: ' + str(e)
                response = {'status':status, 'error_text':error_text}
        else:
            # Otherwise, create and store the json response object
            response = {'status':status,
                        'rel_base':rel_base,
                        'return_values':return_values}
            try:
                f = open(abs_json,'w')
                f.write(json.dumps(response))
                f.close()
            except:
                status = 'ERROR'
                error_text = 'CGI ERROR: cannot write json file to cache: ' + str(e)
                response = {'status':status, 'error_text':error_text}
    
    elif status == 'ERROR':
        response = {'status':status, 'error_text':error_text }
    
    else:
        response = {'status':status, 'error_text':'CGI ERROR: An unknown error occurred.' }
    
    # Write out the JSON response for AJAX
    if request['debug'] == 'none':
        sys.stdout.write("Content-type: application/json\n\n")
        sys.stdout.write(json.dumps(response))
    
    # Write out the JSON response for humans
    elif request['debug'] == 'transcript':
        sys.stdout.write("Content-type: text/plain\n\n")
        sys.stdout.write("TRANSCRIPT:\n")
        sys.stdout.write(debug_text + "\n")
        sys.stdout.write(json.dumps(response, sort_keys=True, indent=4)) # pretty
        sys.stdout.write("\n")
        sys.stdout.write("\nEND OF TRANSCRIPT\n")
    

################################################################################
# END response. All done!
################################################################################


# If this is being run from the command line, add another blank line
if FS.keys() == []:
    print("\n")

