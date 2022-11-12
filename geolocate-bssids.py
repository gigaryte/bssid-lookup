#!/usr/bin/env python3
import re
import time
import json
import wloc
import logging
import argparse
import requests
from queue import Queue
from threading import Thread
from urllib3.exceptions import InsecureRequestWarning

logging.basicConfig(level=logging.INFO)
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def doLookup(q, lookups, idx):
    """Thread target that pulls the next set of BSSIDs to query, then does the query

    """

    batch = []
    while not q.empty() and len(batch) < 10:
        batch.append(q.get())

        if len(batch) == 10:

            logging.debug("Batch len == 10, querying")
            results = wloc.QueryBSSIDs(batch)
            queryTime = int(time.time())

            for result in results:

                #lat, lon = results[result]
                #lookups[idx].append((queryTime, result, lat, lon))

                with open(args.output_file, 'a') as f:
                    f.write(f"{queryTime}\t{result}\t{' '.join([str(x) for x in results[result]])}\n")

            #Account for all the finished tasks we've done here
            for i in range(len(batch)):
                q.task_done()

            batch = []


    logging.debug(f"Had {len(batch)} remaining, doing last query")
    if len(batch):
        results = wloc.QueryBSSID(batch)
        queryTime = int(time.time())

        for result in results:

            lat, lon = results[result]
            #lookups[idx].append((queryTime, result, lat, lon))
            with open(args.output_file, 'a') as f:
                f.write(f"{queryTime}\t{result}\t{lat},{lon}\n")

    #Account for the last batch of finished tasks
    for i in range(len(batch)):
        q.task_done()

    return

def geolocate(bssidSet, numThreads):
    """queries the apple location services API using the macs from the preprocessed file

    Args:
        numThreads: number of threads to use to query Apple
    """

    results = {}
    #Queue to put MACs in for worker threads
    q = Queue()
    #Dictionary to place each thread's results
    lookups = {}

    #populate queue
    for bssid in bssidSet:
        q.put(bssid)

    #start thread pool working on it
    logging.debug(f"Starting {numThreads} worker threads")
    for i in range(numThreads):
        lookups[i] = []
        worker = Thread(target=doLookup, args=(q,lookups, i))
        worker.daemon = True
        worker.start()

    q.join()

    logging.debug(f"Finished with lookups, got {sum([len(lookups[i]) for i in lookups])} results")

    #iterate over the results the worker processes retrieved and add them to the
    #results dict
    for i in lookups:
        for result in lookups[i]:
            timestamp, bssid, lat, lon = result

            #This was something we actually queried, so fill in the object's
            #values
            if bssid in bssidSet:
                results[bssid] = lat, lon

        with open(args.output_file, 'a') as f:
            for bssid in results:
                f.write(f"{bssid}\t{results[bssid][0]},{results[bssid][1]}\n")
 
    return

def main(args):

    #clear file
    with open(args.output_file, 'w') as f: pass

    bssidSet = set()

    with open(args.bssid_file) as f:
        for line in f:
            l = line.strip()
            bssidSet.add(l)


    geolocate(bssidSet, args.numthreads)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bssid_file", 
        help="File of new-line delimited BSSIDs")
    parser.add_argument("-o", "--output-file", required=True,
        help="Output file name to write results")
    parser.add_argument("-n", "--numthreads", type=int, default=10,
        help="Number of threads")
    args = parser.parse_args()

    main(args)
