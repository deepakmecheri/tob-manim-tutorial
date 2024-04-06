FROM mcr.microsoft.com/devcontainers/universal:2

RUN sudo apt update \
    && sudo apt -y install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg \
    && sudo apt -y install python3-pip \
    && sudo apt -y install texlive texlive-latex-extra \
    && pip3 install manim

