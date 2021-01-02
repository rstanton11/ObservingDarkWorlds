# ObservingDarkWorlds

 This is a working directory for collaboration on the Observing Dark Worlds competition on Kaggle (this competition is no longer active) which can be found at :
        https://www.kaggle.com/c/DarkWorlds/overview/description
 
 There are 120 Skies in the test set, each sky contains galaxies each of which have an (x, y) coordinate between 0 and 4200 with (0, 0) being the bottom left corner.
 
 GOAL: predict the location of the halos (x, y) coordinates 
 
 Ellipticity:
  e1 : elongation along (x, y) axis
      positive represents horizontal 
      negative represents vertical
 
  e2 : elongation along the 45 or 135 degree axis
      positive is 45 degrees
      negative is 135 degrees
  
  Ellipticity of point (x,y) relative to (x',y') : 
  
    et = -(e1 cos(2phi) + e2 sin(2phi))
  
    phi = arctan((y-y')/(x-x'))
    
 Evaluating results : 
  method provided in DarkWorldsMetric.py
  
    m = F/1000 + G
    
    F = lowest sum of radial distances (in cases of multiple halos you get the lowest)
    G = SQRT[ (1/N)SUM(cos(phi)) + (1/N)SUM(sin(phi)) ]  -> they supply a reference point in the files and more information can be found at the evaluation page.
    
Submission : 
  format CSV
  must have 7 columns
  SkyId, x_halo1, y_halo1, x_halo2, y_halo2, x_halo3, y_halo3
  0.0 is the default value if there are less than 3 halos
 
