# January, 2013
# November, 2010
# July, 2009
# Jonathan Callahan
# mazamascience.com
#
# Makefile for a Mazama Science Databrowser.

# The following make variables are defined in Makefile_vars.mk:
 
# Server specific locations
#
# SERVER                      -- DNS name of the server
# OWNERSHIP                   -- argument to chown, allows web server to create files
# CGI_PATH                    -- absolute path of the CGI directory
# DATABROWSER_PATH            -- absolute path of the databrowser directory
# DATABROWSER                 -- name of databrowser
# DATA_DIR                    -- name of subdirectory containing data accessed by the databrowser (will be soft linked --> data/)
# OUTPUT_DIR                  -- name of subdirectory containing databrowser products
# CACHE_SIZE                  -- size of cache in megabytes
#
# PYTHON_SED_SCRIPT           -- sed script for the location of Python
# URL_PATH_SED_SCRIPT         -- sed script for full databrowser URLs
# DATABROWSER_PATH_SED_SCRIPT -- sed script for full databrowser path
# OUTPUT_DIR_SED_SCRIPT       -- sed script for the output directory
# ATTRIBUTION_SED_SCRIPT      -- sed script for the text at the bottom of plots
# DATABROWSER_SED_SCRIPT      -- sed script for the databrowser name
# CACHE_SIZE_SED_SCRIPT       -- sed script for the cache size


################################################################################
# Invoke this Makefile with a specific location argument:
#   make install location=test | make install location=production 
# 
# The config/Makefile_vars_~ file associated with this location must exist.

include config/Makefile_vars_$(location)


################################################################################
# Targets 

reboot_clear_cache: uninstall uninstall_cache install install_cache


reboot: uninstall install


install_UI: FORCE
	mkdir -p $(DATABROWSER_PATH)
	cp html/*.html $(DATABROWSER_PATH)
	cp -r docs style $(DATABROWSER_PATH)
	sed $(PYTHON_SED_SCRIPT) __Databrowser.cgi | \
		sed $(URL_PATH_SED_SCRIPT) | \
		sed $(DATABROWSER_PATH_SED_SCRIPT) | \
                sed $(OUTPUT_DIR_SED_SCRIPT) | \
                sed $(DATABROWSER_SED_SCRIPT) | \
                sed $(CACHE_SIZE_SED_SCRIPT) >  $(CGI_PATH)/$(DATABROWSER).cgi
	-chown $(OWNERSHIP) $(CGI_PATH)/$(DATABROWSER).cgi
	-chmod 755 $(CGI_PATH)/$(DATABROWSER).cgi


install: install_UI
	sed $(DATABROWSER_PATH_SED_SCRIPT) R/__Databrowser.R | \
		sed $(OUTPUT_DIR_SED_SCRIPT) | \
                sed $(DATABROWSER_SED_SCRIPT) | \
                sed $(ATTRIBUTION_SED_SCRIPT) > $(DATABROWSER_PATH)/$(DATABROWSER).R
	touch $(DATABROWSER_PATH)/TRANSCRIPT.txt
	touch $(DATABROWSER_PATH)/DEBUG.txt
	-chown $(OWNERSHIP) $(DATABROWSER_PATH)/*.txt
	-chmod 666 $(DATABROWSER_PATH)/*.txt
	sed $(DATABROWSER_SED_SCRIPT) behavior/__Mazama_databrowser.js > behavior/Mazama_databrowser.js
	cp -r behavior data_local images R $(DATABROWSER_PATH)
	rm $(DATABROWSER_PATH)/behavior/__Mazama_databrowser.js
	rm behavior/Mazama_databrowser.js
	ln -s $(DATA_DIR) $(DATABROWSER_PATH)/data


uninstall: FORCE
	rm -f $(CGI_PATH)/$(DATABROWSER).cgi
	rm -f $(DATABROWSER_PATH)/*.*
	rm -f $(DATABROWSER_PATH)/data
	rm -rf $(DATABROWSER_PATH)/behavior
	rm -rf $(DATABROWSER_PATH)/data_local
	rm -rf $(DATABROWSER_PATH)/docs
	rm -rf $(DATABROWSER_PATH)/images
	rm -rf $(DATABROWSER_PATH)/R
	rm -rf $(DATABROWSER_PATH)/style


install_cache: FORCE
	cp -r output* $(DATABROWSER_PATH)
	-chown $(OWNERSHIP) $(DATABROWSER_PATH)/output*
	-chmod 777 $(DATABROWSER_PATH)/output*


uninstall_cache: FORCE
	rm -rf $(DATABROWSER_PATH)/output*


clear_cache: FORCE
	rm -f $(DATABROWSER_PATH)/output*/*


reboot_from_svn: FORCE
	rm -rf LOCAL_INSTALL_VERSION
	mkdir LOCAL_INSTALL_VERSION
	cd ..; tar -czf $(DATABROWSER).tgz --exclude=.svn $(DATABROWSER)
	cd LOCAL_INSTALL_VERSION; tar -xzf ../../$(DATABROWSER).tgz
	cd LOCAL_INSTALL_VERSION/$(DATABROWSER); make reboot_clear_cache location=$(location)
	rm ../$(DATABROWSER).tgz
	rm -rf LOCAL_INSTALL_VERSION


################################################################################
# Targets for checking DEBUG and TRANSCRIPT logs

debug: FORCE
	cat $(DATABROWSER_PATH)/DEBUG.txt

transcript: FORCE
	cat $(DATABROWSER_PATH)/TRANSCRIPT.txt


################################################################################
# Targets for creating the distribution tarball

dist: FORCE
	cd ..; tar -czf $(DATABROWSER).tgz --exclude=.svn $(DATABROWSER)

dist_from_svn: FORCE
	cd ..; tar -czf GenericDatabrowser.tgz --exclude=.svn --exclude=.R* GenericDatabrowser

################################################################################
# Target for creating a new databrowser project

new_databrowser_project: dist_from_svn
ifeq ($(directory),)
	@echo "Argument missing:  directory=INSTALLATION_DIR"
else
ifeq ($(directory),"")
	@echo "Argument missing:  directory=INSTALLATION_DIR"
else
	mkdir $(directory)/branches
	mkdir $(directory)/tags
	mkdir $(directory)/trunk
	mkdir $(directory)/trunk/Data
	mkdir $(directory)/trunk/Development
	tar -xzf ../GenericDatabrowser.tgz -C $(directory)/trunk
	mv $(directory)/trunk/GenericDatabrowser $(directory)/trunk/Databrowser
endif
endif

FORCE:

