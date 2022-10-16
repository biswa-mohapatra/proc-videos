echo [$(date)]: "START"
echo [$(date)]: "Calling conda.sh"
. C:/Users/DELL/Anaconda3/etc/profile.d/conda.sh
echo [$(date)]: "Creating enviroment"
conda create --prefix ./env python>=3.7 -y
echo [$(date)]: "Activate enviroment"
source activate ./env
echo [$(date)]: "install requirements"
pip install -r requirements.txt
echo [$(date)]: "END"