/* access location of data */
LIBNAME mydata "/courses/d1406ae5ba27fe300 " access=readonly;

/* access relevant data set */
/* DATA new; creates a new, temporary data set */
/* set mydata.marscrater_pds; calls the relevant data set and gives it the name chosen in the previous step, here "mydata" */
DATA new; set mydata.marscrater_pds;

/* Add descriptive data labels. */
LABEL 	DIAM_CIRCLE_IMAGE="Crater Diameter"
	 	DEPTH_RIMFLOOR_TOPOG="Crater Depth"
	 	MORPHOLOGY_EJECTA_1="Ejecta Morphology 1"
	 	MORPHOLOGY_EJECTA_2="Ejecta Morphology 2"
	 	MORPHOLOGY_EJECTA_3="Ejecta Morphology 3"
	 	NUMBER_LAYERS="Number of Crater Layers";

/* Subset data to exclude craters without recorded ejecta morphologies (EM) */
/* Also excluding EM1 type Rd which represents more than 50% of the remaining entries */
/* ne = "not equal" */
IF MORPHOLOGY_EJECTA_1 ne " ";
/* IF MORPHOLOGY_EJECTA_1 ne "Rd"; */

/* PROC SORT; indicates you want to preform a PROCedure on the data as it's imported (here, should be sorted) */
/* by CRATER_ID; indicates which variable the data should be sorted by */
PROC SORT; by CRATER_ID;

/* PROC FREQ; compute varible frequencies */
/* TABLES return as tables frequcies for the listed variables */
/* run; executes all previous calls */
/* breaking into several pieces to try and reduce run times, but can list many variables on a sinlge line  */
/* PROC FREQ; TABLES DIAM_CIRCLE_IMAGE; */
PROC FREQ; TABLES DEPTH_RIMFLOOR_TOPOG;
PROC FREQ; TABLES MORPHOLOGY_EJECTA_1;
/* PROC FREQ; TABLES MORPHOLOGY_EJECTA_2; */
/* PROC FREQ; TABLES MORPHOLOGY_EJECTA_3; */
/* PROC FREQ; TABLES NUMBER_LAYERS; */
run;