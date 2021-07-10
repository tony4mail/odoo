FROM odoo:13
MAINTAINER tony4mail@gmail.com
SHELL ["/bin/bash", "-xo", "pipefail", "-c"]
USER root
COPY . /mnt/extra-addons
RUN chown -R root:root /mnt/extra-addons
