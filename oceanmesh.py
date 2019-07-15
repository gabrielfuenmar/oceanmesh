"""
Created on Mon Jul 15 09:21:29 2019

Author: Gabriel Fuentes Lezcano
"""

import geopandas as gpd
import meshpy.triangle as triangle
import numpy as np

def round_trip_connect(start, end):
        """
        Parameters:
            start: First point of sequence
            end: Last point of sequence
        Returns:
            Facets
        Start and End of linering. Used to create a sequence of points."""
        return [(i, i+1) for i in range(start, end)] + [(end, start)]
        
def triang_export(path_to_ocean_scale,polygon_nu):
    """ Parameters: 
            path_to_ocean_scale:File name or path to IHO World Seas shapefile as 
            distributed in marineregions.org by Flanders Marine Institute. No 
            direct download is permitted as per License, hence no direct 
            availability through code. 
            Download the latest shapefile and use as input for this code.
            
            polygon_nu: Integer
            
            The polygon number as defined in the IHO World Seas 
            Shapefile from 0 to 21.
        
        Returns: 
            File of Numpy Arrays that includes an array of the 
            points and an array of the point combinations by index, that creates 
            every triangle mesh.
        
        Description:
            1. A shapefile with the IHO world seas polygons is read.
            2. An individual polygon from the former shapefile is used as basis
            for the creation of an exterior linering and facets .
            (order of linereings connection) that serves as input for 
            meshpy.triangle.
            3. Meshpy triangle result (points,facets) given as numpy arrays
            4. Refinement of meshpy triangles into 4 subdivisions for every 
            triangle taking the former point results.
            5.Values exported as numpy files with the number of the polygon as 
            the name.
            """
    gdf=gpd.read_file("{}.shp".format(path_to_ocean_scale))
    polygon=gdf.geometry.iloc[polygon_nu]
        
    linering=list(polygon.exterior.coords)
          
    facets=round_trip_connect(0,len(linering)-1)
    
    info=triangle.MeshInfo()
    info.set_points(linering)
    info.set_facets(facets)
    
    mesh=triangle.build(info,max_volume=0.2,min_angle=30)
    
    mesh_points=np.array(mesh.points)
    mesh_facets=np.array(mesh.facets)
    
    sub=triangle.subdivide_facets(4,mesh_points.tolist(),mesh_facets.tolist())
    
    sub_points=np.array(sub[0])
    sub_facets=np.array(sub[1])
    
    info.set_points(sub_points)
    info.set_facets(sub_facets)
    
    mesh2=triangle.build(info,max_volume=0.5,min_angle=30)
    
    mesh_points2=np.array(mesh2.points)
    mesh_tris2=np.array(mesh2.elements)
    
    np.savez("{}.npz".format(polygon_nu),mesh_points2,mesh_tris2)
