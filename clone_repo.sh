#!/bin/bash
#chmod a+x clone_repo.sh

set -e

echo "Cloning repositories we need for this project to utils"
cd utils
git clone https://github.com/youyoubilly/jetcam_b.git