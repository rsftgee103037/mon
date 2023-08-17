import xml.etree.ElementTree as ET
def xml_to_dict(element):
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = xml_to_dict(child)
    return result
tree=ET.parse("setting.xml")
root=tree.getroot()
data=xml_to_dict(root)
month=int(data["month"])
monthly=int(data["money"])
intrest=int(data["interest"])
total=0
for i in range(month):
    total=total+monthly
    total=total*(1+intrest/100)
result=open("result.txt","w",encoding="utf-8")
result.write("......"+str(int(total)))
result.close()
print(int(total))