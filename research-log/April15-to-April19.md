_April 15, 2019_
**papers:**
- Mars rover localization based on feature matching between ground and orbital imagery by Kaichang, Zhaoquin, and Zongyu

**links:**
[HiRISE map](https://www.uahirise.org/hiwish/browse)
[Mars interactive data](https://an.rsl.wustl.edu/)

**information:**
The viewing angles of ground and orbital imagery differ by about 90°, and there is also a large difference between their resolution leves. This makes extremely difficult to match ground with orbital images.

Rocks are one of the major features found in ground based Rover images, large rocks can be identified within HiRISE imagery. 

Position is defined in local site frame.

Navcam - FFL (stereo images) and XYL (derived 3D point-cloud data)
HiRISE - EDR (raw data) and RDR (processed data)

1st - 3D mapping on **Navcam** taken at one position to generate 3D point cloud, a DEM (digital elevation model) and an orthophoto (image geometrically corrected, the scale is uniform and utilized in the same manner as a map. Can be used to measure true distances of features within the photo). **HiRISE** imagery preproced using histogram streching and a Gaussian filter to enhance the image and remove any noise effect.

2do - Feature extraction, large rocks, and keyponts are extracted from ground-image.derived 3D point clouds and he ortophoto. Same points are also extracted from the HiRISE images.

3rd . Feature matching for rocks (Rocky areas) or keypoints (Outcrop areas) is perfomed.

By establishing similarity ransformation model between the local Rover site freame and the HiRISE frame using the matched feature, the Rover position can be positioned to the HiRISE image.

Isolated dark pixxels in orbital images are identified as rocks. 

It is impossible to match individual rocks between ground and orbital data, instead we must look at rock distribution patterns to determine the correspondece between these two uniques datasets

Since two sets of rocks are all represented in a ground coordinate system, their relationship can be described using asimilarity transformation with translation rotation and scale parameters (RANSAC)

Transform all the rock positions from Rover data (local site frame) to the orbital image coordinate frame with the similarity transformation model determined by the two rocks (SIFT)

---
_April 16, 2019_
**papers:**
- Automated detection of geologial landforms on Mars using CNNs by Leon, Christopher, Alexander, and Stephen.
- Towards autonomous Mars Rover localization: operations in 2005 MER mission and new developments for future missions. 
- A novel deep neural network architecture for Mars visual navigation by Jiang, Yuanqing, and Gaunghui.
- SPOC: Deep learning-based terrain classification for Mars Rover missions by Brandon, Jeremie, Ryan, Masahiro, and Matt.

**information:**
Rocks detected from both orbital and ground imagery serve as tie points for Rover localization. From orbital images; Rocks are extracted based on brigthness values and the shape of dark spots. 

Wherever we observed large features (e.g. craters), we used an alternative localization method, ccomparission of an orbital image based map and orthoimages generated from Rover imagery. 

Oucrop layers and geological features investigated by the Rover are also labeled.

The problem is with long-range Rover transverses. 

During the MER mission the Rover are primarly localized on board by IMU, wheel-odometry, and sun-sensing technology. VO technique has been effectively applied on board over short distances to correct slippage erros. BA methos has been perfomed on Earth to acheive a high accuracy solution to the entire Rover transverse.

Autonomous navigation algorithms are essential for Mars Rovers to avoid risky areas (such as craters, high montains, and rocks) and reach target points precisely and effectively. 

EDL - Entry, Descent, and Landing 

Prior knowledge about the obstacles in maps is prerequisite for Neural Networks to work. 

Monte Carlo simmulations?

---
_April 17, 2019_

**links:**
[AI learns to guide planetary Rovers without GPS](https://frontierdevelopmentlab.org/blog/2018/9/28/in-the-news-ai-learns-to-guide-planetary-rovers-without-gps)
[FDL 2018 team 2 resource](https://en.calameo.com/read/005503280981516330f4f?page=1)
[AI in space](https://spectrum.ieee.org/tech-talk/robotics/artificial-intelligence/ai-in-space)
[Nasa's Mars Unreal Engine](https://www.unrealengine.com/zh-CN/blog/nasa-is-using-unreal-engine-4-to-make-mars-a-virtual-reality?lang=zh-CN)
[Mars 2030](https://store.steampowered.com/app/510850/Mars_2030/)

**information:**

Previous missions to the moon have not generated enough high-resolution ground images to put together a training data set for the rover localization task, so used a simulation.

Reprojected view (using panoramic images) matched with true orbital view.

FDL is an artificial intelligence research program sponsored by NASA

The lab sponsors small groups of computer and planetary science researchers to work on important problems in space science for two months each summer.

Martian altimetry data from the University of Arizona’s HiRISE project?

---
_April 18, 2019_

**links:**
[HiRISE why](https://www.uahirise.org/faq/#Why)
[Face on Mars](https://science.nasa.gov/science-news/science-at-nasa/2001/ast24may_1/)
[HiView](https://www.uahirise.org/hiview/)
[Mars science laboratory](https://mars.jpl.nasa.gov/msl/sitemap/)
[Mars institute](https://www.marsinstitute.no/)
[Trek map](https://trek.nasa.gov/mars/)
[Global topography of Mars](https://tharsis.gsfc.nasa.gov/global_paper.html)
[HiRISE data](https://hirise-pds.lpl.arizona.edu/PDS/)


**information:**

Spirit mission, sol 639, mosaic, Nav source, 10 frames total, Unknown.

"Range to target site" is the distance between the HiRISE camera and the spot on Mars captured in the image, in Km.

Raw data -> radiometically calibrated (to correct stripes, mismatch, and other camera artifacts), Geometrically projected (to map the image onto planetary coordinates). Do it with ISIS software.

How Long Does it Take for an Image to Get Processed?
After an image is acquired by the HiRISE camera, it takes about 15 minutes to transmit it from the spacecraft to Earth, via the Deep Space Network (DSN). It can take a few hours for the data to be transmitted from the DSN to JPL, and JPL then sends the data to HiROC within an hour. Once an image is received by HiROC computers, it takes about two hours for our pipelines to process it. We then have to wait a week for the ephemerides (position of spacecraft relative to Mars) data to be constructed. After that, it takes about two hours to complete the remainder of the image processing.

Camera coordinates are converted to map projection coordinates. This means that North is up in the image, and that every pixel is associated with Mars planetary coordinates. 

XYL with RDR files
FFL with EDR files

HiRISE is located 300 km above the surface.

Lat 40.745 Lon 350.543 - Landform similar to a human face.

Rover On-board memory includes 254MB of DRAM, 2GB of Flash memory both with error dection and corection, and 256 KB of EEPROM. 

MRO cartography?

The coordinate system  used  is  planetocentric  latitude  and  east  positive  longitude direction.  The planetocentric latitude is the angle from the equator to a point on the surface of an oblate planet. The longitude increases from west to east (left to right).

---
_April 19, 2019_

**links:**
[MER Navcam data](https://pds-imaging.jpl.nasa.gov/volumes/mer.html)

**information:**

There are roughly 4000 Navcam mosaics of which 376 are polar and 420 are vertical projection. The remainder are a combination of cylindrical and perspective projections. For MERB (Opportunity), those numbers more than double.

The mosaics are in the two Camera RDR Mosaics directories mer1om_0xxx and mer2ox_0xxx. Many of the mosaics have ".LIS" files that list the source products used in the mosaic.