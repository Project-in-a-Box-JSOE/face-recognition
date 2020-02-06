"""
ECE196 Face Recognition Project
Author: Brian Henriquez

This file is used to ensure the integrity of the images directory and whether or not
the files have been distributed properly by some file splitter.

Please do not modify this file.
"""
from hashlib import md5
from collections import defaultdict
from os import listdir, path
import sys
import argparse
import tqdm

# Constants
class ndirectory:
    TEST = 'test' # Name of testing directory
    TRAIN = 'train' # Name of training directory
    VAL = 'validation' # Name of validation directory

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def createParser():
    ''' Creates the relevant parser '''
    parser = argparse.ArgumentParser(description="Compares a source and destination directory's contents. Checks for signs of an invalid destination directory structure")
    parser.add_argument('source', metavar="S", type=str, nargs='?', help="source directory")
    parser.add_argument('destination', metavar="D", type=str, nargs='?', help="destination directory")
    parser.add_argument('--checksum', dest='chkFlag', action='store_true', help="enables checksum check of files (Experimental)")
    parser.add_argument('--verbose', dest='vFlag', action='store_true', help="turns on verbose output")
    args = parser.parse_args()

    # Check inputs for validity
    if(args.source is None or args.destination is None):
        print("Please enter valid directories...")
        sys.exit()
    if(args.source == "" or not path.isdir(args.source)):
        print("Passed source directory ({}) is invalid.".format(args.source))
        sys.exit()
    if(args.destination == "" or not path.isdir(args.destination)):
        print("Passed destination directory ({}) is invalid.".format(args.destination))
        sys.exit()
    if(args.chkFlag):
        print(bcolors.WARNING + "Warning: Running file checker with checksum validation will drastically increase check time." + bcolors.ENDC)

    # Add final '/' if necessary to files
    if(not args.source.endswith('/')):
        args.source += '/'
    if(not args.destination.endswith('/')):
        args.destination += '/'

    return args

def dirEnum(sourceDir, outDir):
    ''' Enumerates files from both directories in a structured manner '''
    print("Performing initial source to destination check...")

    # Enumerate sourceDir classes
    classNames = listdir(sourceDir)
    sourceEnum = defaultdict(dict)           # class -> filename
    failures = []                            # stores problematic files

    # For each class name walk through the files and collect file paths
    for classDir in classNames:
        curParent = sourceDir + classDir + '/'
        if path.isdir(curParent): # only consider class directories (not README, etc.)
            curDirFilepaths = listdir(curParent)
            for indFilename in curDirFilepaths:
                sourceEnum[classDir][indFilename] = True

    # Do the same with the output dir
    potDirs = [ndirectory.TRAIN, ndirectory.TEST, ndirectory.VAL]
    potDirs = [outDir + potDir + '/' for potDir in potDirs]
    for curDir in potDirs:
        if vFlag:
            print("\tChecking {}...".format(curDir))
        for classDir in classNames:
            curParent = curDir + classDir + '/'
            curDirFilepaths = listdir(curParent)
            for indFilename in curDirFilepaths:
                curFilepath = curParent + indFilename
                if sourceEnum[classDir].get(indFilename, None) is None:
                    # file in result not in original
                    print(bcolors.FAIL + "Eror: Found file {} that was not in source directory.".format(curFilepath) + bcolors.ENDC)
                    failures.append("NEWFILE:\t\t" + curFilepath)
                elif sourceEnum[classDir][indFilename] != True:
                    # File was already found before
                    print(bcolors.FAIL + "Error: Duplicate files {} & {} found.".format(curFilepath, sourceEnum[classDir][indFilename]) + bcolors.ENDC)
                    failures.append("DUPLICATES:\t\t" + curFilepath + "\t\t" + sourceEnum[classDir][indFilename])
                else:
                    # File is newly matched to source file
                    sourceEnum[classDir][indFilename] = curFilepath

    # Perform reverse search now for missing files in dest
    print("\tPerforming missing file check...")
    for className in sourceEnum:
        classDict = sourceEnum[className]
        for fileName in classDict:
            if classDict[fileName] == True:
                # file hasn't been copied to dest
                print(bcolors.FAIL + "Error: Source file {} not found in destination directory.".foramat(sourceDir + className + '/' + fileName))
                failures.append("MISSINGFILE:\t\t{}".format(sourceDir + className + '/' + fileName))

    # Return lookup table for subsequent checksum check
    return sourceEnum, failures

def checksumVal(inTable, sourceDir, errorList):
    ''' Performs the checksum check on a file lookup table '''
    if vFlag:
        print("Performing checksum validation of files...")

    # Calculate list size for tqdm init
    size = 0
    for firstKey in inTable:
        size += len(list(inTable[firstKey].keys()))

    # Comb through files and compare md5
    for _ in tqdm.tqdm(range(size)):
        for className in inTable:
            classDict = inTable[className]
            for fileName in classDict:
                destFile = classDict[fileName]
                if destFile is None:
                    continue
                else: # check md5
                    destOpened = open(destFile, 'rb')
                    sourceOpened = open(sourceDir + className + '/' + fileName, 'rb')

                    # Process first kb for checks
                    destMD5 = md5(destOpened.read()).hexdigest()
                    srcMD5 = md5(sourceOpened.read()).hexdigest()

                    # Perform full check only if discrepancy found
                    if destMD5 != srcMD5:
                        print(bcolors.FAIL + "Eror: Found file {} does not match source {} contents." .format(destFile, sourceDir + className + '/' + fileName))
                        errorList.append("MD5 MISMATCH:\t\t{}\t\t{}".format(destFile, sourceDir + className + '/' + fileName))

                    # Close streams
                    destOpened.close()
                    sourceOpened.close()

if __name__ == "__main__":
    # Receive arguments
    args = createParser()
    vFlag = args.vFlag

    # Go through file checking
    resTable, errorList = dirEnum(args.source, args.destination)

    # Check checksums if requested
    if args.chkFlag:
        errorList = checksumVal(resTable, args.source, errorList)

    if len(errorList) == 0:
        print("Done.")
    else:
        print("Finished with {} errors".format(len(errorList)))