# Ocean-Sailing-Routes

A module that generates feasible oceanic routes for vessels to be used as input for routing and network problems.
Utilizes IHO Oceans shapefile (Flanders Marine Institute (2018). IHO Sea Areas, version 3) and produces triangle meshes for the routes vessels could use.

**Disclaimer: The routes are not intended to be used for navigation purposes. No responsibility will be taken by the author in this regard.**

The code doesn't include the shapefile as per Licence requirements by Flanders Marine Institute. The file could be downloaded for free at http://www.marineregions.org/downloads.php then IHO Sea Areas.

Dependencies: 
geopandas 0.5.0
numpy 1.16.4
meshpy 2018.2.1

Input: 
      
  path_to_ocean_scale: File name or path to IHO World Seas shapefile as 
  distributed in marineregions.org by Flanders Marine Institute. No 
  direct download is permitted as per License, hence no direct 
  availability through code. 
  Download the latest shapefile and use as input for this code.
  
  polygon_nu: The polygon number as defined in the IHO World Seas 
  Shapefile from 0 to 21.

Output: 
  
  File of Array of Numpy Array that includes an array of the 
  points and an array of the point combinations by index, that creates 
  every triangle mesh.

Code development:
  
  1. A shapefile with the IHO world seas polygons is read.
  2. An individual polygon from the former shapefile is used as basis
  for the creation of an exterior linering and facets .
  (order of linereings connection) that serves as input for 
  meshpy.triangle.
  3. Meshpy triangle result (points,facets) given as numpy arrays
  4. Refinement of meshpy triangles into 4 subdivisions for every 
  triangle taking the former point results as input
  5.Values exported as numpy files with the number of the polygon as 
  the name.

Credits: Gabriel Fuentes Lezcano

Licence: MIT License

Copyright (c) 2019 Gabriel Fuentes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
© 2019 GitHub, Inc.
