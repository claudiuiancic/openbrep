---
id: wiki.generated.pointcloud
type: wiki
category: other
commands: ["POINTCLOUD"]
task_types: [create, modify, repair]
priority: 70
source: GDL Reference Guide 28 (auto-generated)
status: draft
---

###### POINTCLOUD

POINTCLOUD "data_file_name" Generates a point cloud in the 3D model. A point cloud is a set of 3D points with color and other possible metadata stored per each point. data_file_name: the name of the loaded library part containing the point cloud data. Must be a string expression. Point clouds are not displayed by the Internal 3D Engine. The 2D is projected, using cutplanes to filter the unnecessary points.

CUTTING IN 3D