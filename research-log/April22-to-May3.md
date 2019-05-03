_April 22, 2019_

**Links:**
[MER NavCam data archives](https://pds-imaging.jpl.nasa.gov/volumes/mer.html)

**information:**
Unknown mosaics on PDS? are they vertical projections. Or perspective projections.  They are from Navcam

(Spirit) 420 are vertical projections.
(Opportunity) 840 are vertical projections 

ICER - Image compression algorithm

All the cameras are monochromatic except for the Pancam. The camera detectors are 1024 x 1024 px. 
Navcam is a stereo pair (2 cameras) Field of view of 45°

Ref 13 

The Pancam was used to image the surface and sky of MArs around two landing sites. The images were used to select desirable targets for composition analysis. It also supported selection of travel paths for the Rover and development of a landing site map. 

The Navcam was primarily ised for navigation purposes and general site characterization (360° panoramic images and targeted images of interest, including terrain not viewable by the Hazcams).

Raw -> Edited -> Calibrated -> Resampled -> Derived  (level 1-C, 2, and 3 for Nasa, and Level 5 for CODMAC)

Level 3 are where Geophysical parameters mapped onto uniform space-time grids.

CCD Charge-Coupled Device.

A PDS label is object-oriented and describes the objects in the data file. The PDS label contains keywords for product identification. The label also contains descriptive information needed to interpret or process the data in the file.

Mosaic RDR - derived from multiple EDR or RDR data h they can be derived from single data products.
Geometric position within the site. 
Projections:
-CYL Cylindrical 
-PER Camera Point Perspective 
-CYP Cylindrical-Perspective 
-POL Polar (This could work, Concentric circles represent constant projected elevation. Mars nadir is at the convergent center and the horizon is corrected for lander tilt. North is up).
-VRT Vertical projection. (This could work too. It assumes that the field is a plane tanget to the Martian surface with up pointing north. This is not an orthorectified rendering but was found to be useful for rapid initial orientation).
-ORT Orthographic
-ORR Ortho-rectified 

There are many uses for the image mosaics.  First is  the assembly of small pieces into a larger field of view.  This includes tilting the camera model in the Mars coordinate system to model a tilted spacecraft, which should result can in mosaics with a level horizon beginning and ending atMars north.  The science teams can use these products to orient themselves.  Another application is to provide to the rover planning team each Sol a small stereo mosaic which is registered to a fixed reference image.  This permits the triangulation of waypoints for the next Sol’s maneuvering.

MILP software to create mosaics. 

SITE_FRAME = North, East, Nadir. 

There are two coordinate frames for MER rover: Mechanical frame (for the rover design) and Traverse Coordinate Frame (used by navigation and imaging).

Z -> Mars spin axis, pointing toward Martial North Pole
X -> Vector lies in the Mars equatorial plane and intersects the prime meridian
Y -> Vector lies in the Mars equatorial plane and completes a right handed coordinate system.

---
_April 30, 2019_

**Papers** 
- Learning deep representations for ground-aerial geolocalization by Tsung, Yin, Serge, and James.
- Geo-localization of street views with aerial image databases by Mayank, Harpreet, Hui, and Kostas.

**links** 
[NNs in practice](https://www.dataversity.net/deep-learning-technology-brings-neural-networks-practical-application/)

**information:**
THe PDS GEosices Node created a corrected version of each Rover traverse by applrying linear interpolation to positions between connected points. (When possible)

The combined visual system and the navigation system are connected in a way that allows rovers (or other devices) to self-localize without a GPS, and to avoid collisions using an “anticipation process,” rather than a reaction process. (obsolete problem?)

Localization: Merging orbital maps with surface-perspective imagery
A significant challenge faced during the execution of lunar or planetary surface missions is that of localizing a perspective with respect to satellite imagery - something we on Earth take for granted in the age of GPS.

Nasa team, they need about 12 hours to localize a robot on the surface of Mars when it lands.

Mars could enough in resolution what they do in a virtual environment. It can be imporved using 3d reporjections.

Datasets: Google-stret-view and 45° aerial view images from some cities. (Mars on Earth could be an option)
The major challenge is simply to establish ground-truth correspondences between street-level and aerial views.
In street view: 15 x 15 meters (256 x 256px)

---
_May 3, 2019_

**Papers** 
- Localization of planetary exploration rovers with orbital imaging: a survey of approaches by Evangelos, Antonios, and Giafranco.
- Seeker-autonomous long range rover navigation for remote exploration by Mark, Andrew, Estelle, etc.

**Links:**
[ESA datasets](http://robotics.estec.esa.int/datasets/all-datasets/)
[Official ESA data](https://earth.esa.int/web/guest/home;jsessionid=0A6B967A3E854ADB0BECC8A3D59AC0C0.jvm1)
[Gianfranco visentin](https://www.researchgate.net/profile/Gianfranco_Visentin)

**Information:**
The rover should be apt to globally localize itself on the Martian surface. Due to the absence of Global NavigationS atellite System (GNSS) on Mars, the most suited approach is the blending of information stemming from ground rovers and orbital imagery.

The localization of a space exploratory roveron  a  georeferenced  orbital  image  is  equivalent  to  globallocalization  and,  hence,  is  considered  sufficient.

The  global  localization  of  Mars  rovers  at  their  landingsite  has  been  employed  by  Direct  to  Earth  (DTE)  radiosignals,  via  two-way  Doppler  tracking  [36]  or  via  descentimage  analysis,  as  reviewed  in  Section  II-A.

Orbital  and  rover  image networks should be connected through tie points. Moreover, it is difficult to extract such features due  to  great  differences  in  the  scaling  and  viewing  angle.

According to some authors, the most sufficient datasets are the ones produced by the ESA on the Chilean Atacam Desert (SEEKER, SAFER) The selected areas in the chilean dessert are considered to be the most Mars-like regions on Earth, . Atacama dataset.

Another  source  of  data  could  be  the  actual  MER  and MSL  programs,  but  since  the  stereo  images  are  sparse(at least sparser compared the actual rover’s frame-rate) and  no  groundtruth  exists,  then  the  Atacama  datasets are the most appropriate.

The method should be tested on different scenarios with different trajectories and surrounfing environments. (Pangu, 3DRov)

One of the issues that arise from the sexcisting methods is the lack  of  robust  techniques  to  overcome  the  manual  tie  point selection among the orbital and rover imagery.

---

**Approaches**
* Learn to detect Rover on HiRISE images (No feasible, They are orbiting Mars, no tracking Rover)
* Detect rocks in surface images and match them in orbial images. (Everyone does this)
* Automatically match surface image with the orbital images (create the dataset is so expensive in time)
	- There are 673 vertical projections that can be used, but need to be matched manually with the orbital images (very difficult due to anlges and orientation)
	- There is a commercial Mars surface render that can be used to create simulated data, $49 USD
	- There is street-view of "Mars on Earth" and posiblle aerial view, need to be processed. 
	- Posible dataset using Atacama dessert as "like-Mars" containing stereo images matched with orbital images (simulating HiRISE)
