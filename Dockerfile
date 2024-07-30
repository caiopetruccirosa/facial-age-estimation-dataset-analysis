# **********************
#       Base Image      
# **********************

# Base images possibilities use CUDA 11.3 or 11.7 and cuDNN 8.0:
#     pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime (ligher)
#     nvcr.io/nvidia/pytorch:22.12-py3
# FROM nvcr.io/nvidia/pytorch:22.12-py3
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# *********************
#     Env Variables    
# *********************

ARG USERNAME=caio.rosa
ARG USER_UID=10399
ARG USER_GID=1000
ARG USER_GNAME=recod

ARG EXPOSED_PORT=4321

ARG DEBIAN_FRONTEND=noninteractive


# **********************
#   Package Management  
# **********************

# Install base utilities and common apt packages
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates apt-utils && \
    apt-get install -y software-properties-common build-essential

# # Add nvtop apt repository
# RUN add-apt-repository ppa:flexiondotorg/nvtop

RUN apt-get update && \
    apt-get install -y \
        wget git nano vim ffmpeg libgl1-mesa-glx libglib2.0-0 \
        bzip2 cmake curl htop libssl-dev nvtop net-tools pandoc \
        python3-sphinx tmux tree unrar unzip xdot fonts-powerline

# Anything else you want to do like clean up goes here *
RUN rm -rf /var/lib/apt/lists/* && \
    ldconfig && \
    apt autoremove && \
    apt clean

# System-wide python packages
RUN python -m pip install --upgrade pip setuptools pytest && \
    python -m pip install jupyterlab ipykernel ipywidgets nbformat \
        black kaleido lightning>=2.1.0 \
        matplotlib numpy pandas plotly seaborn scipy \
        torchmetrics torchvision torchsummary timm tifffile

# # Install project dependencies
# COPY requirements.txt .
# RUN yes | pip install -r .

# ***********************
#   Shell Configuration  
# ***********************

# Terminal colors with xterm
ENV TERM=xterm

# Set the zsh theme
ENV ZSH_THEME=agnoster

# Run Oh-My-Zsh installation script
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true


# **********************
#   User Configuration  
# **********************

# Creates a new group with the specified GID and group name.
RUN groupadd --gid $USER_GID $USER_GNAME

# Creates a new user with the specified UID, GID, and username. The -m flag creates a home directory for the user.
RUN useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Updates the package list from the repositories and installs the sudo package.
RUN apt-get update && apt-get install -y sudo

# Configures the newly created user to have passwordless sudo access.
RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME

# Sets the correct permissions for the sudoers file to ensure security.
RUN chmod 0440 /etc/sudoers.d/$USERNAME

# Changes the ownership of the home directory to the new user and group, ensuring that the user has the appropriate permissions for their home directory
RUN chown -R $USER_UID:$USER_GID /home/$USERNAME

# Changes the default shell for the user to zsh
RUN chsh --shell /bin/zsh $USERNAME

#  Set the default user
USER $USERNAME