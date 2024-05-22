# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import RevitAPI
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import ICollection
from System.Collections.Generic import List
# Syntax: element_collection = List[ElementId](element_id) # element_id is the input of element ID(s)

doc = DocumentManager.Instance.CurrentDBDocument
ui = DocumentManager.Instance.CurrentUIDocument

active_view = doc.ActiveView

all_elements = FilteredElementCollector(doc).WhereElementIsNotElementType()  # All elements in the project
view_elements = FilteredElementCollector(doc, active_view.Id).WhereElementIsNotElementType()  # All elements in the Active View

element_data = []
for element in view_elements:
	element_data.append(element)

OUT = element_data
