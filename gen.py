import xml.etree.ElementTree as ET
import shutil
import os
import os.path
import sys;

vtm = ET.parse('SyntaxTree.VisualStudio.Unity.Vsix.Item..vstman')
vtmRoot = vtm.getroot()

inputtedName = input('Name: ')

if len(inputtedName) == 0:
	os._exit(0)
if not inputtedName.isalpha():
	os._exit(0)

ns = {
	'vtm': 'http://schemas.microsoft.com/developer/vstemplatemanifest/2015',
	'vt': 'http://schemas.microsoft.com/developer/vstemplate/2005'
}

def trace(root):
	for container in root.findall('vtm:VSTemplateContainer', ns):
		path = container.find('vtm:RelativePathOnDisk', ns).text
		filename = container.find('vtm:RelativePathOnDisk', ns).text
		for header in container.findall('vtm:VSTemplateHeader', ns):
			for data in header.findall('vt:TemplateData', ns):
				name = data.find('vt:Name', ns).text
				desc = data.find('vt:Description', ns).text
				icon = data.find('vt:Icon', ns).text
				protype = data.find('vt:ProjectType', ns).text
				defname = data.find('vt:DefaultName', ns).text

				print(f'{path}\n{filename}\n{name}\n{desc}\n{icon}\n{protype}\n{defname}\n')

def indent(root, level=0):
    i = "\n" + level*"  "
    if len(root):
        if not root.text or not root.text.strip():
            root.text = i + "  "
        if not root.tail or not root.tail.strip():
            root.tail = i
        for root in root:
            indent(root, level+1)
        if not root.tail or not root.tail.strip():
            root.tail = i
    else:
        if level and (not root.tail or not root.tail.strip()):
            root.tail = i

def createVtm(name):
	attrib = {
		'TemplateType': 'Item',
		'Locale': '1033'
	}

	containerE = ET.SubElement(vtmRoot, 'ns0:VSTemplateContainer', attrib)
	
	pathE = ET.SubElement(containerE, 'ns0:RelativePathOnDisk')
	filenameE = ET.SubElement(containerE, 'ns0:TemplateFileName')
	
	headerE = ET.SubElement(containerE, 'ns0:VSTemplateHeader')
	dataE = ET.SubElement(headerE, 'ns1:TemplateData')

	nameE = ET.SubElement(dataE, 'ns1:Name')
	descE = ET.SubElement(dataE, 'ns1:Description')
	iconE = ET.SubElement(dataE, 'ns1:Icon')
	protypeE = ET.SubElement(dataE, 'ns1:ProjectType')
	defnameE = ET.SubElement(dataE, 'ns1:DefaultName')

	pathE.text = f'CSharp\\1033\CSharp {name}'
	filenameE.text = f'CSharp {name}.vstemplate'

	nameE.text = f'CSharp {name}'
	descE.text = f'Unity {name} in CSharp language'
	iconE.text = f'icon.ico'
	protypeE.text = 'CSharp'
	defnameE.text = f'New{name}'

	indent(vtmRoot)
	return vtmRoot

def createVt(name):
	attrib = {
		'Version': '2.0.0',
		'Type': 'Item',
		'xmlns:ns0': 'http://schemas.microsoft.com/developer/vstemplate/2005'
	}

	vtRoot = ET.Element('ns0:VSTemplate', attrib)
	dataE = ET.SubElement(vtRoot, 'ns0:TemplateData')

	nameE = ET.SubElement(dataE, 'ns0:Name')
	descE = ET.SubElement(dataE, 'ns0:Description')
	iconE = ET.SubElement(dataE, 'ns0:Icon')
	protypeE = ET.SubElement(dataE, 'ns0:ProjectType')
	defnameE = ET.SubElement(dataE, 'ns0:DefaultName')

	contentE = ET.SubElement(vtRoot, 'ns0:TemplateContent')
	itemE = ET.SubElement(contentE, 'ns0:ProjectItem', {
		'SubType': 'Code',
		'ReplaceParameters': 'true',
		'TargetFileName': '$fileinputname$.cs',
	})

	nameE.text = f'CSharp {name}'
	descE.text = f'Unity {name} in CSharp language'
	iconE.text = f'icon.ico'
	protypeE.text = 'CSharp'
	defnameE.text = f'New{name}'

	itemE.text = f'New{name}.cs'

	indent(vtRoot)
	return vtRoot

vtm = ET.ElementTree(createVtm(inputtedName))
vt = ET.ElementTree(createVt(inputtedName))

dir = f'CSharp/1033/CSharp {inputtedName}'

if not os.path.exists(dir):
	os.mkdir(dir)

if os.path.exists('icon.ico'):
	shutil.copyfile('icon.ico', f'{dir}/icon.ico')

vtm.write(f'SyntaxTree.VisualStudio.Unity.Vsix.Item..vstman')
vt.write(f'{dir}/CSharp {inputtedName}.vstemplate')

if os.path.exists(f'{dir}/New{inputtedName}.cs') is False:
	open(f'{dir}/New{inputtedName}.cs', 'w')