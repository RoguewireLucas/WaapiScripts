from waapi import WaapiClient, CannotConnectToWaapiException

# “try…except…” statement for handling Python exceptions. For instance, when the WAAPI connection fails.
try:
    # Use the default address to connect to Wwise. You can change the port as needed.
    with WaapiClient() as client:

        # All WAAPI arguments are in JSON format, no matter they are passed in or sent back. Use the dictionary to define the printout message (Hello Wwise!)
        new_object = {
            "name": "New_Object",
            "parent": parent_guid, 
            "type": "Sound",
        }
        # Make a remote call to ak.soundengine.postMsgMonitor, then pass in the arguments you just defined
        client.call("ak.wwise.core.object.create", new_object)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")