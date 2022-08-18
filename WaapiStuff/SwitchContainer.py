from unicodedata import name
from waapi import WaapiClient, CannotConnectToWaapiException

# “try…except…” statement for handling Python exceptions. For instance, when the WAAPI connection fails.
try:
    # Use the default address to connect to Wwise. You can change the port as needed.
    with WaapiClient() as client:

        options = {

             'return': ['id', 'name', 'parent']

        }

        result = client.call("ak.wwise.ui.getSelectedObjects", options= options)
        #print(result)
        
        for x in result.get("objects"):
         
            SelectedObjectId = x.get("id")
            SelectedObjectName = x.get("name")
            ObjectParent = x.get("parent").get("id")
            NewName = SelectedObjectName + "_SwitchContainer"
        
            new_object = {
                "parent": ObjectParent, 
                "type": "SwitchContainer",
                "name": NewName
            }
    

            # Make a remote call to ak.soundengine.postMsgMonitor, then pass in the arguments you just defined
            NewSwitch = client.call("ak.wwise.core.object.create", new_object)
            NewSwitchId = NewSwitch.get("id")

            #Assign Switch Group
            switch_properties= {
                "object": NewSwitchId,
                "reference": "SwitchGroupOrStateGroup",
                "value": "SwitchGroup:Oracle_Gender"
            }

            client.call("ak.wwise.core.object.setReference", switch_properties)
            
            #Assign Default Switch
            default_switch= {
                "object": NewSwitchId,
                "reference": "DefaultSwitchOrState",
                "value": "\Switches\Default Work Unit\Oracle_Gender\Female"
            }
            client.call("ak.wwise.core.object.setReference", default_switch)
            
            #Make Selected Object into Switch Child (of mine hehe)
            new_parent = {
                "object": SelectedObjectId,
                "parent": NewSwitchId
            }

            client.call("ak.wwise.core.object.move", new_parent)
            
            #Might want to do an if state gettin _M vs _F at the end of a file name to assign it
            assign_switch_state= {
                "child": SelectedObjectId,
                "stateOrSwitch" : "\Switches\Default Work Unit\Oracle_Gender\Female"
            }

            client.call("ak.wwise.core.switchContainer.addAssignment", assign_switch_state)

except CannotConnectToWaapiException:

    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

#SelectedObjectId = result.get("objects")[0].get("id")
#SelectedObjectName = result.get("objects")[0].get("name")
#ObjectParent = result.get("objects")[0].get("parent").get("id")