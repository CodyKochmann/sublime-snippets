example_output="""
<snippet>
    <content><![CDATA[Type your snippet here]]></content>
    <!-- Optional: Tab trigger to activate the snippet -->
    <tabTrigger>xyzzy</tabTrigger>
    <!-- Optional: Scope the tab trigger will be active in -->
    <scope>source.python</scope>
    <!-- Optional: Description to show in the menu -->
    <description>My Fancy Snippet</description>
</snippet>
"""

def random_string(length=32,upper=True,lower=True,digits=True):
    # Generates a random string with selectable characters
    # By: Cody Kochmann
    from random import choice
    chars = ""
    if upper:
        chars+="QWERTYUIOPASDFGHJKLZXCVBNM"
    if lower:
        chars+="qwertyuiopasdfghjklzxcvbnm"
    if digits:
        chars+="1234567890"
    return(''.join(choice(chars) for _ in range(length)))

def multiline_input(prompt=""):
    print(prompt+"")
    out=[]
    len_before_previous=1
    previous_len=1
    while previous_len > 0 and len_before_previous>0:
        current=raw_input("")
        if current != "":
            out.append(current)
        len_before_previous=previous_len
        previous_len=len(current)
    out="\n".join(out)
    return(out)

def remove_periods(s=""):
    if "." in s:
        return("".join(s.split(".")))
    return(s)

def get_username():
    import getpass
    return(str(getpass.getuser()))

snippet_content=multiline_input("Type your snippet (2 blank lines to submit):")
tab_trigger=raw_input("Enter the tab trigger:\n")
extension_type=remove_periods(raw_input("Enter the file extension this will apply to:\n"))
snippet_description=raw_input("Enter the description:\n")

output="""
<snippet>
    <content><![CDATA[%s]]></content>
    <!-- Optional: Tab trigger to activate the snippet -->
    <tabTrigger>%s</tabTrigger>
    <!-- Optional: Scope the tab trigger will be active in -->
    <scope>source.%s</scope>
    <!-- Optional: Description to show in the menu -->
    <description>%s</description>
</snippet>
""" % (snippet_content, tab_trigger, extension_type,snippet_description)

user_path = "/Users/%s/Library/Application Support/Sublime Text 3/Packages/User" % (get_username())

filename="%s/%s.%s.sublime-snippet" % (user_path,random_string(),extension_type)

with open(filename,'w') as f:
    f.write(output)
    print("\ncreated: %s"%(filename))

print("\n%s\n"%(output))