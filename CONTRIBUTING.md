## Welcome to the automated padel court booking system!

### Installing pdm

We use pdm for dependency management, to install it, follow the steps below:

```bash
sudo apt install python3.12
sudo apt install python3.12-venv
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
echo "export PATH=/home/iarribillaga/.local/bin:$PATH" >> /home/$USER/.bashrc
```

## Installing docker

In linux, follow the steps in https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository.

Then, add your user to the docker group:

```bash
sudo usermod -aG docker $USER
sudo su <your user>
```