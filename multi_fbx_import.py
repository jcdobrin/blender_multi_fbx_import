import bpy
import os
import pprint

def recurLayerCollection(layerColl, collName):
	found = None
	if (layerColl.name == collName):
		return layerColl
	for layer in layerColl.children:
		found = recurLayerCollection(layer, collName)
		if found:
			return found
		
C = bpy.context

for root, dir, files in os.walk("<PATH TO FBX FILES>"):
	path = root.split(os.sep)
	for file in files:
		print(root+"\\"+file)
		
		num = file[5:7] #this is a 2 digit ident number for grouping files in my naming convention
		obj_name = file

		layer_collection = bpy.context.view_layer.layer_collection
		layerColl = recurLayerCollection(layer_collection, num)
		if collection is None:
			bpy.context.blend_data.collections.new(name=num)
			layerColl = recurLayerCollection(layer_collection, num)

		bpy.context.view_layer.active_layer_collection = layerColl

		bpy.ops.import_scene.fbx(filepath = root+"\\"+file)
		obj = C.view_layer.objects.active
		mat = bpy.data.materials.get(num)
		bpy.data.objects[obj_name].children[0].children[-1].data.materials.append(mat)