FROM ubuntu:18.04 as simple_image

run apt-get update && apt-get install -yq python3 python3-pip python3-venv git && apt-get clean

run python3 -m venv general && bash -c "source /general/bin/activate && pip install --upgrade pip && pip install wheel pytest coverage pytest-cov hypothesis"

run python3 -m venv general && bash -c "source /general/bin/activate && pip install numpy"

COPY . /simple










