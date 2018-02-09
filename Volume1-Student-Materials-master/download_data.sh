#!/bin/bash
# Download the data files for this volume and put them in the right folders.

SOURCE="https://github.com/Foundations-of-Applied-Mathematics/Data.git"
GIT="https://git-scm.com"
TEMPDIR="_DATA_"`date +%s`"_"
PYTHONESSENTIALS="$TEMPDIR/PythonEssentials"
VOLUME1="$TEMPDIR/Volume1"
VOLUME2="$TEMPDIR/Volume2"
VOLUME3="$TEMPDIR/Volume3"
VOLUME4="$TEMPDIR/Volume4"

# Check that git is installed.
command -v git > /dev/null ||
{ echo -e "\nERROR: git is required. Download it at $GIT.\n"; exit 1; }

# Download the data using git sparse checkout and git lfs.
mkdir $TEMPDIR
cd $TEMPDIR
git init --quiet
echo -e "\nInitializing Download ...\n"
git remote add -f origin $SOURCE
git config core.sparseCheckout true
echo "Volume1" >> .git/info/sparse-checkout
git pull origin master
cd ../

# Migrate the files from the temporary folder.
set +e
echo -e "\nMigrating files ..."

cp $VOLUME1/horse.npy LinearTransformations/
cp $VOLUME1/circle.npy LeastSquares_Eigenvalues/
cp $VOLUME1/ellipse.npy LeastSquares_Eigenvalues/
cp $VOLUME1/housing.npy LeastSquares_Eigenvalues/
cp $VOLUME1/dream.png ImageSegmentation/
cp $VOLUME1/hubble.jpg SVD_ImageCompression/
cp $VOLUME1/hubble_gray.jpg SVD_ImageCompression/
cp $VOLUME1/faces94.zip FacialRecognition/
cp $VOLUME1/plane.npy Differentiation/
cp $VOLUME1/stability_data.npy Conditioning_Stability/
cp $VOLUME1/matrix.txt PageRank/
cp $VOLUME1/ncaa2013.csv PageRank/
cp $VOLUME1/social_network.csv DrazinInverse/

# Delete the temporary folder.
rm -rf $TEMPDIR
echo -e "\nDone.\n"
