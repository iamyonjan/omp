"""
    Created on August 18, 2013

    @author: Surendra Lama

    [Module 'constants"]
        Parent packages - cfg -> grs
        Sub-packages - None

    Description:
    This module is considered for initializing
    definitions for the system.

"""
#=================================================

#START [Global Definitions] ======================

global ROOTFRAMENAME
#global SYSLOGFRAMENAME
#global EVENTLOGFRAMENAME

global PROJECTDIR
global DATAPATHNAME
global CLASSIFIERDIRNAME
#global SYSTEMLOGDIRNAME
global FRAMESIZE
global FACEDETECTCLASSIFIER
global FISTDETECTCLASSIFIER
global PALMDETECTCLASSIFIER
global NNTRAINERFILENAME
global MODELNAME
#global SYSLOGFILENAME
#global EVENTLOGFILENAME

#END [Global Defintions] =========================
global SKINDIRNAME
global MAXCAMERAINDEX
global TRAINDATAPATH
global OUTPUTLISTS
global FILEINDEX
global OUTPUTCLASSCOUNTS
global SKINFILENAME
#=================================================
#START [Global Assign] ===========================

ROOTFRAMENAME = "GRS-Dev"
PROJECTDIR = "D:/workspace/python/omp/grs/"
DATAPATHNAME = "data/"
CLASSIFIERDIRNAME = "classifier/"
SKINDIRNAME = "skins/"
SKINFILENAME = "skin_002.jpg"
TRAINDATAPATH = "D:/grs_data/"
FACEDETECTCLASSIFIER = "haarcascade_frontalface_default.xml"
FISTDETECTCLASSIFIER = "fist.xml"
PALMDETECTCLASSIFIER = "palm.xml"
NNTRAINERFILENAME = "neuralnetwork.xml"
OUTPUTCLASSCOUNTS = 3
MODELNAME = "model_own_fist_a.xml"
OUTPUTLISTS = {
               'fist': [1., 0., 0.],
               'open': [0., 1., 0.],
               'none' : [0., 0., 1.]
               }
FILEINDEX = 0
FRAMESIZE = (640, 480)
#SYSLOGFILENAME = "sys_log.txt"
#SYSLOGFRAMENAME = "System Log"
#EVENTLOGFILENAME = "event_log.txt"
#EVENTLOGFRAMENAME = "Event Log"

MAXCAMERAINDEX = 3

#END [Global Assign] =============================

__all__ = [
           "ROOTFRAMENAME",
           "DATAPATHNAME",
           "CLASSIFIERDIRNAME",
           "FACEDETECTCLASSIFIER",
           "MAXCAMERAINDEX",
           "NNTRAINERFILENAME",
           "PROJECTDIR",
           "OUTPUTLISTS",
           "FILEINDEX",
           "TRAINDATAPATH",
           "FISTDETECTCLASSIFIER",
           "PALMDETECTCLASSIFIER",
           "OUTPUTCLASSCOUNTS",
           "SKINDIRNAME",
           "SKINFILENAME",
           "MODELNAME",
           "FRAMESIZE"
           ]
