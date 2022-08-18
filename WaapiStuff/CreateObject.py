from unicodedata import name
from waapi import WaapiClient, CannotConnectToWaapiException

# “try…except…” statement for handling Python exceptions. For instance, when the WAAPI connection fails.
try:
    # Use the default address to connect to Wwise. You can change the port as needed.
    with WaapiClient() as client:

        result = client.call("ak.wwise.ui.getSelectedObjects")
        #print(result)
        
        # Get Selected Object!
        SelectedObject = result.get("objects")[0].get("id")

        new_object = {
            "parent": SelectedObject, 
            "type": "Sound",
            "name": "New_Object"
        }
        # Make a remote call to ak.soundengine.postMsgMonitor, then pass in the arguments you just defined
        client.call("ak.wwise.core.object.create", new_object)

except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")