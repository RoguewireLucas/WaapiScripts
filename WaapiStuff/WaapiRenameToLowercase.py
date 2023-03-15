from waapi import WaapiClient, CannotConnectToWaapiException
import sys, re, os, argparse

# Define arguments for the script

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
    #Get Selected Objects
        options = {

             'return': ['id', 'name', 'parent']

        }
        results = client.call("ak.wwise.ui.getSelectedObjects", options= options)

    #Go thorugh selected objects

        for result in results.get("objects"):

    #Get children

            get_args = {
                "from": {"id": [result.get("id")]},
                "transform": [
                    {"select": ['children']}
                ]
            }
            options = {
                'return': ['id', 'name', 'parent']
            }
            childs = client.call("ak.wwise.core.object.get", get_args, options=options)['return']

    #Loop thorugh children and rename them
            
            for x in childs:
                childName = x.get("name").lower()
                print(childName)
                rename_args = {
                    "object" : x.get("id"),
                    "value" : childName
                }
                client.call("ak.wwise.core.object.setName",rename_args)
           



except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

except Exception as e:
    print(str(e))