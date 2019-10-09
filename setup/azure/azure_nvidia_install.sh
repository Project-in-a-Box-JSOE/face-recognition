# Prepare system packages for use
echo -e "\n\n-----------------------------------\nConfiguring Packages...\n-----------------------------------\n\n"
# sudo dpkg --configure -a # Only used for NVIDIA img / Needs supervision
sudo apt update
# sudo apt install -y git # Only used for NVIDIA img

# Install pip3 for python
echo -e "\n\n-----------------------------------\nInstalling pip\n-----------------------------------\n\n"
sudo apt install -y python3-pip

# Install CUDA requisites
echo -e "\n\n-----------------------------------\nInstalling CUDA Toolkit\n-----------------------------------\n\n"
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub && sudo apt update
sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt update
sudo apt install -y cuda-10-0 cuda-toolkit-10-0
rm cuda-repo-ubuntu1804_10.0.130-1_amd64.deb

# Install cuDNN 7 + NCCL
echo -e "\n\n-----------------------------------\nInstalling cuDNN & NCCL\n-----------------------------------\n\n"
wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo dpkg -i nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt update
sudo apt install -y libcudnn7 libcudnn7-dev libnccl2 libc-ares-dev
rm nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb

# Link libaries to proper locations & update PATH
echo -e "\n\n-----------------------------------\nLinking libraries & updating PATH\n-----------------------------------\n\n"
sudo mkdir -p /usr/local/cuda-10.0/nccl/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libnccl.so.2 /usr/local/cuda-10.0/nccl/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libcudnn.so.7 /usr/local/cuda-10.0/nccl/lib
echo "# Path Prepending for CUDA" >> ~/.bashrc
echo 'export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc

# Install TensorFlow given .whl from repository
echo -e "\n\n-----------------------------------\nInstalling Tensorflow from Git\n-----------------------------------\n\n"
wget https://github.com/ProjectInABox/face-recognition/blob/master/setup/azure/tfwhlaa?raw=true
wget https://github.com/ProjectInABox/face-recognition/blob/master/setup/azure/tfwhlab?raw=true
wget https://github.com/ProjectInABox/face-recognition/blob/master/setup/azure/tfwhlac?raw=true
wget https://github.com/ProjectInABox/face-recognition/blob/master/setup/azure/tfwhlad?raw=true
cat tfwhl* > tensorflow-1.15.0rc3-cp36-cp36m-linux_x86_64.whl
rm tfwhl*
pip3 install tensorflow-1.15.0rc3-cp36-cp36m-linux_x86_64.whl

# Test TensorFlow Installation
echo -e "\n\n-----------------------------------\nENSURE OUTPUT IS 1!!!!\n-----------------------------------\n\n"
python3 -c "import tensorflow as tf; print(tf.contrib.eager.num_gpus())"

# Exit with success
exit 0
