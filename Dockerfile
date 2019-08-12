FROM ubuntu:18.04 as simple_image

run apt-get update && apt-get install -yq --no-install-recommends python3=3.6.7-1~18.04 python3-pip=9.0.1-2.3~ubuntu1.18.04.1 python3-venv=3.6.7-1~18.04 git=1:2.17.1-1ubuntu0.4 && apt-get clean && rm -rf /var/lib/apt/lists/*

run python3 -m venv general && bash -c "source /general/bin/activate && pip install --upgrade pip && pip install wheel pytest coverage pytest-cov hypothesis numpy"

COPY . /simple
