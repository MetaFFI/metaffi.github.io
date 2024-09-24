# load JVM
runtime = metaffi.metaffi_runtime.MetaFFIRuntime('openjdk')

# load log4j
log4j_api_module = runtime.load_module('log4j-api-2.21.1.jar;log4j-core-2.21.1.jar')

# load getLogger() method to get a new logger
getLogger = log4j_api_module.load_entity('class=org.apache.logging.log4j.LogManager,callable=getLogger', 
		[new_metaffi_type_info(metaffi_string8_type)], 
		[new_metaffi_type_info(metaffi_handle_type, 'org.apache.logging.log4j.Logger')])

# load error() method in logger
perror = log4j_api_module.load_entity('class=org.apache.logging.log4j.Logger,callable=error,instance_required',
	[new_metaffi_type_info(MetaFFITypes.metaffi_handle_type),
	new_metaffi_type_info(MetaFFITypes.metaffi_string8_type)],
	None)

# create logger with getLogger()
logger = getLogger('pylogger')
perror(logger, 'Logging error from python!')

runtime.release_runtime_plugin()